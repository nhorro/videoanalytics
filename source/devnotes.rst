Development notes
=================

Notes for development and dependency management
-----------------------------------------------

Exporting conda environment:

.. code-block:: console
    
    conda env export --name videoanalytics-gpu > videoanalytics-gpu.yml

Exporting requirements for pip package:

.. code-block:: console
    
    pip freeze > requirements.txt

Generate documentation (Sphinx)

.. code-block:: console
    
    make