# -*- coding: utf-8 -*-

"""
videoanalytics.pipeline.sinks.zmqpub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Publish a frame in ZMQ. This componente is meant to be used with 
`nhorro/mpeg-streamer-service docker image <https://hub.docker.com/r/nhorro/mpeg-streamer-service/>`.

.. code-block:: console
    
    docker run -it --rm --name videoservice --network="host" nhorro/mpeg-streamer-service http://localhost:5000/video_feed
"""

import cv2
import numpy as np
import zmq

from videoanalytics.pipeline import Sink

class ZMQPub(Sink):
    def __init__(self, context,endpoint="tcp://127.0.0.1:5600"):
        super().__init__(context)
        self.endpoint = endpoint
        self.context = context
        self.zmq_context = zmq.Context()
        self.sock = self.zmq_context.socket(zmq.PUB)        
        self.sock.bind(self.endpoint)
        
    def setup(self):
        pass
    
    def process(self):    

        encoded_img = cv2.imencode('.jpg', cv2.cvtColor(self.context["FRAME"], cv2.COLOR_BGR2RGB) )[1].tobytes()
        self.sock.send(encoded_img)
    
    def shutdown(self):
        self.sock.close()