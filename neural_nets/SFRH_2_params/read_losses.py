import numpy as np
import sys,os,glob


##################################### INPUT ##########################################
root = '/mnt/ceph/users/camels/Results/neural_nets/SFRH_2_params/losses'
######################################################################################

files = glob.glob('%s/*'%root)

# read all files and print the minimum loss
for f in files:
    data = np.loadtxt(f, unpack=False)
    valid_loss = data[:,2]
    index = np.where(valid_loss==np.min(valid_loss))[-1]
    print('%s\n%.3e\n'%(f,valid_loss[index[0]]))
