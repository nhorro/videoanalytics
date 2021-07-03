# videoanalytics

![PyPI](https://img.shields.io/pypi/v/videoanalytics)

Python library for fast prototyping [video content analysis](https://en.wikipedia.org/wiki/Video_content_analysis) applications. Relies on OpenCV, Keras, and other standard computer vision and machine learning python packages.

## Functionality and available components

Typical functional blocks of a video analytics application are described in [2]. 

- **Dynamic masking**:	Blocking a part of the video signal based on the signal itself, for example because of privacy concerns.
- **Egomotion estimation**:	Egomotion estimation is used to determine the location of a camera by analyzing its output signal.
- **Motion detection**:	Motion detection is used to determine the presence of relevant motion in the observed scene.
- **Shape recognition**:	Shape recognition is used to recognize shapes in the input video, for example circles or squares. This functionality is typically used in more advanced functionalities such as object detection.
- **Object detection**:	Object detection is used to determine the presence of a type of object or entity, for example a person or car. Other examples include fire and smoke detection.
- **Recognition**:	Face recognition and Automatic Number Plate Recognition are used to recognize, and therefore possibly identify, persons or cars.
- **Style detection**: Style detection is used in settings where the video signal has been produced, for example for television broadcast. Style detection detects the style of the production process.[9]
- **Tamper detection**: Tamper detection is used to determine whether the camera or output signal is tampered with.
- **Video tracking**: Video tracking is used to determine the location of persons or objects in the video signal, possibly with regard to an external reference grid.
- **Video error level analysis**: Video scene content tamper analysis using free software. Video Error level analysis (VELA)
- **Object co-segmentation**: Joint object discovery, classification and segmentation of targets in one or multiple related video sequences

This library provides components for each specific task organized as sources and sinks which are instanced and connected at execution time as [pipelines](https://homepages.fhv.at/thjo/lecturenotes/sysarch/pipes-and-filters.html).
Sources consume data from a camera or file and trigger the processing pipeline.
Sinks process data that was made available from other components and generate new data or perform an action such as storing in a DB.

Some components present in the current version of the library:

- Sources
    - VideoReader
- Sinks
    - Object detection
        - YOLOv4Detector
        - DetectorCSV
    - Tracking
        - SORT
        - DeepSORT
    - Visualization
        - Bounding box annotation
        - Matplotlib
    - Working with ROIs (Regions of interest)
    - Output
        - Metadata
            - DetectionsCSVWriter
                - Store object detections as CSV.
            - TrackingCSVWriter
                - Store tracked objects as CSV.
        - Database
            - InfluxDB. 
            - ELasticSearch
        - Video
            - Write frames to video file.

## Instructions for developers

A GPU conda environment is provided for development.

Import conda environment (GPU):

~~~bash
conda env create -f videoanalytics-gpu.yml
~~~

Some examples are provided as jupyter notebooks.

~~~bash
conda activate videoanalytics-gpu.yml
jupyter notebook .
~~~

## References

1. [Wikipedia article for video content analyis] (https://en.wikipedia.org/wiki/Video_content_analysis)
2. Code for YOLOv4 and DeepSORT was adapted from [yolov4-deepsort](https://github.com/theAIGuysCode/yolov4-deepsort).
3. [EDN Introduction to video analytics](https://www.edn.com/introduction-to-video-analytics/)
