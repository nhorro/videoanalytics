.. videoanalytics documentation master file, created by
   sphinx-quickstart on Mon Jun 21 10:23:22 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation for videoanalytics
================================

This project's documentation is organized in two parts. The first part comprises and :doc:`intro` 
section that describes the scope of the library follwed by a description of the pipeline paradigm 
and its building blocks and methods, in which this library relies. They are described in :doc:`pipeline` section. 
Some basic sources and sinks are detailed in :doc:`sources` and :doc:`sinks` sections respectively.
Specific blocks that might require a more detailed discussion are treated in special sections. This is the case of 
:doc:`object_detection` and :doc:`object_tracking`.

.. toctree::
   :maxdepth: 4
   :caption: Contents

   intro   
   pipeline
   sources
   sinks
   object_detection
   object_tracking
   roi
   background
   database
   zeromq
   utils
   Basic pipeline.ipynb
   Image transformations.ipynb
   Object detection.ipynb   
   Object tracking.ipynb   
   Integration with databases.ipynb
   Events and statistics from ROIs.ipynb
   references   

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
