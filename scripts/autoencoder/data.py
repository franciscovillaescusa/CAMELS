import torch 
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
import numpy as np
import sys, os, time


# This class creates the dataset 
class make_dataset():

    def __init__(self, mode, seed, f_images, grid, minimum=None, maximum=None, 
                 verbose=False):

        # read the data
        data = np.load(f_images) #[number of maps, height, width]

        # normalize maps
        data = np.log10(data)
        if minimum is None:  minimum = np.min(data)
        if maximum is None:  maximum = np.max(data)
        if verbose:  print('%.3f < T(all) < %.3f'%(np.min(data), np.max(data))) 
        data = 2*(data - minimum)/(maximum-minimum) - 1.0
        if verbose:  print('%.3f < T(all) < %.3f'%(np.min(data), np.max(data))) 

        # crop maps
        data = data[:,:grid,:grid]

        # get the size and offset depending on the type of dataset
        unique_maps = data.shape[0]
        if   mode=='train':  
            size, offset = int(unique_maps*0.70), int(unique_maps*0.00)
        elif mode=='valid':  
            size, offset = int(unique_maps*0.15), int(unique_maps*0.70)
        elif mode=='test':   
            size, offset = int(unique_maps*0.15), int(unique_maps*0.85)
        elif mode=='all':
            size, offset = int(unique_maps*1.00), int(unique_maps*0.00)
        else:    raise Exception('Wrong name!')

        # randomly shuffle the maps. Instead of 0 1 2 3...999 have a 
        # random permutation. E.g. 5 9 0 29...342
        np.random.seed(seed)
        indexes = np.arange(unique_maps) #only shuffle realizations, not rotations
        np.random.shuffle(indexes)
        indexes = indexes[offset:offset+size] #select indexes of mode

        # keep only the data with the corresponding indexes
        data = data[indexes]

        # define the matrix hosting all data with all rotations/flipping
        # together with the array containing the numbers of each map
        data_all    = np.zeros((size*8, data.shape[1], data.shape[2]), dtype=np.float32)
        numbers_all = np.zeros(size*8, dtype=np.int32)

        # do a loop over all rotations (each is 90 deg)
        total_maps = 0
        for rot in [0,1,2,3]:
            data_rot = np.rot90(data, k=rot, axes=(1,2))

            data_all[total_maps:total_maps+size,:,:] = data_rot
            numbers_all[total_maps:total_maps+size] = indexes
            total_maps += size

            data_all[total_maps:total_maps+size,:,:] = np.flip(data_rot, axis=1)
            numbers_all[total_maps:total_maps+size] = indexes
            total_maps += size
            
        if verbose:
            print('A total of %d maps used'%total_maps)
            print('%.3f < T < %.3f'%(np.min(data), np.max(data)))

        self.size    = data_all.shape[0]
        self.maps    = torch.unsqueeze(torch.tensor(data_all, dtype=torch.float32),1)
        self.numbers = torch.tensor(numbers_all, dtype=torch.int32)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.maps[idx], self.numbers[idx]


# This routine creates the dataset
def create_dataset(mode, seed, f_images, grid, batch_size, minimum, maximum, 
                   verbose=False):
    data_set    = make_dataset(mode, seed, f_images, grid, minimum, maximum, verbose)
    data_loader = DataLoader(dataset=data_set, batch_size=batch_size, shuffle=True)
    return data_loader

######################################################################################
######################################################################################
######################################################################################

# This class creates the dataset of the fiducial TNG realizations 
class make_dataset_fiducial():

    def __init__(self, mode, seed, f_images, grid, minimum=None, maximum=None,
                 verbose=False):

        # read the data
        data = np.load(f_images) #[number of maps, height, width]

        # normalize maps
        data = np.log10(data)
        if minimum is None:  minimum = np.min(data)
        if maximum is None:  maximum = np.max(data)
        if verbose:  print('%.3f < T(all) < %.3f'%(np.min(data), np.max(data))) 
        data = 2*(data - minimum)/(maximum-minimum) - 1.0
        if verbose:  print('%.3f < T(all) < %.3f'%(np.min(data), np.max(data))) 

        # get all the subimages
        offset_image = 15 #number of pixels to move the frame for a new image
        subimages_dir = (data.shape[1]-grid)//offset_image + 1
        images_tot = subimages_dir*subimages_dir*data.shape[0]
        new_data = np.zeros((images_tot,grid,grid), dtype=np.float32)

        count = 0
        for l in range(data.shape[0]):
            for i in range(subimages_dir):
                x_start, x_end = offset_image*i, offset_image*i+grid
                for j in range(subimages_dir):
                    y_start, y_end = offset_image*j, offset_image*j+grid

                    #print(x_start,x_end)
                    #print(y_start,y_end)
                    new_data[count] = data[l, x_start:x_end, y_start:y_end]
                    count += 1
        print('Using %d maps'%count)


        # get the size and offset depending on the type of dataset
        unique_maps = new_data.shape[0]
        if   mode=='train':  
            size, offset = int(unique_maps*0.70), int(unique_maps*0.00)
        elif mode=='valid':  
            size, offset = int(unique_maps*0.15), int(unique_maps*0.70)
        elif mode=='test':   
            size, offset = int(unique_maps*0.15), int(unique_maps*0.85)
        elif mode=='all':
            size, offset = int(unique_maps*1.00), int(unique_maps*0.00)
        else:    raise Exception('Wrong name!')

        # randomly shuffle the maps. Instead of 0 1 2 3...999 have a 
        # random permutation. E.g. 5 9 0 29...342
        np.random.seed(seed)
        indexes = np.arange(unique_maps) #only shuffle realizations, not rotations
        np.random.shuffle(indexes)
        indexes = indexes[offset:offset+size] #select indexes of mode

        # keep only the data with the corresponding indexes
        data = new_data[indexes]

        # define the matrix hosting all data with all rotations/flipping
        # together with the array containing the numbers of each map
        data_all    = np.zeros((size*8, data.shape[1], data.shape[2]), dtype=np.float32)
        numbers_all = np.zeros(size*8, dtype=np.int32)

        # do a loop over all rotations (each is 90 deg)
        total_maps = 0
        for rot in [0,1,2,3]:
            data_rot = np.rot90(data, k=rot, axes=(1,2))

            data_all[total_maps:total_maps+size,:,:] = data_rot
            numbers_all[total_maps:total_maps+size] = indexes
            total_maps += size

            data_all[total_maps:total_maps+size,:,:] = np.flip(data_rot, axis=1)
            numbers_all[total_maps:total_maps+size] = indexes
            total_maps += size
            
        if verbose:
            print('A total of %d maps used'%total_maps)
            print('%.3f < T < %.3f'%(np.min(data), np.max(data)))

        self.size    = data_all.shape[0]
        self.maps    = torch.unsqueeze(torch.tensor(data_all, dtype=torch.float32),1)
        self.numbers = torch.tensor(numbers_all, dtype=torch.int32)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.maps[idx], self.numbers[idx]


# This routine creates the dataset
def create_dataset_fiducial(mode, seed, f_images, grid, batch_size, minimum, maximum, 
                            verbose=False):
    data_set    = make_dataset_fiducial(mode, seed, f_images, grid, minimum, maximum, 
                                        verbose)
    data_loader = DataLoader(dataset=data_set, batch_size=batch_size, shuffle=True)
    return data_loader
