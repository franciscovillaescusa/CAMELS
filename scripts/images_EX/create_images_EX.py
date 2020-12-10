# This script creates images from the extreme IllustrisTNG simulation
import numpy as np
import sys,os,h5py
import MAS_library as MASL
sys.path.append('../analysis')
import camel_library as CL
import torch
import torchvision.utils as vutils

#################################### INPUT ##########################################
root_in       = '/mnt/ceph/users/camels'
root_out      = '/mnt/ceph/users/camels/Results/images_EX'
sim           = 'IllustrisTNG' #'IllustrisTNG'
snapnum       = 33
realizations  = 1000
TREECOOL_file = '/mnt/ceph/users/camels/Software/TREECOOL'

grid         = 250
splits       = 5

# parameters of the density field routine
periodic = True
x_min, y_min = 0.0, 0.0

# name of snapshot and output file
snapshots = ['%s/Sims/IllustrisTNG/fiducial_0/snap_%03d.hdf5'%(root_in, snapnum),
             '%s/Sims/IllustrisTNG/extreme_0/snap_%03d.hdf5'%(root_in,snapnum),
             '%s/Sims/IllustrisTNG/extremestellar_0/snap_%03d.hdf5'%(root_in,snapnum),
             '%s/Sims/IllustrisTNG/noFB_0/snap_%03d.hdf5'%(root_in,snapnum)]

fouts = ['%s/Images_EX_fiducial'%root_out,
         '%s/Images_EX_AGN'%root_out,
         '%s/Images_EX_SN'%root_out,
         '%s/Images_EX_noFB'%root_out] 
#####################################################################################

