# -*- coding: utf-8 -*-

"""
Implementation-independent object detection related components.
"""

from videoanalytics.utils import read_class_names
import colorsys
import random
import cv2
import csv
import numpy as np
import pandas as pd

from videoanalytics.pipeline import Sink

class DetectionsAnnotator(Sink):
    def __init__(self, context, class_names_filename,show_label=True):
        super().__init__(context)
        self.class_names = read_class_names(class_names_filename)
        self.show_label = show_label
        self.num_classes = len(self.class_names)
        self.hsv_tuples = [(1.0 * x / self.num_classes, 1., 1.) for x in range(self.num_classes)]
        
        self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), self.hsv_tuples))
        self.colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), self.colors))

        random.seed(0)
        random.shuffle(self.colors)
        random.seed(None)
        
    def setup(self):        
        n_frames = self.context["TOTAL_FRAMES"]
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):           
        out_boxes, out_scores, out_classes, num_boxes = self.context["DETECTIONS"]
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
            cv2.rectangle(self.context["FRAME"], c1, c2, bbox_color, bbox_thick)
            
            #print("Object found: {}, Confidence: {:.2f}, BBox Coords (xmin, ymin, width, height): {}, {}, {}, {} ".format(class_name, score, x, y, w, h))

            if self.show_label:
                bbox_mess = '%s: %.2f' % (class_name, score)
                t_size = cv2.getTextSize(bbox_mess, 0, fontScale, thickness=bbox_thick // 2)[0]
                c3 = (c1[0] + t_size[0], c1[1] - t_size[1] - 3)
                cv2.rectangle(self.context["FRAME"], c1, (np.float32(c3[0]), np.float32(c3[1])), bbox_color, -1) #filled
                cv2.putText(self.context["FRAME"], bbox_mess, (c1[0], np.float32(c1[1] - 2)), cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale, (0, 0, 0), bbox_thick // 2, lineType=cv2.LINE_AA)
            
            self.frame_counter+=1     
            
    def shutdown(self):        
        pass

class DetectionsCSVWriter(Sink):
    def __init__(self, context):
        super().__init__(context)
        self.csv_file = open("detections.csv", mode='w')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
    def setup(self):                
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):        
        out_boxes, out_scores, out_classes, num_boxes = self.context["DETECTIONS"]
        for i in range(num_boxes):
            x,y,w,h = out_boxes[i]            
            score = out_scores[i]
            class_idx = int(out_classes[i])                                   
            self.csv_writer.writerow([self.frame_counter, class_idx, 
                     x,y,w,h,
                     score
                ])
            
        self.frame_counter+=1
            
    def shutdown(self):        
        self.csv_file.close()        


class ObjectDetectorCSV(Sink):        
    def __init__(self, context,filename):
        super().__init__(context)
        
        det_columns = ["frame_num","class_idx", "x","y","w","h","score"]        
        self.df = pd.read_csv(filename,names=det_columns)
                
    def setup(self):        
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):        
        self.context["DETECTIONS"] = []
        out_boxes = []
        out_scores = []
        out_classes = []
        for r in self.df[self.df.frame_num==self.frame_counter].iterrows():
            x,y,w,h = int(r[1].x),int(r[1].y),int(r[1].w),int(r[1].h)
            out_boxes.append((x,y,w,h))
            out_scores.append(r[1].score)
            out_classes.append(r[1].class_idx)
            
        self.context["DETECTIONS"] = [out_boxes, out_scores, out_classes, len(out_boxes)]
        self.frame_counter+=1
    
    def shutdown(self):
        pass        