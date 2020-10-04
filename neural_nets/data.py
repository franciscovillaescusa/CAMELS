import torch 
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import numpy as np
import sys, os, time


# This routine reads all SFRH
def read_all_SFRH(root_in, sim, realizations, bins, root_out):

    # check if file already exists
    fout = '%s/SFRH_%s.npy'%(root_out,sim)
    if os.path.exists(fout):  return np.load(fout)

    # define the redshift and SFRH arrays
    z    = np.linspace(0.0, 7.0, bins)
    SFRH = np.zeros((realizations,bins), dtype=np.float32)

    # do a loop over all realizations and save results to file
    for i in range(realizations):
        fin = '%s/Results/SFRH/%s/%d/SFRH_0.00_10.00_10000.txt'%(root_in,sim,i)
        z_real, SFRH_real = np.loadtxt(fin, unpack=True)
        SFRH[i] = np.interp(z, z_real, SFRH_real)
    np.save(fout, SFRH)
    return SFRH

# This class creates the dataset 
class make_dataset():

    def __init__(self, mode, seed, realizations, root_in, bins, sim, root_out):

        # get the size and offset depending on the type of dataset
        if   mode=='train':  
            size, offset = int(realizations*0.70), int(realizations*0.00)
        elif mode=='valid':  
            size, offset = int(realizations*0.15), int(realizations*0.70)
        elif mode=='test':   
            size, offset = int(realizations*0.15), int(realizations*0.85)
        elif mode=='all':
            size, offset = int(realizations*1.00), int(realizations*0.00)
        else:    raise Exception('Wrong name!')

        # define size, input and output matrices
        self.size   = size
        self.input  = torch.zeros((size,6),    dtype=torch.float)
        self.output = torch.zeros((size,bins), dtype=torch.float)

        # read the value of the parameters and normalize them
        params     = np.loadtxt('%s/params_%s.txt'%(root_out,sim))
        min_params = np.min(params, axis=0)
        max_params = np.max(params, axis=0)
        params     = (params - min_params)/(max_params - min_params)

        # read the SFRH and normalize them
        SFRH = read_all_SFRH(root_in, sim, realizations, bins, root_out)
        SFRH[np.where(SFRH==0.0)] = 1e-12 #avoid points with SFRH=0
        SFRH = np.log10(SFRH)
        mean = np.mean(SFRH, axis=0, dtype=np.float64)
        std  = np.std(SFRH,  axis=0, dtype=np.float64)
        SFRH = (SFRH - mean)/std

        # randomly shuffle the cubes. Instead of 0 1 2 3...999 have a 
        # random permutation. E.g. 5 9 0 29...342
        np.random.seed(seed)
        indexes = np.arange(realizations) #only shuffle realizations, not rotations
        np.random.shuffle(indexes)
        indexes = indexes[offset:offset+size] #select indexes of mode

        # get the corresponding parameters and SFRH
        self.input  = torch.tensor(params[indexes], dtype=torch.float32)
        self.output = torch.tensor(SFRH[indexes],   dtype=torch.float32)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.input[idx], self.output[idx]


# This routine creates a dataset loader
def create_dataset(mode, seed, realizations, root_in, bins, sim, batch_size, root_out):
    data_set = make_dataset(mode, seed, realizations, root_in, bins, sim, root_out)
    dataset_loader = DataLoader(dataset=data_set, batch_size=batch_size, shuffle=True)
    return dataset_loader
