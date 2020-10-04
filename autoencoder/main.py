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
import matplotlib.pyplot as plt
import utils


################################### INPUT ############################################
# images parameters
f_images = '/mnt/ceph/users/camels/Results/GAN/Images_T.npy'
seed     = 5 #to split images between training, validation and testing sets
grid     = 64
examples = 16 # when saving images for different epochs

# architecture parameters
lr         = 1e-4
hidden     = 32
wd         = 1e-11
epochs     = 100000
batch_size = 128
BN_dim     = 500

# output files
root_out = '/mnt/ceph/users/camels/Results/autoencoder'
f_loss   = '%s/losses/loss_model_a_32_wd=1e-11_noise_10_500dim.txt'%root_out
f_model  = '%s/models/model_a_32_wd=1e-11_noise_10_500dim.pt'%root_out
######################################################################################

# use GPUs if available
GPU = torch.cuda.is_available()
device = torch.device("cuda" if GPU else "cpu")
print('GPU:',GPU)
print('Training on',device)
cudnn.benchmark = True      #May train faster but cost more memory

# define loss function
criterion = nn.MSELoss()
#criterion = nn.L1Loss()

# get the data
train_loader = data.create_dataset('train', seed, f_images, grid, batch_size, 
                                   verbose=True)
valid_loader = data.create_dataset('valid', seed, f_images, grid, batch_size, 
                                   verbose=True)

# define the model
#model = architecture.autoencoder_64a(BN_dim, hidden).to(device)
model = architecture.autoencoder_64h(BN_dim, hidden).to(device)
#model = architecture.autoencoder_64d(BN_dim, hidden).to(device)
#model = architecture.autoencoder_64e(BN_dim, hidden).to(device)
#model = architecture.autoencoder_64f(BN_dim, hidden).to(device)
#model = architecture.autoencoder_64g(BN_dim, hidden).to(device)
#model = architecture.autoencoder_64c(BN_dim, hidden).to(device)
#model = architecture.autoencoder_64b(BN_dim, hidden).to(device)

# load best-models, if they exists
if os.path.exists(f_model):  model.load_state_dict(torch.load(f_model))
else:                        model.apply(architecture.weights_init)

# define the optimizer
optimizer = optim.Adam(model.parameters(), lr=lr, betas=(0.5, 0.999), weight_decay=wd)

# get the tensor for the images
for valid_maps,idxs in valid_loader:
    test_maps = (valid_maps[:examples]).to(device)
    break

# do a loop over all the epochs
min_loss = 1e8
for epoch in range(epochs):
    
    # training
    train_loss, num_maps = 0.0, 0
    model.train()
    for train_maps,idxs in train_loader:
        train_maps = train_maps.to(device)
        input_maps = train_maps + torch.randn_like(train_maps, device=device)*0.1
        #recon_maps = model(train_maps)
        recon_maps = model(input_maps)

        #train_maps_fft = torch.rfft(train_maps, 2)
        #recon_maps_fft = torch.rfft(recon_maps, 2)
        #loss = ((train_maps_fft-recon_maps_fft)**2).mean()

        loss = criterion(recon_maps, train_maps)
        train_loss += (loss.cpu().item())*train_maps.shape[0]
        num_maps   += train_maps.shape[0]
        optimizer.zero_grad()
        loss.backward()
        #if epoch%25==0:
        #    utils.save_gradients('%s/gradients/gradients_g_%d.txt'%(root_out,epoch), model)
        optimizer.step()
    train_loss = train_loss/num_maps

    # validation
    valid_loss, num_maps = 0.0, 0
    model.eval()
    for valid_maps,idxs in valid_loader:
        with torch.no_grad():
            valid_maps = valid_maps.to(device)
            recon_maps = model(valid_maps)
            loss = criterion(recon_maps, valid_maps)
            valid_loss += (loss.cpu().item())*valid_maps.shape[0]
            num_maps   += valid_maps.shape[0]
    valid_loss = valid_loss/num_maps

    # verbose
    if valid_loss<min_loss:
        min_loss = valid_loss
        torch.save(model.state_dict(), f_model)
        print('Epoch %d: %.3e %.3e (saving)'%(epoch, train_loss, valid_loss))
    else:
        print('Epoch %d: %.3e %.3e'%(epoch, train_loss, valid_loss))

    # save losses
    f = open(f_loss, 'a')  
    f.write('%d %.3e %.3e\n'%(epoch, train_loss, valid_loss))
    f.close()

    """
    # plot some images & save models every 10 epochs
    if epoch%25==0:
        model.eval()
        with torch.no_grad():
            recon_maps = model(test_maps)
            vutils.save_image(torch.cat([test_maps,recon_maps]), 
                              '%s/images/images_g_%d.png'%(root_out,epoch),\
                              normalize=True, nrow=examples, range=(-1.0, 1.0))
    """