# do a loop over the different simulations
for snapshot,fout in zip(snapshots, fouts):

    # read the gas positions, radii and temperature of gas particles
    if not(os.path.exists(snapshot)):  raise Exception('snapshot does not exists')
    f = h5py.File(snapshot, 'r')
    BoxSize = f['Header'].attrs[u'BoxSize']/1e3  #Mpc/h
    redshift = f['Header'].attrs[u'Redshift'];  scale_factor = 1.0/(1.0+redshift)
    Masses  = f['Header'].attrs[u'MassTable'][:]*1e10
    pos_g   = f['PartType0/Coordinates'][:]/1e3  #Mpc/h
    pos_c   = f['PartType1/Coordinates'][:]/1e3  #Mpc/h
    pos_s   = f['PartType4/Coordinates'][:]/1e3  #Mpc/h
    vel_g   = f['/PartType0/Velocities'][:]/np.sqrt(1.0+redshift)
    vel_g   = np.sqrt(vel_g[:,0]**2 + vel_g[:,1]**2 + vel_g[:,2]**2)
    Mg      = f['PartType0/Masses'][:]*1e10      #Msun/h
    Mc      = np.ones(pos_c.shape[0], dtype=np.float32)*Masses[1] #Msun/h
    Ms      = f['PartType4/Masses'][:]*1e10      #Msun/h
    Rg      = f['PartType0/SubfindHsml'][:]/1e3  #Mpc/h
    Rc      = f['PartType1/SubfindHsml'][:]/1e3  #Mpc/h
    Rs      = f['PartType4/SubfindHsml'][:]/1e3  #Mpc/h
    Z       = f['/PartType0/GFM_Metallicity'][:] #metallicity
    f.close()
    HI = CL.HI_mass(snapshot, TREECOOL_file)
    T  = CL.temperature(snapshot)
    P  = CL.pressure(snapshot)         #Msun*(km/s)^2/kpc^3
    ne = CL.electron_density(snapshot) #1e20 electrons*h^2/Mpc^3

    # define the matrix hosting all the maps
    maps_T  = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_Z  = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_Mg = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_Mc = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_Ms = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_Vg = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_HI = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_P  = np.zeros((splits*3, grid, grid), dtype=np.float32)
    maps_ne = np.zeros((splits*3, grid, grid), dtype=np.float32)

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
            indexes_g = np.where((pos_g[:,axis]>=minimum) & (pos_g[:,axis]<maximum))[0] 
            indexes_c = np.where((pos_c[:,axis]>=minimum) & (pos_c[:,axis]<maximum))[0] 
            indexes_s = np.where((pos_s[:,axis]>=minimum) & (pos_s[:,axis]<maximum))[0] 
            pos_g_slice = pos_g[indexes_g].astype(np.float32)
            pos_c_slice = pos_c[indexes_c].astype(np.float32)
            pos_s_slice = pos_s[indexes_s].astype(np.float32)
            Rg_slice    = Rg[indexes_g]
            Rc_slice    = Rc[indexes_c]
            Rs_slice    = Rs[indexes_s]
            Mg_slice    = Mg[indexes_g]
            Mc_slice    = Mc[indexes_c]
            Ms_slice    = Ms[indexes_s]
            Vg_slice    = vel_g[indexes_g]
            T_slice     = T[indexes_g]
            Z_slice     = Z[indexes_g]
            HI_slice    = HI[indexes_g]
            P_slice     = P[indexes_g]
            ne_slice    = ne[indexes_g]

            # project particle mass*temperatures into a 2D maps
            TM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(TM, pos_g_slice, T_slice*Mg_slice, Rg_slice, 
                    x_min, y_min, axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project particle mass*metallicity into a 2D maps
            ZM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(ZM, pos_g_slice, Z_slice*Mg_slice, Rg_slice, 
                        x_min, y_min, axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project particle pressure*mass into a 2D maps
            PM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(PM, pos_g_slice, P_slice*Mg_slice, Rg_slice, 
                    x_min, y_min, axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project particle velocity*mass into a 2D maps
            VM = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(VM, pos_g_slice, Vg_slice*Mg_slice, Rg_slice, 
                               x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project gas particle mass into a 2D maps
            Mgas = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(Mgas, pos_g_slice, Mg_slice, Rg_slice, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project dm particle mass into a 2D maps
            Mcdm = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(Mcdm, pos_c_slice, Mc_slice, Rc_slice, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project star particle mass into a 2D maps
            Mstar = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(Mstar, pos_s_slice, Ms_slice, Rs_slice, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project gas particle HI into a 2D maps
            HIgas = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(HIgas, pos_g_slice, HI_slice, Rg_slice, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose=False)

            # project electron density into a 2D maps
            negas = np.zeros((grid,grid), dtype=np.float64)
            MASL.voronoi_RT_2D(negas, pos_g_slice, ne_slice, Rg_slice, x_min, y_min,
                               axis_x, axis_y, BoxSize, periodic, verbose=False)

            maps_T[count]  = TM/Mgas
            maps_Z[count]  = ZM/Mgas
            maps_Vg[count] = VM/Mgas
            maps_P[count]  = PM/Mgas
            maps_Mg[count] = Mgas
            maps_Mc[count] = Mcdm
            maps_Ms[count] = Mstar
            maps_HI[count] = HIgas
            maps_ne[count] = negas
            count += 1

    print('%d maps'%count)
    print('%.3e < T [K]  < %.3e'%(np.min(maps_T),  np.max(maps_T)))
    print('%.3e <   Z    < %.3e'%(np.min(maps_Z),  np.max(maps_Z)))
    print('%.3e <  Mgas  < %.3e'%(np.min(maps_Mg), np.max(maps_Mg)))
    print('%.3e <  Mcdm  < %.3e'%(np.min(maps_Mc), np.max(maps_Mc)))
    print('%.3e <  Mstar < %.3e'%(np.min(maps_Ms), np.max(maps_Ms)))
    print('%.3e <  Vgas  < %.3e'%(np.min(maps_Vg), np.max(maps_Vg)))
    print('%.3e <   HI   < %.3e'%(np.min(maps_HI), np.max(maps_HI)))
    print('%.3e <   n_e  < %.3e'%(np.min(maps_ne), np.max(maps_ne)))
    print('%.3e <   P    < %.3e'%(np.min(maps_P),  np.max(maps_P)))

    fout1 = '%s_T.npy'%fout;      np.save(fout1, maps_T)
    fout2 = '%s_Z.npy'%fout;      np.save(fout2, maps_Z)
    fout3 = '%s_Mgas.npy'%fout;   np.save(fout3, maps_Mg)
    fout4 = '%s_Mstar.npy'%fout;  np.save(fout4, maps_Ms)
    fout5 = '%s_Vgas.npy'%fout;   np.save(fout5, maps_Vg)
    fout6 = '%s_HI.npy'%fout;     np.save(fout6, maps_HI)
    fout7 = '%s_Mcdm.npy'%fout;   np.save(fout7, maps_Mc)
    fout8 = '%s_ne.npy'%fout;     np.save(fout8, maps_ne)
    fout9 = '%s_P.npy'%fout;      np.save(fout9, maps_P)
    

    # save images
    #maps_total = np.log10(maps_total)
    #maps_total = torch.tensor(maps_total, dtype=torch.float32)
    #maps_total = maps_total.unsqueeze(1)
    #print(maps_total.shape)
    #vutils.save_image(maps_total, 'images_fiducial_0.png',
    #                  normalize=True, nrow=5)
