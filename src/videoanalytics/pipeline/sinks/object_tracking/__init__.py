# -*- coding: utf-8 -*-

"""
This module contains generic components for tracking algorithms.
"""

import cv2
import numpy as np
import csv

from videoanalytics.pipeline import Sink

class TrackedObjectsAnnotator(Sink):
    '''
    Annotates the tracked objects in a frame displaying a bounding box around each 
    identified object with its numeric Id.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | TRACKED_OBJS      | Output of an object tracker.                        |
    +-------------------+-----------------------------------------------------+
    | FRAME             | Numpy array representing the frame.                 |
    +-------------------+-----------------------------------------------------+

    This component **WRITES** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | FRAME             | Numpy array representing the frame.                 |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
    '''
    def __init__(self, name, context):
        super().__init__(name, context)
                
    def setup(self):                        
        pass
        
    def process(self):
        fontScale = 0.4
        image_h, image_w, _ = self.context["FRAME"].shape
        bbox_color = (155,200,200)
        for d in self.context["TRACKED_OBJS"]:
            obj_id, x,y,w,h = int(d[0]), int(d[1]),int(d[2]),int(d[3]),int(d[4])
            score = d[4]            
            bbox_thick = int(0.6 * (image_h + image_w) / 400)
            c1, c2 = (x, y), (x + w, y + h)
            cv2.rectangle(self.context["FRAME"], (int(c1[0]),int(c1[1])), (int(c2[0]),int(c2[1])), bbox_color, bbox_thick)
            bbox_mess = 'ID %03d' % obj_id            
            t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness=bbox_thick // 2)[0]
            c3 = (c1[0] + t_size[0], c1[1] - t_size[1] - 3)
            cv2.rectangle(self.context["FRAME"], (int(c1[0]),int(c1[1])),
                (int(c3[0]), int(c3[1])), bbox_color, -1) #filled
            cv2.putText(self.context["FRAME"], bbox_mess, (int(c1[0]),int(c1[1] - 2)), 
                cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0, 0, 0), 
                bbox_thick // 2, lineType=cv2.LINE_AA)
            
    def shutdown(self):        
        pass



class TrackedObjectsCSVWriter(Sink):
    '''
    Writes the trackings to a CSV file.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | TRACKED_OBJS      | Output of an object tracker.                        |
    +-------------------+-----------------------------------------------------+
    | FRAME             | Numpy array representing the frame.                 |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        filename (str): CSV output file.
    '''
    def __init__(self, name, context, filename):
        super().__init__(name, context)
        self.csv_file = open(filename, mode='w')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self.frame_counter = 0
    def setup(self):                        
        pass
        
    def process(self):
        fontScale = 1.0
        image_h, image_w, _ = self.context["FRAME"].shape
        bbox_color = (155,200,200)
        for d in self.context["TRACKED_OBJS"]:
            obj_id, x,y,w,h = int(d[0]), int(d[1]),int(d[2]),int(d[3]),int(d[4])
            self.csv_writer.writerow([self.frame_counter, obj_id, 
                     x,y,w,h ])
        self.frame_counter+=1
            
    def shutdown(self):        
        self.csv_file.close()    
        pass    
