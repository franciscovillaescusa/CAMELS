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
root_out = '/mnt/ceph/users/camels/Results/autoencoder'
f_images = '/mnt/ceph/users/camels/Results/GAN/Images_T.npy'
#f_images = '/mnt/ceph/users/camels/Results/GAN/Images_T_SIMBA.npy'

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

# define loss function
criterion = nn.MSELoss()

# get the data
data = np.load(f_images)
data = np.log10(data)
data = 2*(data - minimum)/(maximum-minimum) - 1.0

# get the random indexes
indexes = np.arange(data.shape[0])
np.random.seed(seed)
indexes = np.random.choice(indexes, num_images, replace=False)

images = data[indexes]
subimages = np.zeros((16*num_images,64,64), dtype=np.float32)
count = 0
for number in range(num_images):
    for i in range(4):
        if i==3:  i_start, i_end = 186,  250 
        else:     i_start, i_end = i*64, (i+1)*64

        for j in range(4):
            if j==3:  j_start, j_end = 186,  250 
            else:     j_start, j_end = j*64, (j+1)*64
        
            subimages[count] = images[number,i_start:i_end, j_start:j_end]
            count += 1

subimages = torch.tensor(subimages, dtype=torch.float32)
subimages = torch.unsqueeze(subimages, 1)
subimages = subimages.to(device)

# define the model and load best model
model = architecture.autoencoder_64a(BN_dim, hidden).to(device)
model.load_state_dict(torch.load('%s/models/%s'%(root_out, f_model)))

# get autoencoder prediction
model.eval()
with torch.no_grad():
    recon_maps = model(subimages)
loss = criterion(recon_maps, subimages)
print('Test loss = %.3e'%loss.cpu().item())


images2 = torch.zeros((num_images,250,250), dtype=torch.float32)
count = 0
for number in range(num_images):
    for i in range(4):
        if i==3:  i_start, i_end = 186,  250 
        else:     i_start, i_end = i*64, (i+1)*64

        for j in range(4):
            if j==3:  j_start, j_end = 186,  250 
            else:     j_start, j_end = j*64, (j+1)*64
        
            images2[number, i_start:i_end, j_start:j_end] = recon_maps[count,0]
            count += 1

# get the test maps and make images
images  = torch.tensor(images)
images  = torch.unsqueeze(images,1)
images2 = torch.unsqueeze(images2,1)

indexes = np.arange(num_images)

all_images = torch.zeros((num_images*2,1,250,250), dtype=torch.float32)
all_images[2*indexes]   = images
all_images[2*indexes+1] = images2

vutils.save_image(all_images,#torch.cat((images, images2)), 
                  'big_image.png', normalize=True, range=(-1.0, 1.0),
                  nrow=2)#num_images, 
