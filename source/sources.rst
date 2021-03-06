Sources
=======

Sources abstract the details of implementation of different signal acquisition methods.
The obtained signal is fragmented into a sequence of a meaningful units of information.
Currently, only video frames are supported but the concept could be extended to audio signal 
buffers or other signal types.

Design guidelines for sources
-----------------------------

Sources should contemplate a method of guaranteeing an output rate that the processing pipeline
can cope with, being the most naive implementation providing an attribute to drop frames or
reduce frame quality.

API reference
-------------

.. automodule:: videoanalytics.pipeline.sources
   :members: