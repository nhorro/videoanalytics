Object detection
================

This sections describes the components used for object detection. 

Object detection components that are independent of the implementation are
separated from specific models.
Examples of the first category include visual annotators, components to save detections
to CSV format, or to load precalculated detections.
Examples of specific implementation are a tensorflow, OpenCV or other deep learning framework 
port of the Darknet YOLOv4 model or any of its variants. 
The consumption or object detection as a service through gRPC or other protocol is also an
implementation alternative, that could reduce the dependencies for videoanalytics library.


API reference
-------------

.. automodule:: videoanalytics.pipeline.sinks.obj_detector
   :members:

.. automodule:: videoanalytics.pipeline.sinks.yolo4_detector
   :members:   