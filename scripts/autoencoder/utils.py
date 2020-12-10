import numpy as np
import torch


# This function save to a file the mean, std, min and max of the gradients of the 
# different layers
def save_gradients(f_gradients, model):
  
    f = open(f_gradients, 'w')

    # do a loop over all layers
    count = 0
    for name, param in model.named_parameters():
        if (param.requires_grad) and ("bias" not in name) and (param.grad is not None):
            f.write('%d %s %.5e %.5e %.5e %.5e\n'%(count, name, 
                torch.mean(param.grad).item(), torch.std(param.grad).item(),
                torch.min(param.grad).item(),  torch.max(param.grad).item()))
            count +=1

    f.close()
