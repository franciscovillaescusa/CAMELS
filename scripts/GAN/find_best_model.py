import numpy as np
import sys,os
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torchvision.utils as vutils
import architecture
import Pk_library as PKL

# This routine computes the PDF
def compute_PDF(T_maps, bins_T, mean_T, fout):
    total = T_maps.shape[0]*T_maps.shape[1]*T_maps.shape[2]
    histo = np.histogram(T_maps, bins=bins_T)[0]*1.0/total
    np.savetxt(fout, np.transpose([mean_T, histo]))
    return mean_T, histo

# This routine computes the Pk
def compute_Pk(T_maps, BoxSize, fout):
    Pk = np.zeros((T_maps.shape[0],45), dtype=np.float64)
    for i in range(T_maps.shape[0]):
        Pk_real = PKL.Pk_plane(T_maps[i], BoxSize, MAS='None', threads=1, verbose=False)
        k, Pk[i] = Pk_real.k, Pk_real.Pk
    np.savetxt(fout, np.transpose([k, np.mean(Pk,axis=0), np.std(Pk,axis=0)]))
    return k, np.mean(Pk, axis=0), np.std(Pk, axis=0)

################################### INPUT ############################################
root_in = '/mnt/ceph/users/camels/Results/GAN'
f_maps = 'Images_T.npy'

maps = 15000
grid = 64
bins_T = 300

BATCH_SIZE = 100 
Z_DIM      = 100
G_HIDDEN   = 128
EPOCH_NUM  = 25000
REAL_LABEL = 1
FAKE_LABEL = 0

BoxSize = 25.0*grid/250.0
######################################################################################


# use GPUs if available
GPU = torch.cuda.is_available()
device = torch.device("cuda" if GPU else "cpu")
print('GPU:',GPU)
print('Training on',device)
cudnn.benchmark = True      # May train faster but cost more memory


# do a loop over different models and generate maps; save them to disk
for network_number in np.arange(0,1000,1):

    # get file names and check if they already exists
    fin = '%s/models_64/Net_Gen_%d.pt'%(root_in, network_number)
    fout = '%s/test_64/fake_maps_%d.npy'%(root_in, network_number)
    if os.path.exists(fout):  continue
    if not(os.path.exists(fin)):  continue

    print(network_number)

    # define generator network and load it
    netG = architecture.Generator_64(Z_DIM, G_HIDDEN).to(device)
    netG.load_state_dict(torch.load(fin))

    # define the matrix hosting the fake maps
    fake_maps = np.zeros((maps,64,64), dtype=np.float32)

    batches = maps//BATCH_SIZE
    for i in range(batches):

        start, end = i*BATCH_SIZE, (i+1)*BATCH_SIZE

        # generate points in latent space to generate test images
        z = torch.randn(BATCH_SIZE, Z_DIM, 1, 1, device=device)
        
        with torch.no_grad():
            T_maps = netG(z)
            T_maps = T_maps.squeeze(1)
            fake_maps[start:end,:,:] = T_maps.to('cpu').numpy()
            #vutils.save_image(viz_sample, 'fake_samples_new.png', nrow=16, normalize=True)
            
    # save the maps
    np.save(fout, fake_maps)



################################ SUMMARY STATISTICS ##################################
######################################################################################
# define the variables having the distances
dPDF_min, dPk_min = 1e9, 1e9

# read original maps
T_maps = np.load('%s/%s'%(root_in,f_maps))
T_min = np.min(T_maps); T_min_log = np.log10(T_min)
T_max = np.max(T_maps); T_max_log = np.log10(T_max)
T_maps = T_maps[:,:grid,:grid]
print('%.3e < T < %.3e'%(np.min(T_maps),np.max(T_maps)))

# find the bins in T and their mean values
bins_T = np.logspace(np.log10(T_min), np.log10(T_max), bins_T)
mean_T = 10**(0.5*(np.log10(bins_T[1:]) + np.log10(bins_T[:-1])))

# compute PDF & Pk
f_PDF = '%s/test_64/PDF_T_real_64.txt'%root_in
f_Pk  = '%s/test_64/Pk_T_real_64.txt'%root_in
T_mean, PDF_real     = compute_PDF(T_maps, bins_T, mean_T, f_PDF)
k, Pk_real, dPk_real = compute_Pk(T_maps, BoxSize, f_Pk)

# select the relevant bins and do log10
PDF_real = np.log10(PDF_real[:270]+1.0)
Pk_real  = np.log10(Pk_real[:32])

# do a loop over the different realizations
for network_number in np.arange(0,1000,1):

    # get the name of the inputm map
    fin   = '%s/test_64/fake_maps_%d.npy'%(root_in, network_number)
    f_PDF = '%s/test_64/PDF_T_fake_%d_64.txt'%(root_in, network_number)
    f_Pk  = '%s/test_64/Pk_T_fake_%d_64.txt'%(root_in, network_number)
    if not(os.path.exists(fin)):  continue

    if not(os.path.exists(f_Pk)): 
        # read the maps
        T_maps = np.load(fin)
        T_maps = 10**((T_maps + 1.0)/2.0*(T_max_log - T_min_log) + T_min_log)
        Tmin, Tmax = np.min(T_maps), np.max(T_maps)
        print('%.3e < T < %.3e'%(Tmin,Tmax))

        # compute PDF & Pk
        T_mean, PDF_fake     = compute_PDF(T_maps, bins_T, mean_T, f_PDF)
        k, Pk_fake, dPk_fake = compute_Pk(T_maps, BoxSize, f_Pk)    
    else:
        T_mean, PDF_fake     = np.loadtxt(f_PDF, unpack=True)
        k, Pk_fake, dPk_fake = np.loadtxt(f_Pk,  unpack=True)

    # select the relevant bins and do log10
    PDF_fake = np.log10(PDF_fake[:270]+1.0)
    Pk_fake  = np.log10(Pk_fake[:32])

    dPDF = np.mean((PDF_real - PDF_fake)**2)
    dPk  = np.mean((Pk_real - Pk_fake)**2)
    if dPDF<dPDF_min:
        dPDF_min = dPDF
        print('%d dPDF dPk = %.3e %.3e (minimum dPDF)'%(network_number,dPDF,dPk))
    if dPk<dPk_min:
        dPk_min = dPk
        print('%d dPDF dPk = %.3e %.3e (minimum dPk)'%(network_number,dPDF,dPk))
####################################################################################
####################################################################################
