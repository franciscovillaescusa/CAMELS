import numpy as np
import torch
import sys,os
import torch.backends.cudnn as cudnn
sys.path.append('../')
import data as data
import architecture

#################################### INPUT ##########################################
root_in      = '/mnt/ceph/users/camels'
root_out     = '/mnt/ceph/users/camels/Results/neural_nets/params_2_SFRH'
sim          = 'IllustrisTNG'
bins_SFRH    = 100

# architecture parameters
h1 = 500
h2 = 2000
h3 = 2000
h4 = 100
wd = 1e-8
dr = 0.2

seed         = 1
realizations = 1000
batch_size   = 15
fmodel       = '%s/model.pt'%root_out
fout         = '%s/SFRH_ML.txt'%root_out
#####################################################################################

# get GPU if possible
if torch.cuda.is_available():
    print("CUDA Available")
    device = torch.device('cuda')
else:
    print("CUDA Not Available")
    device = torch.device('cpu')

# get the test dataset
test_loader  = data.create_dataset('test', seed, realizations, root_in, bins_SFRH, 
                                   sim, batch_size, root_out)

# get the number of elements in the test set
size = 0
for x_test, y_test in test_loader:
    size += x_test.shape[0]

# define the array with the results
params_pred = np.zeros((size,bins_SFRH), dtype=np.float32)
params_true = np.zeros((size,bins_SFRH), dtype=np.float32)

# get the parameters of the trained model
model = architecture.model_1hl(6, h1, bins_SFRH, dr)
#model = architecture.model_3hl(6, h1, h2, h3, bins_SFRH, dr)
model.load_state_dict(torch.load(fmodel))
model.to(device=device)

# loop over the different batches and get the prediction
offset = 0
model.eval()
for params_test, SFRH_test in test_loader:
    with torch.no_grad():
        params_test = params_test.to(device)
        SFRH_pred = model(params_test)
        length = params_test.shape[0]
        params_pred[offset:offset+length] = SFRH_pred.cpu().numpy()
        params_true[offset:offset+length] = SFRH_test.numpy()
        offset += length

# compute the rmse
error = np.mean((params_pred - params_true)**2)
print(error)

# load all SFRH and compute mean and std
SFRH = data.read_all_SFRH(root_in, sim, realizations, bins_SFRH, root_out)
SFRH = np.log10(SFRH)
mean = np.mean(SFRH, axis=0, dtype=np.float64)
std  = np.std(SFRH,  axis=0, dtype=np.float64)

# de-normalize
SFRH_pred = 10**(params_pred*std + mean)
SFRH_true = 10**(params_true*std + mean)
log_error = np.mean((np.log10(SFRH_pred) - np.log10(SFRH_true))**2)
print('log_error = %.4f'%np.sqrt(log_error))

# relative error
rel_error = np.mean((np.log10(SFRH_pred) - np.log10(SFRH_true))**2/np.log10(SFRH_true)**2)
print('rel_error = %.4f'%np.sqrt(rel_error))

# save results to file
z = np.linspace(0.0, 7.0, 100)
results = np.zeros((bins_SFRH, 2*size+1), dtype=np.float32)
results[:,0] = z
for i in range(1,size+1):
    results[:,i] = SFRH_pred[i-1]
for i in range(size+1,2*size+1):
    results[:,i] = SFRH_true[i-size-1]
np.savetxt(fout, results)
