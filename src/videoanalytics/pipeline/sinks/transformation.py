# -*- coding: utf-8 -*-

"""
Image transformations.
"""

import cv2
import numpy as np
import zmq
import logging

from videoanalytics.pipeline import Sink

logger = logging.getLogger(__name__)

class Resizer(Sink):
    def __init__(self, name, context, output_w,output_h):
        super().__init__(name,context)
        self.context = context
        self.output_w = output_w
        self.output_h = output_h
        
    def setup(self):
        pass
    
    def process(self):    
        self.context["FRAME"] = cv2.resize( 
            self.context["FRAME"],(self.output_w,self.output_h),
            interpolation=cv2.INTER_AREA)

    def shutdown(self):
        pass