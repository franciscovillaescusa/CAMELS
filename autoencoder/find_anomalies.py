import numpy as np
import sys,os
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torchvision.utils as vutils
import data
import architecture

################################### INPUT ############################################
root_out   = '/mnt/ceph/users/camels/Results/autoencoder'
seed       = 5 #to split images between training, validation and testing sets
grid       = 64
batch_size = 128 
BN_dim     = 500
hidden     = 32
examples   = 16
sim        = 'IllustrisTNG_fiducial' #'IllustrisTNG', 'SIMBA', 'IllustrisTNG_fiducial'
mode       = 'all'  #'train', 'valid', 'test', 'all'

#f_model    = 'model_a_32_wd=1e-9_noise_500dim.pt'
#minimum, maximum = 3.182, 7.948

f_model    = 'model_fiducial_a_32_wd=1e-10_500dim.pt'
minimum, maximum = 3.277, 7.507 

fout = '%s/results/Errors_train_on_fiducialTNG_test_on_allfiducialTNG.txt'%root_out
######################################################################################

# get the name of the file containing the images and the data
if sim=='IllustrisTNG':  
    f_images    = '/mnt/ceph/users/camels/Results/GAN/Images_T.npy'
    test_loader = data.create_dataset(mode, seed, f_images, grid, batch_size, 
                                      minimum, maximum, verbose=True)
elif sim=='SIMBA':
    f_images    = '/mnt/ceph/users/camels/Results/GAN/Images_T_SIMBA.npy'
    test_loader = data.create_dataset(mode, seed, f_images, grid, batch_size, 
                                      minimum, maximum, verbose=True)
elif sim=='IllustrisTNG_fiducial':
    f_images    = '/mnt/ceph/users/camels/Results/autoencoder/Images_T_fiducial_IllustrisTNG.npy'
    test_loader = data.create_dataset_fiducial(mode, seed, f_images, grid, batch_size, 
                                               minimum, maximum, verbose=True)
else:
    raise Exception('Incorrect sim!')

# use GPUs if available
GPU = torch.cuda.is_available()
device = torch.device("cuda" if GPU else "cpu")
print('GPU:',GPU)
print('Training on',device)
cudnn.benchmark = True      #May train faster but cost more memory

# define loss function
criterion = nn.MSELoss()

# define the model and load best model
model = architecture.autoencoder_64a(BN_dim, hidden).to(device)
model.load_state_dict(torch.load('%s/models/%s'%(root_out, f_model)))

# define variables needed to compute the error histogram
bins_histo  = np.logspace(-6,-2, 301)
mean_histo  = 10**(0.5*(np.log10(bins_histo[1:]) + np.log10(bins_histo[:-1])))
dhisto      = bins_histo[1:] - bins_histo[:-1]
histo_error = np.zeros(bins_histo.shape[0]-1, dtype=np.float64)

# compute test loss
test_loss, maps, batches = 0.0, 0, 0
min_error, mean_error, max_error = 1e9, 0.0, 0.0
model.eval()
for test_maps, numbers in test_loader:
    with torch.no_grad():

        # get input, output maps and loss
        test_maps = test_maps.to(device)
        recon_maps = model(test_maps)
        loss = criterion(recon_maps, test_maps)

        # get cumulative loss and number of maps
        test_loss += loss.cpu().item()
        batches += 1
        maps += test_maps.shape[0]

        # save some images
        #if test_maps.shape[0]>examples:
        #    vutils.save_image(torch.cat((test_maps[:examples],recon_maps[:examples])), 
        #                      '%s/images/images_%s_%s.png'%(root_out,sim,mode),\
        #                      normalize=True, nrow=examples, range=(-1.0, 1.0))

        # compute reconstruction error for each map
        error = ((test_maps - recon_maps)**2).cpu().numpy()
        error = np.mean(error, axis=(1,2,3))
        mean_error += np.sum(error)
        histo_error += np.histogram(error, bins_histo)[0]

        # identify the larger reconstruction error and make image
        index = np.where(error==np.max(error))[0]
        if error[index]>max_error:
            max_error = error[index]
            print('max error = %.3e : %d'%(max_error, numbers[index]))
            #vutils.save_image(torch.cat([test_maps[index],recon_maps[index]]), 
            #                 '%s/images/images_%s_%s_outlier.png'%(root_out,sim,mode),\
            #                  normalize=True, nrow=1, range=(-1.0, 1.0))

        # identify the smaller reconstruction error
        index = np.where(error==np.min(error))[0]
        if error[index]<min_error:
            min_error = error[index]
            print('min error = %.3e : %d'%(min_error, numbers[index]))

# final verbose
print('\nTest loss  = %.3e'%(test_loss/batches))
print('Min = %.3e  :  Max = %.3e'%(min_error, max_error))
print('Mean error = %.3e'%(mean_error/maps))
print('Number of maps = %d'%maps)

# histogram
histo_error = histo_error/maps#/dhisto
print('Integral histo = %.3e'%(np.sum(histo_error*dhisto)))
np.savetxt(fout, np.transpose([mean_histo, histo_error]))
