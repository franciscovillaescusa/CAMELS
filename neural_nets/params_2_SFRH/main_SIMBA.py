import numpy as np
import sys, os, time
import torch 
import torch.nn as nn
import torch.backends.cudnn as cudnn
sys.path.append('../')
import data as data
import architecture as architecture

##################################### INPUT ##########################################
root_in      = '/mnt/ceph/users/camels'
root_out     = '/mnt/ceph/users/camels/Results/neural_nets/params_2_SFRH/SIMBA'
sim          = 'SIMBA'
seed         = 1
realizations = 1000
bins_SFRH    = 100

# architecture parameters
h1 = 1000
h2 = 1000
h3 = 100
h4 = 100
dr = 0.0

# training parameters
batch_size = 32
lr         = 1e-4
epochs     = 100000
wd         = 5e-4

# name of the output files
name   = '2hd_1000_1000_0.0_5e-4'
fout   = '%s/losses/%s.txt'%(root_out,name)
fmodel = '%s/models/%s.pt'%(root_out,name)
######################################################################################

# use GPUs if available
if torch.cuda.is_available():
    print("CUDA Available")
    device = torch.device('cuda')
else: 
    print("CUDA Not Available")
    device = torch.device('cpu')
cudnn.benchmark = True   

# define loss function
criterion = nn.MSELoss() 

# get train, validation, and test sets
print('preparing dataset loaders')
train_loader = data.create_dataset('train', seed, realizations, root_in, bins_SFRH, 
                                   sim, batch_size, root_out)
valid_loader = data.create_dataset('valid', seed, realizations, root_in, bins_SFRH, 
                                   sim, batch_size, root_out)
test_loader  = data.create_dataset('test',  seed, realizations, root_in, bins_SFRH, 
                                   sim, batch_size, root_out)

# define architecture
#model = architecture.model_1hl(6, h1, bins_SFRH, dr)
model = architecture.model_2hl(6, h1, h2, bins_SFRH, dr)
model = architecture.model_3hl(6, h1, h2, h3, bins_SFRH, dr)
model.to(device=device)
network_total_params = sum(p.numel() for p in model.parameters())
print('total number of parameters in the model = %d'%network_total_params)

# define optimizer and scheduler
optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(0.5, 0.999), 
                             weight_decay=wd)	

# load best-model, if it exists
if os.path.exists(fmodel):  
    print('Loading model...')
    model.load_state_dict(torch.load(fmodel))
    model.to(device=device)

# get validation loss
print('Computing initial validation loss')
model.eval()
min_valid_loss, points = 0.0, 0
for params_val, SFRH_val in valid_loader:
    with torch.no_grad():
        params_val = params_val.to(device=device)
        SFRH_val   = SFRH_val.to(device=device)
        SFRH_pred = model(params_val)
        min_valid_loss += criterion(SFRH_pred, SFRH_val).item()*SFRH_val.shape[0]
        points += SFRH_val.shape[0]
min_valid_loss /= points
print('Initial valid loss = %.3e'%min_valid_loss)

# see if results for this model are available
if os.path.exists(fout):  
    dumb = np.loadtxt(fout, unpack=False)
    offset = int(dumb[:,0][-1]+1)
else:  offset = 0

# do a loop over all epochs
start = time.time()
for epoch in range(offset,offset+epochs):
        
    # do training
    train_loss, points = 0.0, 0
    model.train()
    for params_train, SFRH_train in train_loader:
        params_train = params_train.to(device)
        SFRH_train   = SFRH_train.to(device)
        SFRH_pred  = model(params_train)

        loss = criterion(SFRH_pred, SFRH_train)
        train_loss += loss.item()*SFRH_train.shape[0]
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
            params_val = params_val.to(device)
            SFRH_val   = SFRH_val.to(device)
            SFRH_pred = model(params_val)
            valid_loss += criterion(SFRH_pred, SFRH_val).item()*SFRH_val.shape[0]
            points += SFRH_val.shape[0]
    valid_loss /= points

    # do testing
    test_loss, points = 0.0, 0
    model.eval()
    for params_test, SFRH_test in test_loader:
        with torch.no_grad():
            params_test = params_test.to(device)
            SFRH_test   = SFRH_test.to(device)
            SFRH_pred = model(params_test)
            test_loss += criterion(SFRH_pred, SFRH_test).item()*SFRH_test.shape[0]
            points += SFRH_test.shape[0]
    test_loss /= points

    # save model if it is better
    if valid_loss<min_valid_loss:
        #print('saving model...')
        torch.save(model.state_dict(), fmodel)
        min_valid_loss = valid_loss
        print('%03d %.3e %.3e %.3e'%(epoch, train_loss, valid_loss, test_loss))
    
    # save losses to file
    f = open(fout, 'a')
    f.write('%d %.5e %.5e %.5e\n'%(epoch, train_loss, valid_loss, test_loss))
    f.close()
    
stop = time.time()
print('Time take (m):', "{:.4f}".format((stop-start)/60.0))
