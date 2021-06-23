# -*- coding: utf-8 -*-

"""
This module contains the Built-in sinks.
"""
import logging

import cv2
import numpy as np

from videoanalytics.pipeline import Sink

class VideoWriter(Sink):
    '''
    Writes video to a file using OpenCV writer.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | INPUT_FPS         | Input video FPS.                                    |
    +-------------------+-----------------------------------------------------+
    | INPUT_WIDTH       | Input video width in pixels.                        |
    +-------------------+-----------------------------------------------------+
    | INPUT_HEIGHT      | Input video height in pixels.                       |
    +-------------------+-----------------------------------------------------+
    | FRAME             | Numpy array representing the frame.                 |
    +-------------------+-----------------------------------------------------+

    Args:
        name(str): the component unique name.
        context (dict): The global context.         
        filename (str): output video filename.
        output_format (str): output format (default to XVID). 
                             Any format supported by OpenCV VideoWriter_fourcc.        
    '''
    
    logger = logging.getLogger(__name__)

    def __init__(self, name, context, filename,output_format="XVID"):
        super().__init__(name,context)
        self.filename = filename
        codec = cv2.VideoWriter_fourcc(*output_format)
        fps = self.context["INPUT_FPS"]
        width = self.context["INPUT_WIDTH"]
        height = self.context["INPUT_HEIGHT"]
        self.out = cv2.VideoWriter(self.filename, codec, fps, (width, height))
            
    def setup(self):
        pass
    
    def process(self):    
        converted = cv2.cvtColor(self.context["FRAME"], cv2.COLOR_RGB2BGR)        
        self.out.write( converted )
    
    def shutdown(self):
        self.logger.info("Shutting down VideoWriter. Video saved to %s" % self.filename )
        self.out.release()   

