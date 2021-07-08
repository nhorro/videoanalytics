# -*- coding: utf-8 -*-

"""
This module contains the core components for video input.
"""

import os
import logging

import cv2
import numpy as np

from videoanalytics.pipeline import Source

class VideoReader(Source):
    logger = logging.getLogger(__name__)

    '''
    Reads video from a file using OpenCV capture device interface.

    This component **WRITES** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | INPUT_FPS         | Input video FPS.                                    |
    +-------------------+-----------------------------------------------------+
    | INPUT_WIDTH       | Input video width in pixels.                        |
    +-------------------+-----------------------------------------------------+
    | INPUT_HEIGHT      | Input video height in pixels.                       |
    +-------------------+-----------------------------------------------------+
    | START_FRAME       | Input video start frame.                            |
    +-------------------+-----------------------------------------------------+
    | TOTAL_FRAMES      | Input video width in pixels.                        |
    +-------------------+-----------------------------------------------------+
    | STEP_FRAMES       | Input video width in pixels.                        |
    +-------------------+-----------------------------------------------------+
    | FRAME             | Numpy array representing the frame.                 |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        video_path (str): input video filename.
        start_frame(int): start frame (default is 0).
        max_frames(int): maximum number of frames to read (default is 1).
        step_frames(int): default is 1, use other values to drop frames. 
                          This option is used for pipelines that can not cope with 
                          a high framerate.
    '''
    def __init__(self, name, context, video_path:str,
                 start_frame=0,max_frames=None,step_frames=1):
        super().__init__(name,context)
        self.processed_frames = 0

        if not os.path.isfile(video_path):
            raise ValueError("File {} does not exist".format(video_path))
        
        self.cap = cv2.VideoCapture(video_path)
        
        video_frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.start_frame = start_frame
        self.max_frames = max_frames
        if self.max_frames is None:
            self.total_frames = video_frame_count-self.start_frame 
        else:
            self.total_frames = self.max_frames 

        if self.total_frames>(video_frame_count-self.start_frame):
            self.total_frames=video_frame_count-self.start_frame
        
        self.step_frames = step_frames

        self.context["INPUT_FPS"] = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.context["INPUT_WIDTH"] = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.context["INPUT_HEIGHT"] = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.context["START_FRAME"] =  self.start_frame
        self.context["TOTAL_FRAMES"] = self.total_frames
        self.context["STEP_FRAMES"] = self.step_frames
        
        self.progress= 0 
        
        self.logger.info("Start frame:", self.start_frame)
        self.logger.info("Total frames:", self.total_frames)
        self.logger.info("Step frames :", self.step_frames)
   
    def setup(self):
        pass
    
    def read(self):        
        ret = False        
        if self.processed_frames < self.total_frames:
            ret, frame = self.cap.read()
            
            if ret:
                self.context['FRAME'] = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.processed_frames+=1
                self.progress=(self.processed_frames/self.total_frames)*100.0
        return ret

    def get_progress(self):
        return self.progress
    
    def shutdown(self):
        self.logger.info("Shutting down VideoReader")
        self.cap.release()



class ImageSequenceReader(Source):
    logger = logging.getLogger(__name__)

    '''
    Reads sequence of images from a list of files.

    This component **WRITES** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | IMG_FILENAME      | Input image name.                                   |
    +-------------------+-----------------------------------------------------+
    | INPUT_WIDTH       | Input image width in pixels.                        |
    +-------------------+-----------------------------------------------------+
    | INPUT_HEIGHT      | Input image height in pixels.                       |
    +-------------------+-----------------------------------------------------+
    | FRAME             | Numpy array representing the frame.                 |
    +-------------------+-----------------------------------------------------+
    | START_FRAME       | First element of the sequence (always 0, only for   |
    |                   | compatibility with other sources)                   |
    +-------------------+-----------------------------------------------------+
    | TOTAL_FRAMES      | Length of the image sequence.                       |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        img_seq (list): sequence of images.        
    '''
    def __init__(self, name, context, img_seq:list):
        super().__init__(name,context)
        self.processed_frames = 0
        self.img_seq = img_seq
        self.processed_frames = 0
        self.total_frames = len(img_seq)

        self.context["START_FRAME"] = 0
        self.context["TOTAL_FRAMES"] = self.total_frames
        
    def setup(self):
        pass
    
    def read(self):    
        ret = False
        if self.processed_frames < self.total_frames:
            img_filename =  self.img_seq[self.processed_frames]
            frame = cv2.imread(img_filename)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)        
            self.context["FRAME"] = frame

            img_basename = os.path.splitext(os.path.basename(img_filename))[0]
            self.context['IMG_FILENAME'] = img_basename
            self.progress = (self.processed_frames/self.total_frames)*100.0
            self.processed_frames+=1
            ret = True
        return ret

    def get_progress(self):
        return self.progress        
    
    def shutdown(self):
        pass