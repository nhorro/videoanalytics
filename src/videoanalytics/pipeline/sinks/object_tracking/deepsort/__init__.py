# -*- coding: utf-8 -*-

"""
Implementation of DeepSORT tracking algorithm. 

.. admonition:: Note

    The code included in this module is only a wrapper class for the
    `original paper's code <https://github.com/nwojke/deep_sort/>`__
    with minor changes to adjust documentation format or minor refactoring.
"""

import numpy as np
import pandas as pd
import cv2

from videoanalytics.pipeline import Sink

from .feature_extractor import create_box_encoder
from .nn_matching import NearestNeighborDistanceMetric
from .tracker import Tracker
from .detection import Detection


class DeepSORT(Sink):
    '''
    Wrapper class for the DeepSORT algorithm.

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
        model_filename(str): filename for the reidentification model.
    '''
    def __init__(self, name, context, model_filename):
        super().__init__(name, context)
        self.relative_frame_counter = 0            

        # Definition of the parameters
        self.max_cosine_distance = 0.4
        self.nn_budget = None
        self.encoder = create_box_encoder(model_filename, batch_size=1)
        
        # calculate cosine distance metric
        self.metric = NearestNeighborDistanceMetric("cosine", self.max_cosine_distance, self.nn_budget)
        # initialize tracker
        self.mot_tracker = Tracker(self.metric)

        
    def setup(self):                        
        self.frame_counter = self.context["START_FRAME"]
        
    def process(self):        
        self.context["TRACKED_OBJS"] = []
        out_boxes, out_scores, out_classes, num_boxes = self.context["DETECTIONS"]
        if num_boxes>0:    
            # encode yolo detections and feed to tracker
            features = self.encoder (self.context["FRAME"], out_boxes)
            detections = [Detection(bbox, score, class_idx, feature) for bbox, score, class_idx, feature in zip(out_boxes, out_scores, out_classes, features)]
        else:            
            detections = None
        
        # Call the tracker
        self.mot_tracker.predict()
        if detections:
            self.mot_tracker.update(detections)

        # update tracks
        for track in self.mot_tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue 
            bbox = track.to_tlwh()
            x,y,w,h = bbox[0],bbox[1],bbox[2],bbox[3]
            obj_id = track.track_id
            self.context["TRACKED_OBJS"].append([obj_id,x,y,w,h])
      
        self.frame_counter+=1
        self.relative_frame_counter +=1
        pass
            
    def shutdown(self):        
        pass