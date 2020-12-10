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
root_in  = '/mnt/ceph/users/camels'
root_G   = '/mnt/ceph/users/camels/Results/GAN'
folder_plot = '/mnt/ceph/users/camels/Software/plots/GAN'

seed    = 125
grid    = 64
net_num = 348

# parameters for big images
rows_big    = 6
columns_big = 15

# parameters for interpolation
rows_inter    = 6 #number of interpolations between two images
columns_inter = 6

Z_DIM      = 100
G_HIDDEN   = 128
######################################################################################

z1_index = {0:11, 1:28, 2:89, 3:45, 4:37, 5:3}
z2_index = {0:47, 1:30, 2:24, 3:28, 4:76, 5:66}

# random seed
np.random.seed(seed)
torch.manual_seed(seed)

# use GPUs if available
GPU = torch.cuda.is_available()
device = torch.device("cuda" if GPU else "cpu")
print('GPU:',GPU)
print('Trainin on',device)
cudnn.benchmark = True

# define generator and load best-fit model
netG = architecture.Generator_64(Z_DIM, G_HIDDEN).to(device)
netG.load_state_dict(torch.load('%s/models_64/Net_Gen_%d.pt'%(root_G,net_num)))

######### big images ##########
# get real images images
#train_loader = data.create_train_set(root_G, grid, rows_big*columns_big, verbose=True)
#for data in train_loader:
#    vutils.save_image(data, '%s/real_images.png'%folder_plot, 
#                      nrow=columns_big, normalize=True, range=(-1,1))
#    break

# define the tensor hosting the points in latent space
z = torch.randn(rows_big*columns_big, Z_DIM, 1, 1, device=device)
fake_maps = netG(z)
vutils.save_image(fake_maps, '%s/fake_images.png'%folder_plot, 
                  nrow=columns_big, normalize=True, range=(-1,1))
###############################

######## interpolation ########
# define the tensor hosting the points in latent space
z_inter = np.zeros((rows_inter*columns_inter, Z_DIM, 1, 1), dtype=np.float32)

# define the vector for interpolate points in latent space
t = np.linspace(0, 1, columns_inter)

# do a loop over the different rows (interpolations)
count = 0
for i in range(rows_inter):

    # generate points in latent space to generate test images
    z1 = z[z1_index[i]][:,0,0].cpu() #np.random.randn(Z_DIM)
    z2 = z[z2_index[i]][:,0,0].cpu() #np.random.randn(Z_DIM)

    cos_angle = np.dot(z1,z2)/np.sqrt(np.dot(z1,z1)*np.dot(z2,z2))
    angle = np.arccos(cos_angle)

    for j in range(columns_inter):
        # linear interpolation
        #z[count,:,0,0] = z1 + (z2-z1)*t[j]
        # Slerp interpolation
        z_inter[count,:,0,0] = (np.sin((1-t[j])*angle)*z1 + np.sin(t[j]*angle)*z2)/np.sin(angle)
        count += 1

# make it a torch tensor
z_inter = torch.tensor(z_inter, device=device)
        
# generate maps and save figure
with torch.no_grad():
    fake_maps = netG(z_inter)
    vutils.save_image(fake_maps, '%s/fake_samples_interp.png'%folder_plot, 
                      nrow=columns_inter, normalize=True, range=(-1,1))



