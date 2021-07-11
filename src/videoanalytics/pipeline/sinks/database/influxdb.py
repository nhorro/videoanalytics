# -*- coding: utf-8 -*-

"""
InfluxDB output.
"""

import numpy as np
import cv2
from influxdb import InfluxDBClient
from datetime import datetime, timedelta

from videoanalytics.pipeline import Sink


def get_current_timestamp_as_str():
    return datetime.utcnow().strftime("%Y%m%d%H%M")

class InfluxDBWriter(Sink):
    def __init__(self, context, variables_to_publish, host='localhost', port=8086, database="my_application" ):
        super().__init__(context)        
        self.context = context
        self.client = InfluxDBClient(host=host, port=port, database=database)        
        self.counter = 0
        self.variables_to_publish = variables_to_publish

    def setup(self):
        pass
    
    def process(self):    
        json_body = []
        now_str = get_current_timestamp_as_str()        
        for v in self.variables_to_publish:
            if v in self.context:
                json_body.append(
                    {
                        "measurement": v,
                        "time":  now_str,
                        "fields": {
                            "value": self.context[v]
                        }
                    }
                )        
            
        self.client.write_points(json_body)
    
    def shutdown(self):
        self.client.close()
