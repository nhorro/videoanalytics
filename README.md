# videoanalytics

Python library for prototyping of video analytic applications. Relies on OpenCV, Keras, and other standard computer vision and machine learning python packages.

References:
- Code for YOLOv4 and DeepSORT was adapted from [yolov4-deepsort](https://github.com/theAIGuysCode/yolov4-deepsort).

## Instructions for developers

Import conda environment (GPU):

~~~bash
conda env create -f videoanalytics-gpu.yml
~~~

Some examples are provided as jupyter notebooks.

~~~bash
conda activate videoanalytics-gpu.yml
jupyter notebook .
~~~

## Component reference

Components are organized as Sources and sinks which are instanced and connected at execution time as pipelines.
Sources consume data from a camera or file and trigger the processing pipeline.
Sinks process data that was made available from other components and generate new.

- Sources
    - VideoReader
- Sinks
    - Object detection
        - YOLOv4Detector
        - DetectorCSV
    - Visualization
        - Bounding box annotation
        - Matplotlib
    - Outputs
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

## Notes for development and dependency management

Exporting conda environment:

~~~bash
conda env export --name videoanalytics-gpu > videoanalytics-gpu.yml
~~~

Exporting requirements for pip package:

~~~bash
pip freeze > requirements.txt
~~~

Generate documentation (Sphinx)

~~~bash
make
~~~