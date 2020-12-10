import numpy as np
import sys,os,glob


##################################### INPUT ##########################################
root = '/mnt/ceph/users/camels/Results/autoencoder/losses'
######################################################################################

files = glob.glob('%s/*'%root)

# read all files and print the minimum loss
for f in files:
    epoch, train_loss, valid_loss = np.loadtxt(f, unpack=True)
    index = np.where(valid_loss==np.min(valid_loss))[0]
    print('%s\n%.3e\n'%(f,valid_loss[index[0]]))
