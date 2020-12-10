# This script creates 2D images/fields from different fields of the simulations
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
# data parameters
root_in       = '/mnt/ceph/users/camels'
root_out      = '/mnt/ceph/users/camels/Results/images_1P'
#TREECOOL_file = '/mnt/ceph/users/camels/Software/TREECOOL'
sim           = 'SIMBA'
snapnum       = 33
realizations  = 66

# images parameters
grid         = 250
splits       = 5

# parameters of the density field routine
periodic     = True
verbose      = False
x_min, y_min = 0.0, 0.0
#####################################################################################

# find the numbers that each cpu will work with
numbers = np.where(np.arange(realizations)%nprocs==myrank)[0]

# define the matrix hosting all the maps
maps_T_loc  = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_T_tot  = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Z_loc  = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Z_tot  = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_P_loc  = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_P_tot  = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Mg_loc = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Mg_tot = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Mc_loc = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Mc_tot = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Ms_loc = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Ms_tot = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Vg_loc = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_Vg_tot = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_HI_loc = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_HI_tot = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_ne_loc = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)
maps_ne_tot = np.zeros((splits*3*realizations, grid, grid), dtype=np.float32)

# do a loop over all realizations
for i in numbers:

    if i in [16,27,38,49,60]:  index = 1505
    else:                      index = 1500+i

    if myrank==0:  print(i, end=' ', flush=True)
    
    # read the gas positions, radii and temperature of gas particles
    snapshot = '%s/Sims/%s/%d/snap_%03d.hdf5'%(root_in,sim,index,snapnum)
    if not(os.path.exists(snapshot)):  raise Exception('%s not found'%snapshot)
    f = h5py.File(snapshot, 'r')
    BoxSize = f['Header'].attrs[u'BoxSize']/1e3 #Mpc/h
    redshift = f['Header'].attrs[u'Redshift'];  
    Masses  = f['Header'].attrs[u'MassTable'][:]*1e10
    pos_g   = f['PartType0/Coordinates'][:]/1e3;  pos_g = pos_g.astype(np.float32)#Mpc/h
    pos_c   = f['PartType1/Coordinates'][:]/1e3;  pos_c = pos_c.astype(np.float32)#Mpc/h
    pos_s   = f['PartType4/Coordinates'][:]/1e3;  pos_s = pos_s.astype(np.float32)#Mpc/h
    vel_g   = f['/PartType0/Velocities'][:]/np.sqrt(1.0+redshift)
    vel_g   = np.sqrt(vel_g[:,0]**2 + vel_g[:,1]**2 + vel_g[:,2]**2)
    Mg      = f['PartType0/Masses'][:]*1e10     #Msun/h
    Ms      = f['PartType4/Masses'][:]*1e10     #Msun/h
    if sim=='IllustrisTNG':
        Mc  = np.ones(pos_c.shape[0], dtype=np.float32)*Masses[1] #Msun/h
        Rg  = f['PartType0/SubfindHsml'][:]/1e3  #Mpc/h
        Rc  = f['PartType1/SubfindHsml'][:]/1e3  #Mpc/h
        Rs  = f['PartType4/SubfindHsml'][:]/1e3  #Mpc/h
        Z   = f['/PartType0/GFM_Metallicity'][:] #metallicity
        HI  = CL.HI_mass(snapshot, TREECOOL_file)
    else:
        Mc  = f['PartType1/Masses'][:]*1e10       #Msun/h
        Rg  = f['PartType0/AGS-Softening'][:]/1e3 #Mpc/h
        Rc  = f['PartType1/AGS-Softening'][:]/1e3 #Mpc/h
        Rs  = f['PartType4/AGS-Softening'][:]/1e3 #Mpc/h
        Z   = f['/PartType0/Metallicity'][:,0] #metallicity
        HI  = f['/PartType0/NeutralHydrogenAbundance'][:]  #HI/H
    f.close()
    T  = CL.temperature(snapshot)      #K
    P  = CL.pressure(snapshot)         #Msun*(km/s)^2/kpc^3
    ne = CL.electron_density(snapshot) #1e20 electrons*h^2/Mpc^3

    # do a loop over the three different axes
    for axis in [0,1,2]:

        axis_x, axis_y = (axis+1)%3, (axis+2)%3 

        # do a loop over the different slices of each axis
        for j in range(splits):
            
            # get the number of the map; this is important for MPI
            num = i*3*splits + axis*splits + j

            # find the range in the slice
            minimum, maximum = j*BoxSize/splits, (j+1)*BoxSize/splits

            # select the particles in the considered slice
            indexes_g = np.where((pos_g[:,axis]>=minimum) & (pos_g[:,axis]<maximum))[0] 
            pos_g_    = pos_g[indexes_g]
            vel_g_    = vel_g[indexes_g]
            Rg_       = Rg[indexes_g]
            Mg_       = Mg[indexes_g]
            T_        = T[indexes_g]
            Z_        = Z[indexes_g]
            HI_       = HI[indexes_g]
            P_        = P[indexes_g]
            ne_       = ne[indexes_g]
            indexes_c = np.where((pos_c[:,axis]>=minimum) & (pos_c[:,axis]<maximum))[0] 
            pos_c_    = pos_c[indexes_c]
            Mc_       = Mc[indexes_c]
            Rc_       = Rc[indexes_c]
            indexes_s = np.where((pos_s[:,axis]>=minimum) & (pos_s[:,axis]<maximum))[0] 
            pos_s_    = pos_s[indexes_s]
            Ms_       = Ms[indexes_s]
            Rs_       = Rs[indexes_s]
            
            # project gas mass*temperatures into a 2D map
            TM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(TM, pos_g_, T_*Mg_, Rg_, x_min, y_min, 
                               axis_x, axis_y, BoxSize, periodic, verbose)
            
            # project gas mass*metallicity into a 2D map
            ZM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(ZM, pos_g_, Z_*Mg_, Rg_, x_min, y_min, 
                               axis_x, axis_y, BoxSize, periodic, verbose)
            
            # project gas velocity*mass into a 2D map
            VM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(VM, pos_g_, vel_g_*Mg_, Rg_, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose)
            
            # project gas pressure*mass into a 2D map
            PM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(PM, pos_g_, P_*Mg_, Rg_, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose)

            # project gas mass into a 2D map
            Mgas = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(Mgas, pos_g_, Mg_, Rg_, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose)

            # project cdm mass into a 2D map
            Mcdm = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(Mcdm, pos_c_, Mc_, Rc_, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose)

            # project stellar mass into a 2D map
            Mstar = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(Mstar, pos_s_, Ms_, Rs_, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose)
                
            # project HI mass into a 2D map
            HIgas = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(HIgas, pos_g_, HI_, Rg_, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose)

            # project electron density into a 2D map
            negas = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(negas, pos_g_, ne_, Rg_, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose)

            maps_T_loc[num]  = TM/Mgas
            maps_Z_loc[num]  = ZM/Mgas
            maps_P_loc[num]  = PM/Mgas
            maps_Vg_loc[num] = VM/Mgas
            maps_Mg_loc[num] = Mgas
            maps_Mc_loc[num] = Mcdm
            maps_Ms_loc[num] = Mstar
            maps_HI_loc[num] = HIgas
            maps_ne_loc[num] = negas

