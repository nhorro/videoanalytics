# -*- coding: utf-8 -*-

"""
videoanalytics.pipeline.sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Built-in sources.
"""

import os
import cv2
import numpy as np
from tqdm import tqdm

from videoanalytics.pipeline import Source

class VideoReader(Source):
    def __init__(self, context,video_path,
                 start_frame=0,max_frames=None,step_frames=None):
        super().__init__(context)
        self.processed_frames = 0
        self.cap = cv2.VideoCapture(video_path)
        
        video_frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.start_frame = start_frame
        self.max_frames = max_frames
        if self.max_frames is None:
            self.total_frames = video_frame_count-self.start_frame 
        else:
            self.total_frames = self.max_frames-self.start_frame 

        if self.total_frames>(video_frame_count-self.start_frame):
            self.total_frames=video_frame_count-self.start_frame
        
        if step_frames is None:
            self.step_frames = 1
        else:
            self.step_frames = step_frames

        self.context["INPUT_FPS"] = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.context["INPUT_WIDTH"] = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.context["INPUT_HEIGHT"] = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.context["START_FRAME"] =  self.start_frame
        self.context["TOTAL_FRAMES"] = self.total_frames
        self.context["STEP_FRAMES"] = self.step_frames
        self.progress_bar = tqdm(total=self.total_frames)

        self.skip_frames=0
        while self.skip_frames < self.start_frame:
            _ , _ = self.cap.read()
            self.skip_frames += 1
        
        print("Start frame:", self.start_frame)
        print("Total frames frame:", self.total_frames)
        print("Skipped frames :", self.skip_frames)
   
    def setup(self):
        #print("Setting up VideoReader")
        pass
    
    def read(self):
        
        if self.processed_frames < self.total_frames:
            if self.processed_frames % self.step_frames == 0:
                ret, frame = self.cap.read()
                self.processed_frames+=1
            else:
                while self.processed_frames % self.step_frames != 0 and self.processed_frames < self.total_frames:
                    ret, frame = self.cap.read()
                    self.processed_frames+=1

                if self.processed_frames > self.total_frames:
                    ret = False
                else:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #
            self.context['FRAME'] = frame
                
            update_every=int(os.getenv('UPDATE_PROGRESS_NFRAMES',self.step_frames))
            if (self.processed_frames -1) % update_every == 0:
                self.progress_bar.update(update_every)
                
        else:
            ret = False
        return ret
    
    def shutdown(self):
        #print("Shutting down VideoReader")
        self.cap.release()