Sinks
=====

Sinks abstract the concept of receiving data to produce new data or perform a specifc action
such as publishing or storing it in a database.

Design guidelines for sinks
---------------------------

It is recommeded that sinks perform a single specific task and complex actions are achieved
by interaction of several sinks specified at configuration time rather than a monolithic approach.

API reference
-------------

.. automodule:: videoanalytics.pipeline.sinks
   :members: