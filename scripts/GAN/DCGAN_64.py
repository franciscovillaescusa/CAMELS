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
root_in  = '/mnt/ceph/users/camels/Results/GAN'
root_out = '/mnt/ceph/users/camels/Results/GAN'

lr_D = 1e-5
lr_G = 1e-4
seed = 1   #mainly for the generated images
grid = 64

BATCH_SIZE = 128 
Z_DIM      = 100
G_HIDDEN   = 128
D_HIDDEN   = 80
EPOCH_NUM  = 1000
REAL_LABEL = 1
FAKE_LABEL = 0
######################################################################################

# use GPUs if available
GPU = torch.cuda.is_available()
device = torch.device("cuda" if GPU else "cpu")
print('GPU:',GPU)
print('Training on',device)
cudnn.benchmark = True      # May train faster but cost more memory

# initialize random number generator
if seed is None:  seed = np.random.randint(1, 10000)
np.random.seed(seed)
torch.manual_seed(seed)
if GPU:  torch.cuda.manual_seed(seed)

# generate points in latent space to generate test images
viz_noise = torch.randn(BATCH_SIZE, Z_DIM, 1, 1, device=device)

# define loss function
criterion = nn.BCELoss()

# get the data
train_loader = data.create_train_set(root_in, grid, BATCH_SIZE, verbose=True)

# define generator and discriminator networks
netG = architecture.Generator_64(Z_DIM, G_HIDDEN).to(device)
netG.apply(architecture.weights_init)
netD = architecture.Discriminator_64(D_HIDDEN).to(device)
netD.apply(architecture.weights_init)

# load best-models, if they exists
netG.load_state_dict(torch.load('%s/models_64/Net_Gen_808.pt'%root_out))
netD.load_state_dict(torch.load('%s/models_64/Net_Dis_808.pt'%root_out))

# define the optimizers
optimizerD = optim.Adam(netD.parameters(), lr=lr_D, betas=(0.5, 0.999))
#optimizerD = optim.SGD(netD.parameters(), lr=lr_D, momentum=0.9)
optimizerG = optim.Adam(netG.parameters(), lr=lr_G, betas=(0.5, 0.999))


# do a loop over all the epochs
for epoch in range(808,2000):
    
    # do a loop over all maps
    for i,true_maps in enumerate(train_loader):

        # find the number of maps in this batch
        num_maps = true_maps.shape[0]

        true_maps = true_maps.to(device)
        real_label = torch.full((num_maps,), REAL_LABEL, device=device)
        fake_label = torch.full((num_maps,), FAKE_LABEL, device=device)

        if epoch==0 and i==0:
            vutils.save_image(true_maps, '%s/images_64/real_samples.png'%root_out, 
                              normalize=True, nrow=16, range=(-1.0,1.0))

        # Update D with real data
        netD.zero_grad()
        y_real = netD(true_maps)
        loss_D_real = criterion(y_real, real_label)
        loss_D_real.backward()

        # Update D with fake data
        z_noise = torch.randn(num_maps, Z_DIM, 1, 1, device=device)
        fake_maps = netG(z_noise)
        y_fake = netD(fake_maps.detach())
        loss_D_fake = criterion(y_fake, fake_label)
        loss_D_fake.backward()
        optimizerD.step()

        # Update G with fake data
        netG.zero_grad()
        y_fake_r = netD(fake_maps)
        loss_G = criterion(y_fake_r, real_label)
        loss_G.backward()
        optimizerG.step()

    # print info about losses and save them to file
    print('Epoch {} loss_D_real: {:.4f} loss_D_fake: {:.4f} loss_G: {:.4f}'\
          .format(epoch, loss_D_real.mean().item(), loss_D_fake.mean().item(),
                  loss_G.mean().item()))
    f = open('%s/losses/loss_64.txt'%root_out, 'a')
    f.write('%d %.3e %.3e %.3e\n'%(epoch,loss_D_real.mean().item(),
                                   loss_D_fake.mean().item(), loss_G.mean().item()))
    f.close()
        
    # save images from generator to file
    with torch.no_grad():
        viz_sample = netG(viz_noise)[:49]
        vutils.save_image(viz_sample, '%s/images_64/fake_samples_%d.png'\
                          %(root_out,epoch), normalize=True, nrow=7, range=(-1.0, 1.0))

    # save networks
    torch.save(netG.state_dict(), '%s/models_64/Net_Gen_%d.pt'%(root_out,epoch))
    torch.save(netD.state_dict(), '%s/models_64/Net_Dis_%d.pt'%(root_out,epoch))

