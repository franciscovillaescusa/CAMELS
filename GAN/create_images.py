from mpi4py import MPI
import numpy as np
import sys,os,h5py
import MAS_library as MASL
sys.path.append('../analysis')
import camel_library as CL

###### MPI DEFINITIONS ###### 
comm   = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

#################################### INPUT ##########################################
root_in      = '/mnt/ceph/users/camels'
root_out     = '/mnt/ceph/users/camels/Results/GAN'
sim          = 'SIMBA' #'IllustrisTNG'
snapnum      = 33
realizations = 1000

grid         = 250
splits       = 5

# parameters of the density field routine
periodic = True
x_min, y_min = 0.0, 0.0
#####################################################################################

# define the matrix hosting all the maps
maps_local = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_total = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)

# find the numbers that each cpu will work with
numbers = np.where(np.arange(realizations)%nprocs==myrank)[0]

# do a loop over all realizations
for i in numbers:

    # read the gas positions, radii and temperature of gas particles
    snapshot = '%s/Sims/%s/%d/snap_%03d.hdf5'%(root_in,sim,i,snapnum)
    if not(os.path.exists(snapshot)):  
        count += 3*splits
        continue
    f = h5py.File(snapshot, 'r')
    BoxSize = f['Header'].attrs[u'BoxSize']/1e3 #Mpc/h
    pos     = f['PartType0/Coordinates'][:]/1e3 #Mpc/h
    mass    = f['PartType0/Masses'][:]*1e10     #Msun/h
    if sim=='IllustrisTNG':
        radius  = f['PartType0/SubfindHsml'][:]/1e3 #Mpc/h
    else:
        #radius  = f['PartType0/SmoothingLength'][:]/1e3 #Mpc/h
        radius  = f['PartType0/AGS-Softening'][:]/1e3 #Mpc/h
    f.close()
    T = CL.temperature(snapshot)

    # do a loop over the three different axes
    for axis in [0,1,2]:

        axis_x, axis_y = (axis+1)%3, (axis+2)%3 

        # do a loop over the different slices of each axis
        for j in range(splits):

            # get the index of the map
            count = splits*3*i + splits*axis + j

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

            maps_local[count] = TM/M
    print('Realization %d : %d maps'%(i, count+1))

# join all images and save results to file
comm.Reduce(maps_local, maps_total, root=0)

if myrank==0:
    if sim=='SIMBA':  
        start,end = 714*15, 715*15
        numbers = np.arange(start,end)
        maps_total = np.delete(maps_total, numbers, axis=0)
    print(maps_total.shape)
    print('%.3e < T [K] < %.3e'%(np.min(maps_total), np.max(maps_total)))
    np.save('%s/Images_T_%s.npy'%(root_out,sim), maps_total)
