import numpy as np
import torch
import sys,os
sys.path.append('../')
import data as data
import architecture

#################################### INPUT ##########################################
root_in      = '/mnt/ceph/users/camels'
root_out     = '/mnt/ceph/users/camels/Results/neural_nets/params_2_SFRH/SIMBA'
sim          = 'SIMBA'
bins_SFRH    = 100
realizations = 1000

# architecture parameters
h1 = 1000
h2 = 1000
h3 = 2000
h4 = 100
dr = 0.0

# name of the output files
name   = '1hd_1000_0.0_5e-5'
fout   = '%s/results/%s_1P.txt'%(root_out,name)
fmodel = '%s/models/%s.pt'%(root_out,name)
#####################################################################################

# get GPU if possible
if torch.cuda.is_available():
    print("CUDA Available")
    device = torch.device('cuda')
else:
    print("CUDA Not Available")
    device = torch.device('cpu')

# get the test dataset
params_sorted = np.loadtxt('%s/params_%s.txt'%(root_out,sim))
min_params    = np.min(params_sorted, axis=0)
max_params    = np.max(params_sorted, axis=0)

# generate the parameters                            
params = np.zeros((66,6), dtype=np.float64)

# set fiducial values
params[:,0] = 0.3
params[:,1] = 0.8
params[:,2] = 1.0
params[:,3] = 1.0
params[:,4] = 1.0
params[:,5] = 1.0

# set value of sims with different Omega_m                             
params[:11,  0] = np.linspace(0.1, 0.5, 11)
params[11:22,1] = np.linspace(0.6, 1.0, 11)
params[22:33,2] = np.logspace(np.log10(0.25), np.log10(4.00), 11)
params[33:44,3] = np.logspace(np.log10(0.25), np.log10(4.00), 11)
params[44:55,4] = np.logspace(np.log10(0.50), np.log10(2.00), 11)
params[55:66,5] = np.logspace(np.log10(0.50), np.log10(2.00), 11)
params = (params - min_params)/(max_params - min_params)
params = params.astype(np.float32)
params = torch.from_numpy(params)

# get the parameters of the trained model
model = architecture.model_1hl(6, h1, bins_SFRH, dr)
#model = architecture.model_3hl(6, h1, h2, h3, bins_SFRH, dr)
model.load_state_dict(torch.load(fmodel))
model.to(device=device)

# get prediction
offset = 0
model.eval()
with torch.no_grad():
    params = params.to(device)
    SFRH   = model(params)

# load all SFRH and compute mean and std
SFRH_all = data.read_all_SFRH(root_in, sim, realizations, bins_SFRH, root_out)
SFRH_all[np.where(SFRH_all==0.0)] = 1e-12 #avoid points with SFRH=0
SFRH_all = np.log10(SFRH_all)
mean = np.mean(SFRH_all, axis=0, dtype=np.float64)
std  = np.std(SFRH_all,  axis=0, dtype=np.float64)

# de-normalize
SFRH = SFRH.cpu().numpy()
SFRH = 10**(SFRH*std + mean)

# save results to file
z = np.linspace(0.0, 7.0, bins_SFRH)
results = np.zeros((bins_SFRH, 67), dtype=np.float32)
results[:,0] = z
for i in range(1,67):
    results[:,i] = SFRH[i-1]
np.savetxt(fout, results)
