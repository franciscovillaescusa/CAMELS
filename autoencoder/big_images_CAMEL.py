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
root_in  = '/mnt/ceph/users/camels/Results/autoencoder'
root_out = '/mnt/ceph/users/camels/Software/plots/autoencoder'
f_images = '/mnt/ceph/users/camels/Software/plots/autoencoder/CAMEL.npy'

seed       = 5 #to split images between training, validation and testing sets
grid       = 64
batch_size = 128 
BN_dim     = 500
hidden     = 32

num_images = 5

minimum, maximum = 3.277, 7.507 

f_model = 'model_fiducial_a_32_wd=1e-10_500dim.pt'
#f_model = 'model_a_32_wd=1e-9_noise_500dim.pt'

seed = 12
######################################################################################

# use GPUs if available
GPU = torch.cuda.is_available()
device = torch.device("cuda" if GPU else "cpu")
print('GPU:',GPU)
print('Training on',device)
cudnn.benchmark = True      #May train faster but cost more memory

# define variables needed to compute the error histogram
bins_histo  = np.logspace(-5,-1, 301)
mean_histo  = 10**(0.5*(np.log10(bins_histo[1:]) + np.log10(bins_histo[:-1])))
dhisto      = bins_histo[1:] - bins_histo[:-1]
histo_error = np.zeros(bins_histo.shape[0]-1, dtype=np.float64)

# define loss function
criterion = nn.MSELoss()

# get the data
data = np.load(f_images)
data = np.transpose(data)
data = 2*data/255.0-1.0
print(data.shape)
print(data.dtype)
print(np.min(data), np.max(data))

images = data
subimages = np.zeros((24*26,64,64), dtype=np.float32)
count = 0
for i in range(26):
    i_start, i_end = i*64, (i+1)*64

    for j in range(24):
        j_start, j_end = j*64, (j+1)*64
        
        subimages[count] = images[i_start:i_end, j_start:j_end]
        count += 1

subimages = torch.tensor(subimages, dtype=torch.float32)
subimages = torch.unsqueeze(subimages, 1)
subimages = subimages.to(device)

# define the model and load best model
model = architecture.autoencoder_64a(BN_dim, hidden).to(device)
model.load_state_dict(torch.load('%s/models/%s'%(root_in, f_model)))

# get autoencoder prediction
model.eval()
with torch.no_grad():
    recon_maps = model(subimages)
loss = criterion(recon_maps, subimages)
print('Test loss = %.3e'%loss.cpu().item())

# compute histogram
error = np.mean((recon_maps.cpu().numpy() - subimages.cpu().numpy())**2, axis=(1,2,3))
histo = np.histogram(error, bins=bins_histo)[0]
histo = histo/900.0
np.savetxt('%s/results/Error_CAMEL.txt'%root_in, np.transpose([mean_histo, histo]))

# plots
indexes = np.where(error<1.3e-3)[0]
vutils.save_image(torch.cat((subimages[indexes], recon_maps[indexes])), 
                  '%s/CAMEL_good_recon.png'%root_out, normalize=True, 
                  range=(-1.0, 1.0), nrow=len(indexes))
indexes = np.where(error>4e-3)[0]
vutils.save_image(torch.cat((subimages[indexes], recon_maps[indexes])), 
                  '%s/CAMEL_bad_recon.png'%root_out, normalize=True, 
                  range=(-1.0, 1.0), nrow=len(indexes))


images2 = torch.zeros((26*64,24*64), dtype=torch.float32)
count = 0
for i in range(26):
    i_start, i_end = i*64, (i+1)*64

    for j in range(24):
        j_start, j_end = j*64, (j+1)*64
        
        images2[i_start:i_end, j_start:j_end] = recon_maps[count,0]
        count += 1

# get the test maps and make images
images  = torch.tensor(images, dtype=torch.float32)

print('Average error = %.3e'%torch.mean((images-images2)**2))

# save plots
#vutils.save_image(torch.cat((images, images2)), 'CAMEL_recon.png', 
#                  normalize=True, range=(-1.0, 1.0), nrow=2)
vutils.save_image(images, '%s/CAMEL_original.png'%root_out, 
                  normalize=True, range=(-1.0, 1.0), nrow=1)
vutils.save_image(images2, '%s/CAMEL_reconstructed.png'%root_out, 
                  normalize=True, range=(-1.0, 1.0), nrow=1)
