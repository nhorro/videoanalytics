Working with ROIs
=================

Regions of interest (ROIs) are polygonal areas which can be tested for the presence of objects or other events
such as:

- If an object enters or leaves a region.
- The time an object stays inside a region.
- The number of objects in a region.
- The amount of movement or activity inside a region.
- Etc.


Combined with the information from an object detector, an object tracker, or motion estimation,
ROIs can provide useful insights of what is happening in a scene.

As an example :numref:`fig-mirtar-rois` shows how regions are applied to a scene with a fixed camera
to associate the presence of human operators or pixel activity in each region to different tasks being 
performed.

.. _fig-mirtar-rois:

.. figure:: _static/mirtar-rois.png
    :figclass: align-center

    Regions in the deck of a ship for classification of on board tasks in video footage.

API reference
-------------

JSON format for definition of polygonal regions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: json

   {
      "regions": [
         {
            "name": "tangon_babor_sup",
            "polygon": [[385, 315], [676, 334], [754, 625], [668, 810], [165, 757]],
            "color": [155,155,0]
         },

         {
            "name": "tangon_babor_inf",
            "polygon": [[11, 532], [777, 606], [666, 1073], [5, 1074]],
            "color": [155,155,0]
         },
      
         {
            "name": "tangon_estribor_sup",
            "polygon": [[1057, 336], [908, 682], [954, 773], [1522, 754], [1565, 595], [1210, 305]],
            "color": [155,0,155]
         },
      
         {
            "name": "tangon_estribor_inf",
            "polygon": [[973, 1072], [949, 625], [1749, 538], [1904, 1068]],
            "color": [155,0,155]
         },

         {
            "name": "puente",
            "polygon": [[1088, 369], [592, 382], [570, 580], [1131, 584]],
            "color": [0,255,0]
         }
      ]		
   }



.. automodule:: videoanalytics.pipeline.sinks.roi
   :members: