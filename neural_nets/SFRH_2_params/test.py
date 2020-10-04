import numpy as np
import torch
import sys,os
sys.path.append('../')
import data as data
import architecture

#################################### INPUT ##########################################
# data parameters
root_in      = '/mnt/ceph/users/camels'
root_out     = '/mnt/ceph/users/camels/Results/neural_nets/SFRH_2_params'
sim          = 'IllustrisTNG'
seed         = 1
realizations = 1000
bins_SFRH    = 100

# architecture parameters
h1 = 750
h2 = 750
h3 = 750
dropout_rate = 0.0

# training parameters
batch_size = 10

minimum = np.array([0.1, 0.6, 0.25, 0.25, 0.5, 0.5])
width   = np.array([0.4, 0.4, 3.75, 3.75, 1.5, 1.5])

# name of output files
name   = '3hd_750_750_750_0.0_3e-3'
fout   = '%s/results/%s.txt'%(root_out,name)
fmodel = '%s/models/%s.pt'%(root_out,name)
#####################################################################################

# get GPU if available
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
for params_test, SFRH_test in test_loader:
    size += params_test.shape[0]

# define the array with the results
pred = np.zeros((size,6), dtype=np.float32)
true = np.zeros((size,6), dtype=np.float32)

# get the parameters of the trained model
#model = architecture.model_1hl(bins_SFRH, h1, 6, dropout_rate)
#model = architecture.model_2hl(bins_SFRH, h1, h2, 6, dropout_rate)
model = architecture.model_3hl(bins_SFRH, h1, h2, h3, 6, dropout_rate)
model.load_state_dict(torch.load(fmodel))
model.to(device=device)

# loop over the different batches and get the prediction
offset = 0
model.eval()
for params_test, SFRH_test in test_loader:
    with torch.no_grad():
        #params_test = params_test.to(device)
        SFRH_test   = SFRH_test.to(device)
        params_pred = model(SFRH_test)
        length = params_test.shape[0]
        pred[offset:offset+length] = params_pred.cpu().numpy()
        true[offset:offset+length] = params_test.numpy()
        offset += length

# compute the rmse; de-normalize
error_norm = ((pred - true))**2
pred  = pred*width + minimum
true  = true*width + minimum
error = (pred - true)**2

print('Error^2 norm      = %.3e'%np.mean(error_norm))
print('Error             = %.3e'%np.sqrt(np.mean(error)))
print('Relative error Om = %.3e'%np.sqrt(np.mean(error[:,0])))
print('Relative error s8 = %.3e'%np.sqrt(np.mean(error[:,1])))
print('Relative error A1 = %.3e'%np.sqrt(np.mean(error[:,2])))
print('Relative error A2 = %.3e'%np.sqrt(np.mean(error[:,3])))
print('Relative error A3 = %.3e'%np.sqrt(np.mean(error[:,4])))
print('Relative error A4 = %.3e'%np.sqrt(np.mean(error[:,5])))

# save results to file
results = np.zeros((size,12))
results[:,0:6]  = true
results[:,6:12] = pred
np.savetxt(fout, results)

