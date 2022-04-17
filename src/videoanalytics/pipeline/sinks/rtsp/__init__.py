
import cv2
import subprocess as sp

from videoanalytics.pipeline import Sink

class RTSPPublisher(Sink):
    '''
    Publishes to RTSP using FFMPEG.

    This component **READS** the following entries:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | FRAME             | Current frame.                                      |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
    '''
    def __init__(self, name, context, rstp_output_server):
        super().__init__(name, context)
        self.rstp_output_server = rstp_output_server

    def setup(self):           
        
        # FIXME: get from context, or make configurable
        size_str = str(int(320)) + 'x' + str(int(240))
        fps = 30
        command = ['ffmpeg',
               
               # Input
               '-re',
               '-s', size_str,
               '-r', str(fps),  # rtsp fps (from input server)
               '-i', '-',               

               # Image format (tweakable)
               '-pix_fmt', 'yuv420p',
               '-r', '30',  # output fps
               '-g', '50',
               '-c:v', 'libx264',
               '-b:v', '2M',
               '-bufsize', '64M',
               '-maxrate', "4M",
               '-preset', 'veryfast',               
               '-segment_times', '5',

               # Output format
               '-f', 'rtsp',
               '-rtsp_transport', 'tcp',
               self.rstp_output_server]
        self.ffmpeg_process = sp.Popen(command, stdin=sp.PIPE)
        self.frame_counter = self.context["START_FRAME"]

    def process(self):        
        converted = cv2.cvtColor(self.context["FRAME"], cv2.COLOR_RGB2BGR)     
        ret, frame = cv2.imencode('.png', converted)
        self.ffmpeg_process.stdin.write(frame.tobytes())
        self.frame_counter+=1

    def shutdown(self):        
        self.process.close()
        pass