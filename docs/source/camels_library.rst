.. _CAMELS_library:

**************
CAMELS_library
**************

The CAMELS library is a set python routines written to simplify the analysis of CAMELS data.

Installation
------------

.. code-block:: bash

   git clone https://github.com/franciscovillaescusa/CAMELS.git
   cd CAMELS/library
   python setup.py install

If you want to have more control on where the libraries are install we recommend instead:

.. code-block:: bash

   git clone https://github.com/franciscovillaescusa/CAMELS.git
   cd CAMELS/library
   python setup.py build

This will create a folder called build inside CAMELS/library. Inside build/ there will be a folder that start with lib. Just put the path to that folder in your PYTHONPATH and the libraries will be installed. E.g.:

.. code-block::  bash
		 
   export PYTHONPATH=$PYTHONPATH//Users/fvillaescusa/Desktop/CAMELS/library/build/lib
