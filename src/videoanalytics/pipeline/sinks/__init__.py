import cv2
import numpy as np

from videoanalytics.pipeline import Sink

class VideoWriter(Sink):
    def __init__(self, context,filename,output_format="XVID"):
        super().__init__(context)
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
        print("Shutting down VideoWriter. Video saved to %s" % self.filename )
        self.out.release()   