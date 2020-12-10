import numpy as np
import sys,os

def compute_errors(x_train, y_train, x_test, y_test):
    y_pred = function(x_train)
    error_train  = np.sqrt(np.mean((y_pred - y_train)**2/y_train**2))
    error_train2 = np.sqrt(np.mean((y_pred - y_train)**2))

    y_pred = function(x_test)
    error_test  = np.sqrt(np.mean((y_pred - y_test)**2/y_test**2))
    error_test2 = np.sqrt(np.mean((y_pred - y_test)**2))
    
    return error_train, error_train2, error_test, error_test2

"""
def function(params): #errors1.txt
    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
    A = Om*0.637**(A3 - np.cos(A1) + np.cos((z+1)*(Om-1)))
    B = np.sin(s8)**((z+1+A1)*np.exp(-np.tan(np.tan(np.tan(Om)))))
    C = np.zeros((A.shape[0],2), dtype=np.float64)
    C[:,0] = A;  C[:,1] = B
    return np.log(np.amin(C,axis=1))
"""

"""
def function(params): #errors2.txt
    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
    A = np.zeros((z.shape[0],2), dtype=np.float32)
    B = np.zeros((z.shape[0],2), dtype=np.float32)
    A[:,0] = (1+z) - 1.75593240370718*np.exp(s8);  A[:,1] = np.log(A3)
    B[:,0] = np.tan(s8);                           B[:,1] = 0.105*(1+z)/Om
    return -A1**0.393 + (0.726*s8)**np.amax(A,axis=1) + \
        np.log(np.amin(B,axis=1)*np.sin(Om))
"""

"""
def function(params): #errors3.txt
    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
    A = np.zeros((z.shape[0],2), dtype=np.float32)
    B = np.zeros((z.shape[0],2), dtype=np.float32)
    C = np.zeros((z.shape[0],2), dtype=np.float32)
    A[:,0] = A3;                     A[:,1] = s8
    B[:,0] = Om**np.amin(A,axis=1);  B[:,1] = Om**(0.212*(1+z-s8))
    C[:,0] = np.amin(B,axis=1);      C[:,1] = 0.159*(1+z)
    return np.log(s8*(z+0.774)**np.log(s8)*np.amin(C,axis=1)/A1**0.387)
"""

#def function(params): #errors4.txt
#    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
#    return 2.016 + 0.1345*(1+z)*A3 + 2.549*s8*np.log(1.0+z) - 0.0399*(1+z)/Om - s8*A3 - 0.6195*(1+z) - 2.94*A1**0.1384

#def function(params): #errors5.txt
#    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
#    return (1+z)*(0.589*Om - 1.715/(1+z)**2 - 0.397/s8) + 0.501**A1 - 0.0226*A1/Om - A3*np.exp(Om - 0.397*(1+z)/s8 - 0.132*A1)

#def function(params): #errors6.txt
#    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
#    return 0.39**A1 + (1+z)*(0.559*Om - 0.365/s8 - 3.57e-3*A1/(Om*s8)) - (1.777 + s8*A3)/(1+z)

#def function(params): #errors7.txt
#    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
#    return (1+z)*(0.54*Om - 0.352/s8 - 4.366e-3*A1/(Om*s8)) + 0.854*0.418**A1 - (1.732 + s8*A3)/(1+z)

#def function(params): #errors8.txt
#    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
#    return 0.692*A1**0.458/((1+z)*A3) - 1.21*A1**0.406 - 1.631 + 2.534*np.log(1+z) - 0.038*(1+z)/Om + (0.36 - 0.425*(1+z))/s8

def function(params): #errors9.txt
    z,Om,s8,A1,A3 = params[:,0], params[:,1], params[:,2], params[:,3], params[:,4]
    return 2.317*np.log(1+z) + 0.696/((1+z)*A3) - 0.0389*(1+z)/Om -0.379*(1+z)/s8 - 1.333 - A1**0.391



################################### INPUT ###########################################
root_in  = '/mnt/ceph/users/camels/Results/neural_nets/params_2_SFRH'
root_out = '/mnt/ceph/users/camels/Results/symbolic_regression'

f_SFRH   = '%s/SFRH_IllustrisTNG.npy'%root_in
f_params = '%s/params_IllustrisTNG.txt'%root_in

training_num = 700
testing_num  = 300

fout = '%s/errors9.txt'%root_out
#####################################################################################

# read SFRH and params; get the redshifts
SFRH   = np.load(f_SFRH);       SFRH = np.log10(SFRH)
params = np.loadtxt(f_params)
z      = np.linspace(0, 7, 100)

##### training set #####
x_train = np.zeros((training_num*100,5), dtype=np.float32)
y_train = np.zeros((training_num*100, ), dtype=np.float32)

# do a loop over the different realizations
count = 0
for i in range(training_num):
    
    # do a loop over the different redshfits
    for j in range(100):
        x_train[count,0] = z[j]
        x_train[count,1] = params[i,0]
        x_train[count,2] = params[i,1]
        x_train[count,3] = params[i,2]
        x_train[count,4] = params[i,4]
        y_train[count]   = SFRH[i,j]
        count += 1
########################

##### testing set #####
x_test = np.zeros((testing_num*100,5), dtype=np.float32)
y_test = np.zeros((testing_num*100, ), dtype=np.float32)

# do a loop over the different realizations
count = 0
for i in range(training_num, training_num + testing_num):
    
    # do a loop over the different redshfits
    for j in range(100):
        x_test[count,0] = z[j]
        x_test[count,1] = params[i,0]
        x_test[count,2] = params[i,1]
        x_test[count,3] = params[i,2]
        x_test[count,4] = params[i,4]
        y_test[count]   = SFRH[i,j]
        count += 1
########################

# do a loop over the different redshifts
f = open(fout, 'w')
for redshift in z:
    indexes = np.where(x_test[:,0]==redshift)[0]
    error_train, error_train2, error_test, error_test2 = \
    compute_errors(x_train[indexes], y_train[indexes], x_test[indexes], y_test[indexes])
    f.write('%.3f %.3f %.5f %.3f %.5f\n'%(redshift, error_train, error_train2, error_test, error_test2))
f.close()

# compute average error
error_train, error_train2, error_test, error_test2 = \
                                compute_errors(x_train, y_train, x_test, y_test)
print('Average train error  = %.3f'%error_train)
print('Average train error2 = %.3f'%error_train2)
print('Average test error   = %.3f'%error_test)
print('Average test error2  = %.3f'%error_test2)
