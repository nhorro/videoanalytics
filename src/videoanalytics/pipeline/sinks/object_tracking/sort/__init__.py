# -*- coding: utf-8 -*-

"""
Implementation of SORT tracking algorithm.

.. admonition:: Note

    The code included in this module is only a wrapper class for the
    `original paper's code <https://github.com/abewley/sort>`__
    with minor changes to adjust documentation format or minor refactoring.

"""

import numpy as np
import pandas as pd
import cv2

from videoanalytics.pipeline.sinks.object_tracking.kalman import KalmanBoxTracker
from videoanalytics.utils.boundingboxes import iou_batch
from videoanalytics.pipeline import Sink

from videoanalytics.pipeline.sinks.object_tracking.linear_assignment import linear_assignment

def associate_detections_to_trackers(detections,trackers,iou_threshold = 0.3):
    """
    Assigns detections to tracked object (both represented as bounding boxes)
    Returns 3 lists of matches, unmatched_detections and unmatched_trackers
    """
    if(len(trackers)==0):
        return np.empty((0,2),dtype=int), np.arange(len(detections)), np.empty((0,5),dtype=int)

    iou_matrix = iou_batch(detections, trackers)

    if min(iou_matrix.shape) > 0:
        a = (iou_matrix > iou_threshold).astype(np.int32)
        if a.sum(1).max() == 1 and a.sum(0).max() == 1:
            matched_indices = np.stack(np.where(a), axis=1)
        else:
            matched_indices = linear_assignment(-iou_matrix)
    else:
        matched_indices = np.empty(shape=(0,2))

    unmatched_detections = []
    for d, det in enumerate(detections):
        if(d not in matched_indices[:,0]):
            unmatched_detections.append(d)
    unmatched_trackers = []
    for t, trk in enumerate(trackers):
        if(t not in matched_indices[:,1]):
            unmatched_trackers.append(t)
            
    #filter out matched with low IOU
    matches = []
    for m in matched_indices:
        if(iou_matrix[m[0], m[1]]<iou_threshold):
            unmatched_detections.append(m[0])
            unmatched_trackers.append(m[1])
        else:
            matches.append(m.reshape(1,2))
    if(len(matches)==0):
        matches = np.empty((0,2),dtype=int)
    else:
        matches = np.concatenate(matches,axis=0)

    return matches, np.array(unmatched_detections), np.array(unmatched_trackers)         


class Sort(object):    
    '''
    SORT algorithm implementation.

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        max_age (int): age limit for a tracklet without being updated before removing it.
        min_hits (int): minimum hits required to start a new track.
        iou_threshold (float): minimum IoU to consider overlapping boxes.
    '''

    def __init__(self, max_age=1, min_hits=3, iou_threshold=0.3):
        """
        Sets key parameters for SORT
        """
        self.max_age = max_age
        self.min_hits = min_hits
        self.iou_threshold = iou_threshold
        self.trackers = []
        self.frame_count = 0

    def update(self, dets=np.empty((0, 5))):
        """
        Updates the internal state of the tracked objects. 
        This method must be called once for each frame even with empty detections (use np.empty((0, 5)) 
        for frames without detections).

        Args:
            dets - a numpy array of detections in the format [[x1,y1,x2,y2,score],[x1,y1,x2,y2,score],...]
            
        Returns 
            A similar array, where the last column is the object ID.
        
        Note: The number of objects returned may differ from the number of detections provided.
        """
        self.frame_count += 1
        
        # get predicted locations from existing trackers.
        trks = np.zeros((len(self.trackers), 5))
        to_del = []
        ret = []
        
        for t, trk in enumerate(trks):
            pos = self.trackers[t].predict()[0]
            trk[:] = [pos[0], pos[1], pos[2], pos[3], 0]
            if np.any(np.isnan(pos)):
                to_del.append(t)
        trks = np.ma.compress_rows(np.ma.masked_invalid(trks))
        for t in reversed(to_del):
            self.trackers.pop(t)
        matched, unmatched_dets, unmatched_trks = associate_detections_to_trackers(dets,trks, 
                                                                                   self.iou_threshold)

        # update matched trackers with assigned detections
        for m in matched:
            self.trackers[m[1]].update(dets[m[0], :])

        # create and initialise new trackers for unmatched detections
        for i in unmatched_dets:
            trk = KalmanBoxTracker(dets[i,:])
            self.trackers.append(trk)
        i = len(self.trackers)
        for trk in reversed(self.trackers):
            d = trk.get_state()[0]
            if (trk.time_since_update < 1) and (trk.hit_streak >= self.min_hits or self.frame_count <= self.min_hits):
                ret.append(np.concatenate((d,[trk.id+1])).reshape(1,-1)) # +1 as MOT benchmark requires positive
            i -= 1
            # remove dead tracklet
            if(trk.time_since_update > self.max_age):
                self.trackers.pop(i)
        if(len(ret)>0):
            return np.concatenate(ret)
        return np.empty((0,5))



class SORT(Sink):
    '''
    Wrapper class for the SORT algorithm.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | DETECTIONS        | Output of an object detection model.                |
    +-------------------+-----------------------------------------------------+
    | START_FRAME       | Initial frame index.                                |
    +-------------------+-----------------------------------------------------+

    This component **WRITES** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | TRACKED_OBJS      | Object trackings.                                   |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        max_age (int): age limit for a tracklet without being updated before removing it.
        min_hits (int): minimum hits required to start a new track.
        iou_threshold (float): minimum IoU to consider overlapping boxes.
    '''

    def __init__(self, name, context, max_age=1, min_hits=3, iou_threshold=0.3):
        super().__init__(name, context)
        self.relative_frame_counter = 0            
        KalmanBoxTracker.count = 0
        self.mot_tracker = Sort(max_age, min_hits, iou_threshold)        
        
    def setup(self):                        
        self.frame_counter = self.context["START_FRAME"]
        
    def process(self):
        out_boxes, out_scores, out_classes, num_boxes = self.context["DETECTIONS"]
        if num_boxes>0:    
            boxes,scores = np.array(out_boxes),np.array(out_scores).reshape(-1,1)
            dets = np.append(boxes, scores, axis=1) 
            dets[:, 2:4] += dets[:, 0:2] # convertir a x0,y0,x1,y1
            trackers = self.mot_tracker.update(dets)
            self.context["TRACKED_OBJS"] = []
        else:    
            trackers = self.mot_tracker.update()
          
        for d in trackers:
            x,y,w,h,obj_id = d[0],d[1],d[2]-d[0],d[3]-d[1],d[4]            
            self.context["TRACKED_OBJS"].append([obj_id,x,y,w,h])
            #print(obj_id,x,y,w,h)

        self.frame_counter+=1
        self.relative_frame_counter +=1
            
    def shutdown(self):        
        pass