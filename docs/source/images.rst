******
Images
******

There are two different ways to create images from the simulations:

Column density
--------------

The first option is to create images by computing the column density along the center of each pixel. The next script computes the 

.. code-block::  python

   import numpy as np
   import MAS_library as MASL
   import camels_library as CL
   import h5py

   ##################################### INPUT ######################################
   # input and output files
   snapshot = '/mnt/ceph/users/camels/Sims/IllustrisTNG/LH_0/snap_033.hdf5'
   f_out    = 'gas_temperature.npy'

   # region over which make the image (should be squared)
   x_min, x_max = 0.0, 5.0 #Mpc/h
   y_min, y_max = 0.0, 5.0 #Mpc/h
   z_min, z_max = 0.0, 5.0 #Mpc/h 
   grid         = 250      #image will have grid x grid pixels
   
   # parameters to compute column density
   periodic = False  #whether treat image as periodic in the considered plane
   plane    = 'XY' #'XY', 'YZ', 'XZ'
   verbose  = False

   # KDTree parameters
   k       = 32 #number of neighborghs
   threads = -1
   ##################################################################################
   
   # read gas position and masses
   f        = h5py.File(snapshot, 'r')
   BoxSize  = f['Header'].attrs[u'BoxSize']/1e3  #Mpc/h
   redshift = f['Header'].attrs[u'Redshift']
   pos_g    = f['PartType0/Coordinates'][:]/1e3  #Mpc/h
   pos_g    = pos_g.astype(np.float32)           #positions as float32
   Mg       = f['PartType0/Masses'][:]*1e10      #Msun/h
   f.close()
   T        = CL.temperature(snapshot)           #K
   Rg       = KDTree_distance(pos_g, pos_g, k, BoxSize*(1.0+1e-8), threads, verbose=False) #Mpc/h

   # select the particles in the considered region
   indexes = np.where((pos_g[:,0]>x_min) & (pos_g[:,0]<x_max) &
		      (pos_g[:,1]>y_min) & (pos_g[:,1]<y_max) &
                      (pos_g[:,2]>z_min) & (pos_g[:,2]<z_max))[0]
   pos_g_ = pos_g[indexes]
   T_     = T[indexes]
   Mg_    = Mg[indexes]
   Rg_    = Rg[indexes]

   if   plane=='XY':  axis_x, axis_y, width = 0, 1, x_max-x_min
   elif plane=='YZ':  axis_x, axis_y, width = 1, 2, y_max-y_min
   elif plane=='XZ':  axis_x, axis_y, width = 0, 2, z_max-z_min

   # project gas mass*temperatures into a 2D map
   TM = np.zeros((grid,grid), dtype=np.float64)
   MASL.voronoi_RT_2D(TM, pos_g_, T_*Mg_, Rg_, x_min, y_min, 
		      axis_x, axis_y, width, periodic, verbose)

   # project gas mass into a 2D map
   M = np.zeros((grid,grid), dtype=np.float64)
   MASL.voronoi_RT_2D(M, pos_g_, Mg_, Rg_, x_min, y_min,
		      axis_x, axis_y, width, periodic, verbose)

   # compute mean temperature 
   T = TM/M
   print('%.3e < T < %.3e'%(np.min(T), np.max(T)))

   # save results to file
   np.save(f_out, T)


3D fields slices
----------------
