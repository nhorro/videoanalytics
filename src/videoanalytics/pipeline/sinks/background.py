# -*- coding: utf-8 -*-

"""
videoanalytics.pipeline.sinks.background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Components for background substraction and movement estimation.
"""

import numpy as np
import cv2

from videoanalytics.pipeline import Sink

class BackgroundExtractor1(Sink):
    def __init__(self, context):
        super().__init__(context)
        self.context = context
        self.subtractor = cv2.createBackgroundSubtractorMOG2()
        self.display_enabled = False
    def setup(self):
        pass
    
    def process(self):    
        mask = self.subtractor.apply(self.context["FRAME"])

        if self.display_enabled:
            self.context["FRAME"] = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        self.context["activity"] = np.sum(cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR))
        #print(self.context["actividad"])

    def shutdown(self):
        pass



class BackgroundExtractor2(Sink):
    def __init__(self, context):
        super().__init__(context)
        self.context = context
        self.count = 0
        self.display_enabled = False
        
    def setup(self):
        pass
    
    def process(self):    
        gray = cv2.cvtColor(self.context["FRAME"], cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        if self.count > 0:          
          difference = cv2.absdiff(gray,  self.prev_frame)
          _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY )
          
          if self.display_enabled:
            self.context["FRAME"] = cv2.cvtColor(difference, cv2.COLOR_GRAY2BGR)
          
        else:
            self.context["FRAME_TMP"] = gray
        self.prev_frame = gray
        self.count+=1

    def shutdown(self):
        pass        