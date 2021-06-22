# -*- coding: utf-8 -*-

"""
Loading and processing of polygonal regions of interest (ROIs).
"""

import colorsys
import random
import cv2
import numpy as np
import pandas as pd

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


from videoanalytics.pipeline import Sink
import json

class ROIView(Sink):        
    def __init__(self, context,filename):
        super().__init__(context)

        with open(filename) as f:
            self.rois = json.load(f)

        self.rois = self.rois["regions"]

        for i,v in enumerate(self.rois):
            self.rois[i]["polygon"] = np.int32([self.rois[i]["polygon"]])
            #print(self.rois[i]["polygon"])
   
    def setup(self):        
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):       
        if self.display_enabled:
            overlay = self.context["FRAME"].copy()

            alpha = 0.2  # Transparency factor.
            # Following line overlays transparent rectangle over the image
            
            for r in self.rois:
                cv2.fillPoly(overlay, pts = r["polygon"] , color = r["color"])
                cv2.polylines(overlay, r["polygon"] , 5, r["color"])
            self.context["FRAME"] = cv2.addWeighted(overlay, alpha, self.context["FRAME"], 1 - alpha, 0)            
        self.frame_counter+=1
    
    def shutdown(self):
        pass   


class ROIObjTest(Sink):        
    def __init__(self, context,filename):
        super().__init__(context)

        with open(filename) as f:
            self.rois = json.load(f)

        print(self.rois)
        self.rois = self.rois["regions"]


        for r in self.rois:
            r["activity"] = 0.

        for i,v in enumerate(self.rois):
            self.rois[i]["polygon_i32"] = np.int32([self.rois[i]["polygon"]])
            self.rois[i]["polygon"] = Polygon(self.rois[i]["polygon"])
   
    def setup(self):        
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):       
        out_boxes, out_scores, out_classes, num_boxes = self.context["DETECTIONS"]
        q_total = 0 
        for r in self.rois:
            r["activity"] = 0
            for i in range(num_boxes):
                x,y,w,h = out_boxes[i]         
                x = x+w/2
                y = y+h/2   
                score = out_scores[i]
                class_idx = int(out_classes[i])
                point = Point(x, y)
                self.context["FRAME"] = cv2.circle( self.context["FRAME"], (int(x),int(y)) , 5, (255,0,0))
                if r["polygon"].contains(point):
                    #print("Objeto adentro de {}".format(r["name"]))
                    r["activity"] += 1

                # Publicar variable
                self.context["q_{}".format(r["name"])]=r["activity"] 
            q_total+=r["activity"] 

            #if r["activity"] > 0:
            #    self.context["FRAME"] = cv2.polylines( self.context["FRAME"] , r["polygon_i32"] , 5, (0,0,255))
        self.context["q_total"] = q_total
            
        self.frame_counter+=1
    
    def shutdown(self):
        pass   
