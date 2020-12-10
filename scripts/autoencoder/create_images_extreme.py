# This script creates images from the extreme IllustrisTNG simulation
import numpy as np
import sys,os,h5py
import MAS_library as MASL
sys.path.append('../analysis')
import camel_library as CL
import torch
import torchvision.utils as vutils

#################################### INPUT ##########################################
root_in      = '/mnt/ceph/users/camels'
root_out     = '/mnt/ceph/users/camels/Results/autoencoder'
sim          = 'SIMBA' #'IllustrisTNG'
snapnum      = 33
realizations = 1000

grid         = 250
splits       = 5

# parameters of the density field routine
periodic = True
x_min, y_min = 0.0, 0.0

# name of snapshot and output file
#snapshot = '%s/Sims/IllustrisTNG/extremestellar_0/snap_%03d.hdf5'%(root_in,snapnum)
#fout     = '%s/Images_T_extremestellar_0.npy'%root_out
#snapshot = '%s/Sims/IllustrisTNG/noFB_0/snap_%03d.hdf5'%(root_in,snapnum)
#fout     = '%s/Images_T_noFB_0.npy'%root_out
snapshot = '%s/Sims/IllustrisTNG/fiducial_0/snap_%03d.hdf5'%(root_in,snapnum)
fout     = '%s/Images_T_fiducial_0.npy'%root_out
#####################################################################################

# define the matrix hosting all the maps
maps_total = np.zeros((splits*3, grid, grid), dtype=np.float32)

# read the gas positions, radii and temperature of gas particles
if not(os.path.exists(snapshot)):  raise Exception('snapshot does not exists')
f = h5py.File(snapshot, 'r')
BoxSize = f['Header'].attrs[u'BoxSize']/1e3 #Mpc/h
pos     = f['PartType0/Coordinates'][:]/1e3 #Mpc/h
mass    = f['PartType0/Masses'][:]*1e10     #Msun/h
radius  = f['PartType0/SubfindHsml'][:]/1e3 #Mpc/h
#radius  = f['PartType0/SmoothingLength'][:]/1e3 #Mpc/h
#radius  = f['PartType0/AGS-Softening'][:]/1e3 #Mpc/h
f.close()
T = CL.temperature(snapshot)

# do a loop over the three different axes
count = 0
for axis in [0,1,2]:

    axis_x, axis_y = (axis+1)%3, (axis+2)%3 

    # do a loop over the different slices of each axis
    for j in range(splits):

        # get the index of the map
        count = splits*axis + j

        # find the range in the slice
        minimum, maximum = j*BoxSize/splits, (j+1)*BoxSize/splits

        # select the particles in the considered slice
        indexes = np.where((pos[:,axis]>=minimum) & (pos[:,axis]<maximum))[0] 
        pos_slice    = pos[indexes].astype(np.float32)
        radius_slice = radius[indexes]
        mass_slice   = mass[indexes]
        T_slice      = T[indexes]

        # project particle mass*temperatures into a 2D maps
        TM = np.zeros((grid,grid), dtype=np.float64)
        MASL.voronoi_RT_2D(TM, pos_slice, T_slice*mass_slice, radius_slice, 
                x_min, y_min, axis_x, axis_y, BoxSize, periodic, verbose=False)

        # project particle mass into a 2D maps
        M = np.zeros((grid,grid), dtype=np.float64)
        MASL.voronoi_RT_2D(M, pos_slice, mass_slice, radius_slice, x_min, y_min,
                           axis_x, axis_y, BoxSize, periodic, verbose=False)

        maps_total[count] = TM/M
print('%d maps'%(count+1))
print(maps_total.shape)
print('%.3e < T [K] < %.3e'%(np.min(maps_total), np.max(maps_total)))
np.save(fout, maps_total)

# save images
maps_total = np.log10(maps_total)
maps_total = torch.tensor(maps_total, dtype=torch.float32)
maps_total = maps_total.unsqueeze(1)
print(maps_total.shape)
vutils.save_image(maps_total, 'images_fiducial_0.png',
                  normalize=True, nrow=5)
