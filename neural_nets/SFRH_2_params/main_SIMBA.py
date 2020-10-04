import numpy as np
import sys, os, time
import torch 
import torch.nn as nn
sys.path.append('../')
import data as data
import architecture as architecture

##################################### INPUT ##########################################
# data parameters
root_in      = '/mnt/ceph/users/camels'
root_out     = '/mnt/ceph/users/camels/Results/neural_nets/SFRH_2_params/SIMBA'
sim          = 'SIMBA'
seed         = 1
realizations = 1000
bins_SFRH    = 100

# architecture parameters
h1 = 500
h2 = 500
h3 = 500
h4 = 1000
dropout_rate = 0.0

# training parameters
batch_size = 128
lr         = 1e-5
epochs     = 100000
wd         = 2.5e-3

# name of output files
name   = '3hd_500_500_500_0.0_2.5e-3'
fout   = '%s/losses/%s.txt'%(root_out,name)
fmodel = '%s/models/%s.pt'%(root_out,name)
######################################################################################

# use GPUs if available
if torch.cuda.is_available():
    print("CUDA Available")
    device = torch.device('cuda')
else:
    print('CUDA Not Available')
    device = torch.device('cpu')

# define loss function
criterion = nn.MSELoss() 

# get train and validation sets
print('preparing dataset...')
train_loader = data.create_dataset('train', seed, realizations, root_in, bins_SFRH, 
                                   sim, batch_size, root_out)
valid_loader = data.create_dataset('valid', seed, realizations, root_in, bins_SFRH, 
                                   sim, batch_size, root_out)
test_loader  = data.create_dataset('test',  seed, realizations, root_in, bins_SFRH, 
                                   sim, batch_size, root_out)

# define architecture
#model = architecture.model_1hl(bins_SFRH, h1, 6, dropout_rate)
#model = architecture.model_2hl(bins_SFRH, h1, h2, 6, dropout_rate)
model = architecture.model_3hl(bins_SFRH, h1, h2, h3, 6, dropout_rate)
#model = architecture.model_4hl(bins_SFRH, h1, h2, h3, h4, 6, dropout_rate)
model.to(device=device)
network_total_params = sum(p.numel() for p in model.parameters())
print('total number of parameters in the model = %d'%network_total_params)

# define optimizer and scheduler
optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(0.5, 0.999), 
                             weight_decay=wd)	
#scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', 
#                                factor=0.5, patience=25, verbose=True, eps=1e-8)

# load best-model, if it exists
if os.path.exists(fmodel):  
    print('Loading model...')
    model.load_state_dict(torch.load(fmodel))

# get validation loss
print('Computing initial validation loss')
model.eval()
min_valid_loss, points = 0.0, 0
for params_val, SFRH_val in valid_loader:
    with torch.no_grad():
        params_val = params_val.to(device=device)
        SFRH_val   = SFRH_val.to(device=device)
        params_pred = model(SFRH_val)
        min_valid_loss += (criterion(params_pred, params_val).item())*SFRH_val.shape[0]
        points += SFRH_val.shape[0]
min_valid_loss /= points
print('Initial valid loss = %.3e'%min_valid_loss)

# see if results for this model are available
if os.path.exists(fout):  
    dumb = np.loadtxt(fout, unpack=False)
    offset = int(dumb[:,0][-1]+1)
else:   offset = 0

# do a loop over all epochs
start = time.time()
for epoch in range(offset, offset+epochs):
        
    # do training
    train_loss, points = 0.0, 0
    model.train()
    for params_train, SFRH_train in train_loader:
        params_train = params_train.to(device)
        SFRH_train   = SFRH_train.to(device)
        params_pred  = model(SFRH_train)

        loss = criterion(params_pred, params_train)
        train_loss += (loss.item())*SFRH_train.shape[0]
        points += SFRH_train.shape[0]
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    train_loss /= points

    # do validation
    valid_loss, points = 0.0, 0
    model.eval()
    for params_val, SFRH_val in valid_loader:
        with torch.no_grad():
            params_val  = params_val.to(device)
            SFRH_val    = SFRH_val.to(device)
            params_pred = model(SFRH_val)
            valid_loss += (criterion(params_pred, params_val).item())*SFRH_val.shape[0]
            points += SFRH_val.shape[0]
    valid_loss /= points

    # do testing
    test_loss, points = 0.0, 0
    model.eval()
    for params_test, SFRH_test in test_loader:
        with torch.no_grad():
            params_test  = params_test.to(device)
            SFRH_test    = SFRH_test.to(device)
            params_pred = model(SFRH_test)
            test_loss += (criterion(params_pred, params_test).item())*SFRH_test.shape[0]
            points += SFRH_test.shape[0]
    test_loss /= points

    #scheduler.step(valid_loss)

    # save model if it is better
    if valid_loss<min_valid_loss:
        print('saving model...')
        torch.save(model.state_dict(), fmodel)
        min_valid_loss = valid_loss
        print('%03d %.3e %.3e %.3e'%(epoch, train_loss, valid_loss, test_loss))
    
    # save losses to file
    f = open(fout, 'a')
    f.write('%d %.5e %.5e %.5e\n'%(epoch, train_loss, valid_loss, test_loss))
    f.close()
    
stop = time.time()
print('Time take (m):', "{:.4f}".format((stop-start)/60.0))
