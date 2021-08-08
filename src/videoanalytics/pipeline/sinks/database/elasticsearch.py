# -*- coding: utf-8 -*-

"""
ElasticSearch output.
"""

import numpy as np
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

from videoanalytics.pipeline import Sink

class DetectionsESWriter(Sink):
    '''
    Writes the detections to ElasticSearch.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | DETECTIONS        | Output of an object detection model.                |
    +-------------------+-----------------------------------------------------+
    | START_FRAME       | Initial frame index.                                |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        hostname (str): ElasticSearch hostname.
    '''
    def __init__(self, name, context,es_index,hostname="localhost"):
        super().__init__(name, context)
        self.context = context
        self.frame_counter = self.context["START_FRAME"]
        self.es = es = Elasticsearch("http://{}:9200/".format(hostname))
        self.es_index=es_index
        
    def setup(self):
        pass
    
    def process(self):          
        timestamp = datetime.utcnow()
        out_boxes, out_scores, out_classes, num_boxes = self.context["DETECTIONS"]
        for i in range(num_boxes):
            x,y,w,h = out_boxes[i]            
            score = out_scores[i]
            class_idx = int(out_classes[i])   
            
            doc = {
                'frame':  self.frame_counter ,            
                'timestamp': timestamp,
                'x': x,
                'y': y,
                'w': w,
                'h': h,
                'score': score,
                'class_idx': class_idx
            }        
            res = self.es.index(self.es_index, body=doc)
        self.frame_counter+=1
        
    def shutdown(self):
        pass