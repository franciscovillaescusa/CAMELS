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
examples   = 16

f_model = 'model_a_32_wd=1e-9_noise_500dim.pt'
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
test_loader  = data.create_dataset('test', seed, f_images, grid, batch_size, 
                                   verbose=True)
test_batches = len(test_loader)

# define the model and load best model
model = architecture.autoencoder_64a(BN_dim, hidden).to(device)
model.load_state_dict(torch.load('%s/models/%s'%(root_out, f_model)))

# compute test loss
test_loss, num_maps = 0.0, 0
model.eval()
for test_maps,idxs in test_loader:
    with torch.no_grad():
        test_maps  = test_maps.to(device)
        recon_maps = model(test_maps)
        loss = criterion(recon_maps, test_maps)
        test_loss += loss.cpu().item()*test_maps.shape[0]
        num_maps  += test_maps.shape[0]
test_loss = test_loss/num_maps
print('Test loss = %.3e'%test_loss)

# get the test maps and make images
for test_maps,idxs in test_loader:
    test_maps = (test_maps[:examples]).to(device)
    break
input_maps = test_maps + torch.randn_like(test_maps, device=device)*0.1
recon_maps = model(input_maps)
vutils.save_image(torch.cat((input_maps,recon_maps,test_maps)), 
                  '%s/images/images_test_IllustrisTNG.png'%root_out,\
                  normalize=True, nrow=examples, range=(-1.0, 1.0))
