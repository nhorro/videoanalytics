# -*- coding: utf-8 -*-

"""
Resize a frame.
"""

import cv2
import numpy as np
import zmq

from videoanalytics.pipeline import Sink

class Resizer(Sink):
    def __init__(self, context, output_w,output_h):
        super().__init__(context)
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
        self.sock.close()