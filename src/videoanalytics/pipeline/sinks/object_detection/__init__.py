# -*- coding: utf-8 -*-

"""
The main module contains classes and methods for tasks related with object detection. 

Format conventions
^^^^^^^^^^^^^^^^^^

The are different conventions to represent bounding boxes, being some of them:

- Each bounding box is represented by its top left coordinates and width and height in absolute  
  values (pixels). This is the most convenient format for extracting patches or annotating.
- Each bounding box is represented by its center coordinates and width and height in normalized values 
  (0.0-1.0). This is the format used by YOLO.

Modules :mod:`utils` and :mod:`evaluation` contain utilities for working with different formats.

The adopted format for representing the detections in the global context is storing a tuple with
the entry name "DETECTIONS" with the following components:

- *out_boxes*: a list of boxes in absolute coordinates (top left, width, height, in pixels).
- *out_scores*: a list of the scores (confidence) for each predicted box (0.0-1.0).
- *out_classes*: a list of the class numeric identifier for each box (:math:`0,...,n_{classes}-1`)
- *num_boxes*: the size of the list


The convention used for CSV format in components is to store the each detection as a row.
The columns are:

- *frame_num*: frame number, incremented from variable "START_FRAME" at iteration zero.
- *class_idx*: numeric identifier of the detected class.
- *x,y*: top left bounding box coordinate in pixels.
- *w,h*: width and height of the bounding box in pixels.
- *score*: confidence for the detection.
- *filename (optional)*: this field is fulfilled with the "IMG_FILENAME" variable, if present in the context.

"""

from videoanalytics.utils import read_class_names
import colorsys
import random
import cv2
import csv
import numpy as np
import pandas as pd
import os

from videoanalytics.pipeline import Sink

class DetectionsAnnotator(Sink):
    '''
    Annotates the detections in a frame displaying a bounding box around each 
    identified object.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | DETECTIONS        | Output of an object detection model.                |
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
        class_names_filename (str): text file with class names.
        show_label (bool): display class name in bounding box.
        context_name(str): name of the variable in the context containing detections.
    '''
    def __init__(self, name, context, class_names_filename,context_name="DETECTIONS",show_label=True):
        super().__init__(name, context)
        self.class_names = read_class_names(class_names_filename)
        self.show_label = show_label
        self.num_classes = len(self.class_names)
        self.hsv_tuples = [(1.0 * x / self.num_classes, 1., 1.) for x in range(self.num_classes)]
        
        self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), self.hsv_tuples))
        self.colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), self.colors))

        random.seed(0)
        random.shuffle(self.colors)
        random.seed(None)

        self.frame_counter=0     
        
        self.context_name = context_name
        
    def setup(self):        
        pass
            
    def process(self):           
        out_boxes, out_scores, out_classes, num_boxes = self.context[self.context_name]
        image_h, image_w, _ = self.context["FRAME"].shape
        for i in range(num_boxes):
            if int(out_classes[i]) < 0 or int(out_classes[i]) > self.num_classes: continue
            x,y,w,h = out_boxes[i]
            fontScale = 0.5
            score = out_scores[i]
            class_ind = int(out_classes[i])
            class_name =  self.class_names[class_ind]
            bbox_color = self.colors[class_ind]
            bbox_thick = int(0.6 * (image_h + image_w) / 600)
            c1, c2 = (x, y), (x + w, y + h)
            cv2.rectangle(self.context["FRAME"], (int(x),int(y)), (int(x + w),int(y+h)), bbox_color, bbox_thick)
            
            #print("Object found: {}, Confidence: {:.2f}, BBox Coords (xmin, ymin, width, height): {}, {}, {}, {} ".format(class_name, score, x, y, w, h))

            if self.show_label:
                bbox_mess = '%s: %.2f' % (class_name, score)
                t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness=bbox_thick // 2)[0]
                c3 = (c1[0] + t_size[0], c1[1] - t_size[1] - 3)
                cv2.rectangle(self.context["FRAME"], (int(x),int(y)), (int(c3[0]), int(c3[1])), bbox_color, -1) #filled
                cv2.putText(self.context["FRAME"], bbox_mess, (int(c1[0]), int(c1[1] - 2)), cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale, (0, 0, 0), bbox_thick // 2, lineType=cv2.LINE_AA)
            
            self.frame_counter+=1     
            
    def shutdown(self):        
        pass

class DetectionsCSVWriter(Sink):
    '''
    Writes the detections to a CSV file.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | DETECTIONS        | Output of an object detection model.                |
    +-------------------+-----------------------------------------------------+
    | FRAME             | Numpy array representing the frame.                 |
    +-------------------+-----------------------------------------------------+
    | START_FRAME       | Initial frame index.                                |
    +-------------------+-----------------------------------------------------+
    | IMG_FILENAME (*)  | Image filename (for image sequences)                |
    +-------------------+-----------------------------------------------------+

    (*) Optional.

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        filename (str): CSV output file.
        show_label (bool): display class name in bounding box.
        context_name(str): name of the variable in the context containing detections.
    '''
    def __init__(self, name, context,filename,context_name="DETECTIONS"):
        super().__init__(name, context)
        self.csv_file = open(filename, mode='w')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', 
                                     quoting=csv.QUOTE_MINIMAL)
        self.context_name=context_name
        
    def setup(self):                
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):        
        out_boxes, out_scores, out_classes, num_boxes = self.context[self.context_name]
        for i in range(num_boxes):
            x,y,w,h = out_boxes[i]            
            score = out_scores[i]
            class_idx = int(out_classes[i])   

            # if filename is available, append it
            filename = self.context['IMG_FILENAME'] if 'IMG_FILENAME' in self.context else ""

            self.csv_writer.writerow([self.frame_counter, class_idx, 
                     x,y,w,h,
                     score,
                     filename
                ])
            
        self.frame_counter+=1
            
    def shutdown(self):        
        self.csv_file.close()        


class ObjectDetectorCSV(Sink):     
    '''
    This components reads precomputed detections from a CSV file.
    
    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | START_FRAME       | Initial frame index.                                |
    +-------------------+-----------------------------------------------------+
  
    This component **WRITES** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | DETECTIONS        | Output of an object detection model.                |
    +-------------------+-----------------------------------------------------+    

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        class_names_filename (str): text file with class names.
        show_label (bool): display class name in bounding box.
        context_name(str): name of the variable in the context containing detections.
    '''   
    def __init__(self, name, context,filename, context_name="DETECTIONS"):
        super().__init__(name, context)
        
        det_columns = ["frame_num","class_idx", "x","y","w","h","score","filename"]        
        self.df = pd.read_csv(filename,names=det_columns)
        self.context_name = context_name
                
    def setup(self):        
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):        
        self.context[self.context_name] = []
        out_boxes = []
        out_scores = []
        out_classes = []
        for r in self.df[self.df.frame_num==self.frame_counter].iterrows():
            x,y,w,h = int(r[1].x),int(r[1].y),int(r[1].w),int(r[1].h)
            out_boxes.append((x,y,w,h))
            out_scores.append(r[1].score)
            out_classes.append(r[1].class_idx)
            
        self.context[self.context_name] = [out_boxes, out_scores, out_classes, len(out_boxes)]
        self.frame_counter+=1
    
    def shutdown(self):
        pass
