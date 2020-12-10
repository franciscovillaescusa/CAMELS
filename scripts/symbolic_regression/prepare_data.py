import numpy as np
import sys,os

################################### INPUT ###########################################
root = '/mnt/ceph/users/camels/Results/neural_nets/params_2_SFRH'
root_out = '/mnt/ceph/users/camels/Results/symbolic_regression'

f_SFRH   = '%s/SFRH_IllustrisTNG.npy'%root
f_params = '%s/params_IllustrisTNG.txt'%root

training_num = 700
testing_num  = 300
#####################################################################################

# read SFRH and params
SFRH   = np.load(f_SFRH);       SFRH = np.log10(SFRH)
params = np.loadtxt(f_params)
z      = np.linspace(0, 7, 100)

##### training set #####
data = np.zeros((training_num*100,6), dtype=np.float32)

# do a loop over the different realizations
count = 0
for i in range(training_num):
    
    # do a loop over the different redshfits
    for j in range(100):
        data[count,0] = z[j]+1.0
        data[count,1] = params[i,0]
        data[count,2] = params[i,1]
        data[count,3] = params[i,2]
        data[count,4] = params[i,4]
        data[count,5] = SFRH[i,j]
        count += 1

np.savetxt('%s/training_set.txt'%root_out, data)
########################

##### testing set #####
data = np.zeros((testing_num*100,6), dtype=np.float32)

# do a loop over the different realizations
count = 0
for i in range(training_num, training_num + testing_num):
    
    # do a loop over the different redshfits
    for j in range(100):
        data[count,0] = z[j]+1.0
        data[count,1] = params[i,0]
        data[count,2] = params[i,1]
        data[count,3] = params[i,2]
        data[count,4] = params[i,4]
        data[count,5] = SFRH[i,j]
        count += 1

np.savetxt('%s/test_set.txt'%root_out, data)
########################
