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
f_model    = 'model_a_32_wd=1e-9_noise_500dim.pt'
sim        = 'IllustrisTNG'
mode       = 'test'  #'train', 'valid', 'test', 'all'
######################################################################################

# get the name of the file containing the images
f_images = '/mnt/ceph/users/camels/Results/autoencoder/Images_T_extreme_0.npy'
f_images = '/mnt/ceph/users/camels/Results/autoencoder/Images_T_extremestellar_0.npy'

# use GPUs if available
GPU = torch.cuda.is_available()
device = torch.device("cuda" if GPU else "cpu")
print('GPU:',GPU)
print('Training on',device)
cudnn.benchmark = True      #May train faster but cost more memory

# define loss function
criterion = nn.MSELoss()

# get the data & crop maps
data = np.load(f_images)
data = np.log10(data)
minimum, maximum = 3.182, 7.948  #np.min(data), np.max(data)
data = 2*(data - minimum)/(maximum-minimum) - 1.0
print('%.3f < T(all) < %.3f'%(np.min(data), np.max(data))) 
#data = data[:,:grid,:grid]
maps = np.zeros((15*12*12, 64, 64), dtype=np.float32)
count = 0 
for map_num in range(15):
    for i in range(12):
        for j in range(12):
            maps[count] = data[map_num, 15*i:15*i+64, 15*j:15*j+64]
            count += 1
test_maps = torch.tensor(maps, dtype=torch.float32)
test_maps = test_maps.unsqueeze(1)

# define the model and load best model
model = architecture.autoencoder_64a(BN_dim, hidden).to(device)
model.load_state_dict(torch.load('%s/models/%s'%(root_out, f_model)))

# define variables needed to compute the error histogram
#bins_histo  = np.logspace(-5,-1, 501)
#mean_histo  = 10**(0.5*(np.log10(bins_histo[1:]) + np.log10(bins_histo[:-1])))
#dhisto      = bins_histo[1:] - bins_histo[:-1]
#histo_error = np.zeros(bins_histo.shape[0]-1, dtype=np.float64)

# compute test loss
test_loss, maps, batches = 0.0, 0, 0
min_error, mean_error, max_error = 1e9, 0.0, 0.0
model.eval()
with torch.no_grad():

    # get input, output maps and loss
    test_maps = test_maps.to(device)
    recon_maps = model(test_maps)
    loss = criterion(recon_maps, test_maps)

    # get cumulative loss and number of maps
    test_loss += loss.cpu().item()
    batches += 1
    maps += test_maps.shape[0]

    """
    # save some images
    if test_maps.shape[0]>examples:
        vutils.save_image(torch.cat((test_maps[:examples],recon_maps[:examples])), 
                          '%s/images/images_%s_%s.png'%(root_out,sim,mode),\
                          normalize=True, nrow=examples, range=(-1.0, 1.0))
    """

    # compute reconstruction error for each map
    error = ((test_maps - recon_maps)**2).cpu().numpy()
    error = np.mean(error, axis=(1,2,3))
    mean_error += np.sum(error)
    #histo_error += np.histogram(error, bins_histo)[0]

    # identify the larger reconstruction error and make image
    index = np.where(error==np.max(error))[0]
    if error[index]>max_error:
        max_error = error[index]
        print('max error = %.3e'%(max_error))
        vutils.save_image(torch.cat([test_maps[index],recon_maps[index]]), 
                          '%s/images/images_outlier_extreme_0.png'%(root_out),\
                          normalize=True, nrow=1, range=(-1.0, 1.0))

    # identify the smaller reconstruction error
    index = np.where(error==np.min(error))[0]
    if error[index]<min_error:
        min_error = error[index]
        print('min error = %.3e'%(min_error))

# finale verbose
print('\nTest loss  = %.3e'%(test_loss/batches))
print('Min = %.3e  :  Max = %.3e'%(min_error, max_error))
print('Mean error = %.3e'%(mean_error/maps))
print('Number of maps = %d'%maps)

# histogram
#histo_error = histo_error/maps/dhisto
#print('Integral histo = %.3e'%(np.sum(histo_error*dhisto)))
#np.savetxt('Errors_%s_%s_500dim.txt'%(sim,mode), np.transpose([mean_histo, histo_error]))
