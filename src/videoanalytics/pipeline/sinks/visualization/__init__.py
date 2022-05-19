# -*- coding: utf-8 -*-

"""
This module contains components for annotation, visualization and debugging.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import re
from videoanalytics.pipeline import Sink

class TextOverlay(Sink):        
    '''
    Component for displaying text.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | {VARIABLE_NAME}   | Variable names from the context can be indicated    |
    |                   | with "{}".                                          |
    +-------------------+-----------------------------------------------------+

    This component **WRITES** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    |  FRAME            | Displays the text over the frame.                   |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        text (str): text to display.
        x (int): horizontal position in pixels.
        y (int): vertical position in pixels.
        font_size (int): font size (FIXME: OpenCV units?)
    
    '''   
    def __init__(self, name, context,text,x,y,font_scale=1,font_weight=2):
        super().__init__(name, context)
        self.x=x
        self.y=y
        self.font_weight = font_weight
        self.font_scale = font_scale
        self.text=text
   
    def setup(self):        
        pass
        
    def process(self):               
        text = re.sub(r"\{([A-Za-z0-9_]+)\}", lambda x: str(self.context[x.group()[1:-1]]), self.text)
        dy = 60 # FIXME
        for i, line in enumerate(text.split('\n')):
            y = self.y + i*dy
            self.context["FRAME"] =  cv2.putText(
                self.context["FRAME"], 
                line, (self.x,y), cv2.FONT_HERSHEY_SIMPLEX, self.font_scale, (255,255,255), self.font_weight)
    
    def shutdown(self):
        pass   