# join all images and save results to file
comm.Reduce(maps_T_loc,  maps_T_tot,  root=0)
comm.Reduce(maps_Z_loc,  maps_Z_tot,  root=0)
comm.Reduce(maps_P_loc,  maps_P_tot,  root=0)
comm.Reduce(maps_Vg_loc, maps_Vg_tot, root=0)
comm.Reduce(maps_Mg_loc, maps_Mg_tot, root=0)
comm.Reduce(maps_Mc_loc, maps_Mc_tot, root=0)
comm.Reduce(maps_Ms_loc, maps_Ms_tot, root=0)
comm.Reduce(maps_HI_loc, maps_HI_tot, root=0)
comm.Reduce(maps_ne_loc, maps_ne_tot, root=0)

# save files to disk
if myrank==0:
    print('')
    print('%.3e <  T [K] < %.3e'%(np.min(maps_T_tot),  np.max(maps_T_tot)))
    print('%.3e <   Z    < %.3e'%(np.min(maps_Z_tot),  np.max(maps_Z_tot)))
    print('%.3e <  Mgas  < %.3e'%(np.min(maps_Mg_tot), np.max(maps_Mg_tot)))
    print('%.3e <  Mcdm  < %.3e'%(np.min(maps_Mc_tot), np.max(maps_Mc_tot)))
    print('%.3e <  Mstar < %.3e'%(np.min(maps_Ms_tot), np.max(maps_Ms_tot)))
    print('%.3e <  Vgas  < %.3e'%(np.min(maps_Vg_tot), np.max(maps_Vg_tot)))
    print('%.3e <  M_HI  < %.3e'%(np.min(maps_HI_tot), np.max(maps_HI_tot)))
    print('%.3e <   P    < %.3e'%(np.min(maps_P_tot),  np.max(maps_P_tot)))
    print('%.3e <   n_e  < %.3e'%(np.min(maps_ne_tot), np.max(maps_ne_tot)))

    fout1 = '%s/Images_T_%s_z=%.2f.npy'%(root_out,sim,redshift)      
    fout2 = '%s/Images_Z_%s_z=%.2f.npy'%(root_out,sim,redshift)    
    fout3 = '%s/Images_Mgas_%s_z=%.2f.npy'%(root_out,sim,redshift)   
    fout4 = '%s/Images_Mcdm_%s_z=%.2f.npy'%(root_out,sim,redshift)   
    fout5 = '%s/Images_Mstar_%s_z=%.2f.npy'%(root_out,sim,redshift)  
    fout6 = '%s/Images_Vgas_%s_z=%.2f.npy'%(root_out,sim,redshift)   
    fout7 = '%s/Images_HI_%s_z=%.2f.npy'%(root_out,sim,redshift)     
    fout8 = '%s/Images_P_%s_z=%.2f.npy'%(root_out,sim,redshift)      
    fout9 = '%s/Images_ne_%s_z=%.2f.npy'%(root_out,sim,redshift)    
        
    np.save(fout1, maps_T_tot)
    np.save(fout2, maps_Z_tot)
    np.save(fout3, maps_Mg_tot)
    np.save(fout4, maps_Mc_tot)
    np.save(fout5, maps_Ms_tot)
    np.save(fout6, maps_Vg_tot)
    np.save(fout7, maps_HI_tot)
    np.save(fout8, maps_P_tot)
    np.save(fout9, maps_ne_tot)

