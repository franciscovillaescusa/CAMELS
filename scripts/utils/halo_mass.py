import numpy as np
import sys,os,h5py

root        = '/simons/scratch/sgenel/OUTPUT_RUNS/CosmologicalBoxes/Hydro_DL/'
realization = 1505
snapnum     = 33


fin = '%s/%d/fof_subhalo_tab_%03d.hdf5'%(root,realization,snapnum)

f = h5py.File(fin, 'r')
mass = f['Group/GroupMass'][:]*1e10 #Msun/h
f.close()

print('%.3e < Mass < %.3e'%(np.min(mass), np.max(mass)))
