# This script renames the name of the simulation folders
import numpy as np
import sys,os

################################## INPUT ##############################################
root       = '/mnt/ceph/users/camels/Sims'
simulation = 'SIMBA' #'IllustrisTNG'
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
folders_in  = ['%s/%s/fiducial_0'%(root,simulation),
               '%s/%s/extreme_0'%(root,simulation),
               '%s/%s/extremestellar_0'%(root,simulation),
               '%s/%s/noFB_0'%(root,simulation)]
               
folders_out = ['%s/%s/EX_0'%(root, simulation),
               '%s/%s/EX_1'%(root, simulation),
               '%s/%s/EX_2'%(root, simulation),
               '%s/%s/EX_3'%(root, simulation)]

for folder_in, folder_out in zip(folders_in, folders_out):
    if os.path.exists(folder_in):
        os.system('mv %s %s'%(folder_in, folder_out))

