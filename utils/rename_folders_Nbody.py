# This script renames the name of the N-body simulation folders
import numpy as np
import sys,os

################################## INPUT ##############################################
root       = '/mnt/ceph/users/camels/Sims'
simulation = 'IllustrisTNG_DM' #'SIMBA_DM'
#######################################################################################


# LH set
for i in range(1000):
    folder_in  = '%s/%s/%s'%(root,simulation,i)
    folder_out = '%s/%s/LH_%d'%(root,simulation,i)

    if os.path.exists(folder_in):
        os.system('mv %s %s'%(folder_in, folder_out))


# CV set
for i in range(27):
    folder_in  = '%s/%s/1505_%s'%(root,simulation,i)
    folder_out = '%s/%s/CV_%d'%(root,simulation,i)

    if os.path.exists(folder_in):
        os.system('mv %s %s'%(folder_in, folder_out))


# 1P set
for i in range(66):
    folder_in  = '%s/%s/%s'%(root,simulation,1500+i)
    folder_out = '%s/%s/1P_%d'%(root,simulation,i)

    if os.path.exists(folder_in):
        os.system('mv %s %s'%(folder_in, folder_out))


# EX set
folder_in  = '%s/%s/1505_EX'%(root,simulation)
folder_out = '%s/%s/EX_0'%(root, simulation)
if os.path.exists(folder_in):
    os.system('mv %s %s'%(folder_in, folder_out))

