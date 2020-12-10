import torch 
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import numpy as np
import sys, os, time


# This class creates the dataset 
class make_dataset():

    def __init__(self, root, grid, verbose=False):

        # read the data
        f_maps = '%s/Images_T.npy'%root
        data = np.load(f_maps)
        unique_maps = data.shape[0]

        # normalize maps
        data = np.log10(data)
        minimum = np.min(data)
        maximum = np.max(data)
        mean = np.mean(data, dtype=np.float64)
        std  = np.std(data, dtype=np.float64)
        #data = (data - mean)/std
        data = 2*(data - minimum)/(maximum-minimum) - 1.0
        if verbose:
            print('%.3f < T(all) < %.3f'%(np.min(data), np.max(data)))            

        # crop maps
        data = data[:,:grid,:grid]

        # define the matrix hosting all data with all rotations/flipping
        data_all = np.zeros((unique_maps*8, data.shape[1], data.shape[2]), 
                            dtype=np.float32)
        
        # do a loop over all rotations (each is 90 deg)
        total_maps = 0
        for rot in [0,1,2,3]:
            data_rot = np.rot90(data, k=rot, axes=(1,2))

            data_all[total_maps:total_maps+unique_maps,:,:] = data_rot
            total_maps += unique_maps

            data_all[total_maps:total_maps+unique_maps,:,:] = np.flip(data_rot, axis=1)
            total_maps += unique_maps
            
        if verbose:
            print('A total of %d maps used'%total_maps)
            print('%.3f < T < %.3f'%(np.min(data), np.max(data)))

        self.size   = data.shape[0]
        self.output = torch.unsqueeze(torch.tensor(data, dtype=torch.float32),1)
        

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.output[idx]


# This routine creates the training and validation sets
def create_train_set(root, grid, batch_size, verbose=False):
    train_dataset = make_dataset(root, grid, verbose)
    train_loader  = DataLoader(dataset=train_dataset, batch_size=batch_size, 
                               shuffle=True)
    return train_loader


