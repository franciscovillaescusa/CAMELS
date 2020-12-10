.. _CAMELS_library:

**************
CAMELS library
**************

The CAMELS library is a set python routines written to simplify the analysis of CAMELS data.

Requirements
------------

The CAMELS library has some basic dependences:

- numpy
- scipy
- h5py
- `Pylians3 <https://github.com/franciscovillaescusa/Pylians3>`_ 
  

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

Distance to k nearest neighbors
-------------------------------

The routine ``KDTree_distance`` can be used to compute the distance to the k nearest neighbors of a set of particles. Note that the neighbors can be a different type of particle as the one considered. For instance, it can be used to compute the distance to the k nearest gas particles from the positions of star particles. The ingredients needed for this routine are:

- ``pos1``. The positions of the particles over which compute its nearest neighbors. In the above example, these would be the positions of the stars.

- ``pos2``. The positions of the particles over which compute the distances. In the above example, these would be the positions of the gas particles. Note that ``pos2`` can be the same as ``pos1``: e.g. to compute the distance to the k nearest neighborgs from a set of dark matter particles.

- ``k``. The number of neighbors to consider.

- ``BoxSize``. To account for periodic boundary conditions, set this number to the size of the simulation box. Note that this number may need to be just slightly larger than that to avoid problems with particles in the edge. E.g. set it to ``BoxSize*(1.0+1e-8)``.

- ``threads``. Number of openmp threads to use in the calculation. Set to ``-1`` to use all the available threads.

- ``verbose``. Whether to print some information on the progress.
  
An example of how to use this routine is this

.. code-block:: python

   import numpy as np
   import camels_library as CL
   import h5py

   ################## INPUT ##################
   # snapshot name
   snapshot = '/mnt/ceph/users/camels/Sims/IllustrisTNG/LH_0/snap_033.hdf5'

   # KDTree parameters
   k       = 32    #number of neighbors
   threads = -1    #number of openmp threads
   verbose = True  #whether print some information on calculation progress
   ###########################################
   
   # read positions of gas and star particles
   f         = h5py.File(snapshot, 'r')
   BoxSize   = f['Header'].attrs[u'BoxSize']/1e3  #Mpc/h
   pos_gas   = f['PartType0/Coordinates'][:]/1e3  #Mpc/h
   pos_stars = f['PartType4/Coordinates'][:]/1e3  #Mpc/h
   f.close()

   # compute distance of each star particle to its k nearest gas particle
   # d is a 1D numpy array with the distance of each star particle to its
   # k nearest neighborghs
   d = CL.KDTree_distance(pos_stars, pos_gas, k, BoxSize*(1.0+1e-8), threads, verbose) #Mpc/h
   

   
   


