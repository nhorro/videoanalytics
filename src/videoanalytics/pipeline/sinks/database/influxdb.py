# -*- coding: utf-8 -*-

"""
InfluxDB output.
"""

import numpy as np
from influxdb import InfluxDBClient
from datetime import datetime, timedelta

from videoanalytics.pipeline import Sink

def get_current_timestamp_as_str():
    return datetime.utcnow().strftime("%Y%m%d%H%M")

class InfluxDBWriter(Sink):
    '''
    Stores variables in InfluxDB time series database.

    This component **READS** the entries matching the variable names specified
    in configurations, example "VARIABLE_1", etc.:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | VARIABLE_1        | Variable updated by some component.                 |
    +-------------------+-----------------------------------------------------+
    | VARIABLE_2        | Variable updated by some component.                 |
    +-------------------+-----------------------------------------------------+
    | ...               | ...                                                 |
    +-------------------+-----------------------------------------------------+
    | VARIABLE_N        | Variable updated by some component.                 |
    +-------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        class_names_filename (str): text file with class names.
        show_label (bool): display class name in bounding box.
    '''
    def __init__(self, name, context, variables_to_publish, 
                                host='localhost', 
                                port=8086, 
                                database="my_application",
                                reset_db=False ):
        super().__init__(name, context)
        self.context = context
        self.client = InfluxDBClient(host=host, port=port, database=database)        
        self.counter = 0
        self.variables_to_publish = variables_to_publish

        if reset_db:
            self.client.drop_database(database)

        # Create database in case it does not exist
        if database not in [d[0]['name'] for d in self.client.query("show databases;")]:
            self.client.create_database(database)
        
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
                        #"time":  now_str,
                        "fields": {
                            "value": self.context[v],
                            "index": self.counter
                        }
                    }
                )           

        self.client.write_points(json_body, time_precision='ms')
        self.counter+=1
    
    def shutdown(self):
        self.client.close()


class DetectionsCounter(Sink):
    '''
    Counts the detections for each class in a frame and prepares a variable.

    This component **READS** the following entries in the global context:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | DETECTIONS        | Output of an object detection model.                |
    +-------------------+-----------------------------------------------------+
    | START_FRAME       | Initial frame index.                                |
    +-------------------+-----------------------------------------------------+

    This component **WRITES** the entries in the global context:

    +---------------------------+-----------------------------------------------------+
    | Variable name             | Description                                         |
    +===========================+============+==========+=============================+
    | <PREFIX>_IDX_<POSTFIX>     | Number of instances of class IDX in frame          |
    +---------------------------+-----------------------------------------------------+

    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        classes_to_count (list): List of classes to count (other classes will be ignored)
        prefix (str): prefix for variable names.
        postfix (str): prefix for variable names.
    '''
    def __init__(self, name, context,classes_to_count,prefix="OBJ",postfix="_COUNT"):
        super().__init__(name, context)
        self.context = context
        self.classes_to_count = classes_to_count
        self.prefix=prefix
        self.postfix=postfix
        
    def setup(self):
        pass
    
    def process(self):    
        for c in self.classes_to_count:
            varname="{}{:02d}{}".format(self.prefix,c,self.postfix)
            self.context[varname]=0
        
        out_boxes, out_scores, out_classes, num_boxes = self.context["DETECTIONS"]
        for i in range(num_boxes):
            #x,y,w,h = out_boxes[i]            
            score = out_scores[i]
            class_idx = int(out_classes[i])   
            varname="{}{:02d}{}".format(self.prefix,class_idx,self.postfix)
            self.context[varname]+=1
    
    def shutdown(self):
        pass


def plot_timeseries(influxdbclient,variable_list,ax, index_mode="time",timerange="now()-1d"):
    """ 
    Helper function to plots the evolution of series from InfluxDB.    
    
    Args:        
        influxdbclient: InfluxDB client (1.7)
        variable_list: list of variables to plot
        ax: matplotlib axes.
        index_mode: "time" for timestamp or "index" for frame index
        timerange: time range in InfluxDB format (see InfluxQL reference).
        
    Returns:
        matplotlib axes
    """
    assert(index_mode in ["time","index"])

    ax.grid(which="Both")
    for varname in variable_list:
        rs = influxdbclient.query("select value,index from {} WHERE time >= {}".format(varname,timerange))        
        ts = np.array([x[index_mode] for x in rs[varname]])
        value = np.array([x["value"] for x in rs[varname]],dtype=np.int)
        ax.scatter(ts,value);
    ax.legend(variable_list);
    ax.set_ylabel("Count")
    ax.set_xlabel("Frame index" if index_mode=="index" else "Timestamp")
    return ax