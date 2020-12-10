import torch
import torch.nn as nn

def weights_init(m):
    """custom weights initialization
    """
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        m.weight.data.normal_(0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        m.weight.data.normal_(1.0, 0.02)
        m.bias.data.fill_(0)


####################################################################################
####################################################################################
class autoencoder_64a(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64a, self).__init__()
        
        ##### first, contracting part #####
        # input: 1x64x64 ---------------> output: hiddenx32x32
        self.C1 = nn.Conv2d(1,         hidden, kernel_size=4, stride=2, padding=1, 
                            bias=True)
        self.B1 = nn.BatchNorm2d(hidden)
        # input: hiddenx32x32 ----------> output: 2*hiddenx16x16
        self.C2 = nn.Conv2d(hidden,   2*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B2 = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 --------> output: 4*hiddenx8x8
        self.C3 = nn.Conv2d(2*hidden, 4*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B3 = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ----------> output: 8*hiddenx4x4
        self.C4 = nn.Conv2d(4*hidden, 8*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B4 = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ----------> output: 500x1x1
        self.C5 = nn.Conv2d(8*hidden, BN_dim, kernel_size=6, stride=1, padding=1,
                            bias=True)
        self.B5 = nn.BatchNorm2d(BN_dim)

        ##### bottleneck #####
        self.FC1  = nn.Linear(500,     BN_dim)  #from C5 to bottleneck
        self.FC2  = nn.Linear(BN_dim,  500)     #from bottleneck to C6

        ##### second, expanding part #####
        # input: 500x1x1 ------------> output: 8*hiddenx4x4
        self.C6  = nn.ConvTranspose2d(BN_dim, 8*hidden, kernel_size=4, stride=1, 
                                      padding=0, bias=True)
        self.B6  = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ------------> output: 4*hiddenx8x8
        self.C7  = nn.ConvTranspose2d(8*hidden, 4*hidden, kernel_size=4, stride=2, 
                                      padding=1, bias=True)
        self.B7  = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ------------> output: 2*hiddenx16x16
        self.C8  = nn.ConvTranspose2d(4*hidden, 2*hidden, kernel_size=4, stride=2,
                                      padding=1, bias=True)
        self.B8  = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 ----------> output: hiddenx32x32
        self.C9 = nn.ConvTranspose2d(2*hidden, 1*hidden,  kernel_size=4, stride=2,
                                     padding=1, bias=True)
        self.B9 = nn.BatchNorm2d(hidden)
        # input: 1*hiddenx32x32 ----------> output: 1x64x64
        self.C10 = nn.ConvTranspose2d(hidden,  1,         kernel_size=4, stride=2,
                                      padding=1, bias=True)


        self.dropout   = nn.Dropout(p=0.5)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = self.LeakyReLU(self.C1(image))
        x = self.LeakyReLU(self.B2(self.C2(x)))
        x = self.LeakyReLU(self.B3(self.C3(x)))
        x = self.LeakyReLU(self.B4(self.C4(x)))
        #x = self.LeakyReLU(self.B5(self.C5(x)))
        x = self.LeakyReLU(self.C5(x))
        #inner_cnn = image.shape
        #x = x.view(inner_cnn[0],-1)

        #x = self.LeakyReLU(self.FC1(x))
        #x = self.LeakyReLU(self.FC2(x))

        #x = x.view(inner_cnn[0],inner_cnn[1],inner_cnn[2],inner_cnn[3])
        #x = self.LeakyReLU(self.B6(self.C6(x)))
        x = self.LeakyReLU(self.C6(x))
        x = self.LeakyReLU(self.B7(self.C7(x)))
        x = self.LeakyReLU(self.B8(self.C8(x)))
        x = self.LeakyReLU(self.B9(self.C9(x)))
        x = self.tanh(self.C10(x))

        return x
####################################################################################
####################################################################################

####################################################################################
####################################################################################
class autoencoder_64c(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64c, self).__init__()
        
        ##### first, contracting part #####
        # input: 1x64x64 ---------------> output: hiddenx32x32
        self.C1 = nn.Conv2d(1,         hidden, kernel_size=4, stride=2, padding=1, 
                            bias=True)
        self.B1 = nn.BatchNorm2d(hidden)
        # input: hiddenx32x32 ----------> output: 2*hiddenx16x16
        self.C2 = nn.Conv2d(hidden,   2*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B2 = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 --------> output: 4*hiddenx8x8
        self.C3 = nn.Conv2d(2*hidden, 4*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B3 = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ----------> output: 8*hiddenx4x4
        self.C4 = nn.Conv2d(4*hidden, 8*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B4 = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ----------> output: 500x1x1
        self.C5 = nn.Conv2d(8*hidden, BN_dim, kernel_size=6, stride=1, padding=1,
                            bias=True)
        self.B5 = nn.BatchNorm2d(BN_dim)

        ##### bottleneck #####
        self.FC1  = nn.Linear(500,     BN_dim)  #from C5 to bottleneck
        self.FC2  = nn.Linear(BN_dim,  500)     #from bottleneck to C6

        ##### second, expanding part #####
        # input: 500x1x1 ------------> output: 8*hiddenx4x4
        self.C6  = nn.ConvTranspose2d(BN_dim, 8*hidden, kernel_size=4, stride=1, 
                                      padding=0, bias=True)
        self.B6  = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ------------> output: 4*hiddenx8x8
        self.C7  = nn.ConvTranspose2d(8*hidden, 4*hidden, kernel_size=4, stride=2, 
                                      padding=1, bias=True)
        self.B7  = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ------------> output: 2*hiddenx16x16
        self.C8  = nn.ConvTranspose2d(4*hidden, 2*hidden, kernel_size=4, stride=2,
                                      padding=1, bias=True)
        self.B8  = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 ----------> output: hiddenx32x32
        self.C9 = nn.ConvTranspose2d(2*hidden, 1*hidden,  kernel_size=4, stride=2,
                                     padding=1, bias=True)
        self.B9 = nn.BatchNorm2d(hidden)
        # input: 1*hiddenx32x32 ----------> output: 1x64x64
        self.C10 = nn.ConvTranspose2d(hidden,  1,         kernel_size=4, stride=2,
                                      padding=1, bias=True)


        self.dropout   = nn.Dropout(p=0.5)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = self.LeakyReLU(self.C1(image))
        x = self.LeakyReLU(self.C2(x))
        x = self.LeakyReLU(self.C3(x))
        x = self.LeakyReLU(self.C4(x))
        x = self.LeakyReLU(self.C5(x))
        #inner_cnn = x.shape
        #x = x.view(inner_cnn[0],-1)

        #x = self.LeakyReLU(self.FC1(x))
        #x = self.LeakyReLU(self.FC2(x))

        #x = x.view(inner_cnn[0],inner_cnn[1],inner_cnn[2],inner_cnn[3])
        #x = self.LeakyReLU(self.B6(self.C6(x)))
        x = self.LeakyReLU(self.C6(x))
        x = self.LeakyReLU(self.C7(x))
        x = self.LeakyReLU(self.C8(x))
        x = self.LeakyReLU(self.C9(x))
        x = self.tanh(self.C10(x))

        return x
####################################################################################
####################################################################################

####################################################################################
####################################################################################
class autoencoder_64d(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64d, self).__init__()
        
        ##### first, contracting part #####
        # input: 1x64x64 ---------------> output: hiddenx32x32
        self.C1 = nn.Conv2d(1,         hidden, kernel_size=4, stride=2, padding=1, 
                            bias=True)
        self.B1 = nn.BatchNorm2d(hidden)
        # input: hiddenx32x32 ----------> output: 2*hiddenx16x16
        self.C2 = nn.Conv2d(hidden,   2*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B2 = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 --------> output: 4*hiddenx8x8
        self.C3 = nn.Conv2d(2*hidden, 4*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B3 = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ----------> output: 8*hiddenx4x4
        self.C4 = nn.Conv2d(4*hidden, 8*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B4 = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ----------> output: 1000x1x1
        self.C5 = nn.Conv2d(8*hidden, 1000, kernel_size=6, stride=1, padding=1,
                            bias=True)
        self.B5 = nn.BatchNorm2d(BN_dim)

        ##### bottleneck #####
        self.FC1  = nn.Linear(1000,    500)   
        self.FC2  = nn.Linear(500,     250)   
        self.FC3  = nn.Linear(250,     BN_dim)   
        self.FC4  = nn.Linear(BN_dim,  250)   
        self.FC5  = nn.Linear(250,     500)   
        self.FC6  = nn.Linear(500,     1000)   

        ##### second, expanding part #####
        # input: 1000x1x1 ------------> output: 8*hiddenx4x4
        self.C6  = nn.ConvTranspose2d(1000, 8*hidden, kernel_size=4, stride=1, 
                                      padding=0, bias=True)
        self.B6  = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ------------> output: 4*hiddenx8x8
        self.C7  = nn.ConvTranspose2d(8*hidden, 4*hidden, kernel_size=4, stride=2, 
                                      padding=1, bias=True)
        self.B7  = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ------------> output: 2*hiddenx16x16
        self.C8  = nn.ConvTranspose2d(4*hidden, 2*hidden, kernel_size=4, stride=2,
                                      padding=1, bias=True)
        self.B8  = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 ----------> output: hiddenx32x32
        self.C9 = nn.ConvTranspose2d(2*hidden, 1*hidden,  kernel_size=4, stride=2,
                                     padding=1, bias=True)
        self.B9 = nn.BatchNorm2d(hidden)
        # input: 1*hiddenx32x32 ----------> output: 1x64x64
        self.C10 = nn.ConvTranspose2d(hidden,  1,         kernel_size=4, stride=2,
                                      padding=1, bias=True)


        self.dropout   = nn.Dropout(p=0.5)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = self.LeakyReLU(self.C1(image))
        x = self.LeakyReLU(self.B2(self.C2(x)))
        x = self.LeakyReLU(self.B3(self.C3(x)))
        x = self.LeakyReLU(self.B4(self.C4(x)))
        x = self.LeakyReLU(self.C5(x))
        inner_cnn = x.shape
        x = x.view(inner_cnn[0],-1)

        x = self.LeakyReLU(self.FC1(x))
        x = self.LeakyReLU(self.FC2(x))
        x = self.LeakyReLU(self.FC3(x))
        x = self.LeakyReLU(self.FC4(x))
        x = self.LeakyReLU(self.FC5(x))
        x = self.LeakyReLU(self.FC6(x))

        x = x.view(inner_cnn[0],inner_cnn[1],inner_cnn[2],inner_cnn[3])
        x = self.LeakyReLU(self.C6(x))
        x = self.LeakyReLU(self.B7(self.C7(x)))
        x = self.LeakyReLU(self.B8(self.C8(x)))
        x = self.LeakyReLU(self.B9(self.C9(x)))
        x = self.tanh(self.C10(x))

        return x
####################################################################################
####################################################################################

####################################################################################
####################################################################################
class autoencoder_64e(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64e, self).__init__()
        
        ##### first, contracting part #####
        # input: 1x64x64 ---------------> output: hiddenx16x16
        self.C1 = nn.Conv2d(1,         hidden, kernel_size=6, stride=4, padding=1, 
                            bias=True)
        self.B1 = nn.BatchNorm2d(hidden)
        # input: hiddenx16x16 ----------> output: 2*hiddenx4x4
        self.C2 = nn.Conv2d(hidden,   2*hidden, kernel_size=6, stride=4, padding=1,
                            bias=True)
        self.B2 = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx4x4 --------> output: BN_dimx1x1
        self.C3 = nn.Conv2d(2*hidden, BN_dim, kernel_size=6, stride=4, padding=1,
                            bias=True)
        self.B3 = nn.BatchNorm2d(4*hidden)

        ##### bottleneck #####
        self.FC1  = nn.Linear(500,     BN_dim)  #from C5 to bottleneck
        self.FC2  = nn.Linear(BN_dim,  500)     #from bottleneck to C6

        ##### second, expanding part #####
        # input: BN_dimx1x1 ------------> output: 2*hiddenx4x4
        self.C6  = nn.ConvTranspose2d(BN_dim, 2*hidden, kernel_size=4, stride=1, 
                                      padding=0, bias=True)
        self.B6  = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx4x4 ------------> output: hiddenx16x16
        self.C7  = nn.ConvTranspose2d(2*hidden, 1*hidden, kernel_size=6, stride=4, 
                                      padding=1, bias=True)
        self.B7  = nn.BatchNorm2d(1*hidden)
        # input: 2*hiddenx16x16 ------------> output: 1x64x64
        self.C8  = nn.ConvTranspose2d(1*hidden, 1,        kernel_size=6, stride=4,
                                      padding=1, bias=True)

        self.dropout   = nn.Dropout(p=0.5)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = self.LeakyReLU(self.C1(image))
        x = self.LeakyReLU(self.B2(self.C2(x)))
        x = self.LeakyReLU(self.C3(x))

        #inner_cnn = x.shape
        #x = x.view(inner_cnn[0],-1)

        #x = self.LeakyReLU(self.FC1(x))
        #x = self.LeakyReLU(self.FC2(x))

        #x = x.view(inner_cnn[0],inner_cnn[1],inner_cnn[2],inner_cnn[3])
        #x = self.LeakyReLU(self.B6(self.C6(x)))

        x = self.LeakyReLU(self.C6(x))
        x = self.LeakyReLU(self.B7(self.C7(x)))
        x = self.tanh(self.C8(x))

        return x
####################################################################################
####################################################################################

####################################################################################
####################################################################################
class autoencoder_64f(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64f, self).__init__()
        
        ##### first, contracting part #####
        # input: 1x64x64 ---------------> output: hiddenx16x16
        self.C1 = nn.Conv2d(1,         hidden, kernel_size=6, stride=4, padding=1, 
                            bias=True)
        self.B1 = nn.BatchNorm2d(hidden)
        # input: hiddenx16x16 ----------> output: 2*hiddenx4x4
        self.C2 = nn.Conv2d(hidden,   2*hidden, kernel_size=6, stride=4, padding=1,
                            bias=True)
        self.B2 = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx4x4 --------> output: BN_dimx1x1
        self.C3 = nn.Conv2d(2*hidden, BN_dim, kernel_size=6, stride=4, padding=1,
                            bias=True)
        self.B3 = nn.BatchNorm2d(BN_dim)

        ##### bottleneck #####
        self.FC1  = nn.Linear(500,     BN_dim)  #from C5 to bottleneck
        self.FC2  = nn.Linear(BN_dim,  500)     #from bottleneck to C6

        ##### second, expanding part #####
        # input: BN_dimx1x1 ------------> output: 2*hiddenx4x4
        self.C6  = nn.ConvTranspose2d(BN_dim, 2*hidden, kernel_size=4, stride=1, 
                                      padding=0, bias=True)
        self.B6  = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx4x4 ------------> output: hiddenx16x16
        self.C7  = nn.ConvTranspose2d(2*hidden, 1*hidden, kernel_size=6, stride=4, 
                                      padding=1, bias=True)
        self.B7  = nn.BatchNorm2d(1*hidden)
        # input: 2*hiddenx16x16 ------------> output: 1x64x64
        self.C8  = nn.ConvTranspose2d(1*hidden, 1,        kernel_size=6, stride=4,
                                      padding=1, bias=True)

        self.dropout   = nn.Dropout(p=0.5)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = self.LeakyReLU(self.B1(self.C1(image)))
        x = self.LeakyReLU(self.B2(self.C2(x)))
        x = self.LeakyReLU(self.B3(self.C3(x)))

        #inner_cnn = x.shape
        #x = x.view(inner_cnn[0],-1)

        #x = self.LeakyReLU(self.FC1(x))
        #x = self.LeakyReLU(self.FC2(x))

        #x = x.view(inner_cnn[0],inner_cnn[1],inner_cnn[2],inner_cnn[3])
        #x = self.LeakyReLU(self.B6(self.C6(x)))

        x = self.LeakyReLU(self.B6(self.C6(x)))
        x = self.LeakyReLU(self.B7(self.C7(x)))
        x = self.tanh(self.C8(x))

        return x
####################################################################################
####################################################################################

####################################################################################
####################################################################################
class autoencoder_64g(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64g, self).__init__()
        
        ##### first, contracting part #####
        # input: 1x64x64 ---------------> output: hiddenx16x16
        self.C1 = nn.Conv2d(1,         hidden, kernel_size=6, stride=4, padding=1, 
                            bias=True)
        self.B1 = nn.BatchNorm2d(hidden)
        # input: hiddenx16x16 ----------> output: 2*hiddenx4x4
        self.C2 = nn.Conv2d(hidden,   2*hidden, kernel_size=6, stride=4, padding=1,
                            bias=True)
        self.B2 = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx4x4 --------> output: BN_dimx1x1
        self.C3 = nn.Conv2d(2*hidden, BN_dim, kernel_size=6, stride=4, padding=1,
                            bias=True)
        self.B3 = nn.BatchNorm2d(BN_dim)

        ##### bottleneck #####
        self.FC1  = nn.Linear(500,     BN_dim)  #from C5 to bottleneck
        self.FC2  = nn.Linear(BN_dim,  500)     #from bottleneck to C6

        ##### second, expanding part #####
        # input: BN_dimx1x1 ------------> output: 2*hiddenx4x4
        self.C6  = nn.ConvTranspose2d(BN_dim, 2*hidden, kernel_size=4, stride=1, 
                                      padding=0, bias=True)
        self.B6  = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx4x4 ------------> output: hiddenx16x16
        self.C7  = nn.ConvTranspose2d(2*hidden, 1*hidden, kernel_size=6, stride=4, 
                                      padding=1, bias=True)
        self.B7  = nn.BatchNorm2d(1*hidden)
        # input: 2*hiddenx16x16 ------------> output: 1x64x64
        self.C8  = nn.ConvTranspose2d(1*hidden, 1,        kernel_size=6, stride=4,
                                      padding=1, bias=True)

        self.dropout   = nn.Dropout(p=0.5)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = self.LeakyReLU(self.C1(image))
        x = self.LeakyReLU(self.C2(x))
        x = self.LeakyReLU(self.C3(x))

        x = self.LeakyReLU(self.C6(x))
        x = self.LeakyReLU(self.C7(x))
        x = self.tanh(self.C8(x))

        return x
####################################################################################
####################################################################################

####################################################################################
####################################################################################
class autoencoder_64h(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64h, self).__init__()
        
        ##### first, contracting part #####
        # input: 1x64x64 ---------------> output: hiddenx32x32
        self.C1 = nn.Conv2d(1,         hidden, kernel_size=4, stride=2, padding=1, 
                            bias=True)
        self.B1 = nn.BatchNorm2d(hidden)
        # input: hiddenx32x32 ----------> output: 2*hiddenx16x16
        self.C2 = nn.Conv2d(hidden,   2*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B2 = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 --------> output: 4*hiddenx8x8
        self.C3 = nn.Conv2d(2*hidden, 4*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B3 = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ----------> output: 8*hiddenx4x4
        self.C4 = nn.Conv2d(4*hidden, 8*hidden, kernel_size=4, stride=2, padding=1,
                            bias=True)
        self.B4 = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ----------> output: 1000x1x1
        self.C5 = nn.Conv2d(8*hidden, 1000, kernel_size=6, stride=1, padding=1,
                            bias=True)
        self.B5 = nn.BatchNorm2d(1000)

        ##### bottleneck #####
        self.FC1  = nn.Linear(1000,    BN_dim)  #from C5 to bottleneck
        self.FC2  = nn.Linear(BN_dim,  1000)     #from bottleneck to C6

        ##### second, expanding part #####
        # input: 1000x1x1 ------------> output: 8*hiddenx4x4
        self.C6  = nn.ConvTranspose2d(1000, 8*hidden, kernel_size=4, stride=1, 
                                      padding=0, bias=True)
        self.B6  = nn.BatchNorm2d(8*hidden)
        # input: 8*hiddenx4x4 ------------> output: 4*hiddenx8x8
        self.C7  = nn.ConvTranspose2d(8*hidden, 4*hidden, kernel_size=4, stride=2, 
                                      padding=1, bias=True)
        self.B7  = nn.BatchNorm2d(4*hidden)
        # input: 4*hiddenx8x8 ------------> output: 2*hiddenx16x16
        self.C8  = nn.ConvTranspose2d(4*hidden, 2*hidden, kernel_size=4, stride=2,
                                      padding=1, bias=True)
        self.B8  = nn.BatchNorm2d(2*hidden)
        # input: 2*hiddenx16x16 ----------> output: hiddenx32x32
        self.C9 = nn.ConvTranspose2d(2*hidden, 1*hidden,  kernel_size=4, stride=2,
                                     padding=1, bias=True)
        self.B9 = nn.BatchNorm2d(hidden)
        # input: 1*hiddenx32x32 ----------> output: 1x64x64
        self.C10 = nn.ConvTranspose2d(hidden,  1,         kernel_size=4, stride=2,
                                      padding=1, bias=True)


        self.dropout   = nn.Dropout(p=0.5)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = self.LeakyReLU(self.C1(image))
        x = self.LeakyReLU(self.B2(self.C2(x)))
        x = self.LeakyReLU(self.B3(self.C3(x)))
        x = self.LeakyReLU(self.B4(self.C4(x)))
        x = self.LeakyReLU(self.C5(x))
        dims = x.shape
        x = x.view(dims[0],-1)

        x = self.LeakyReLU(self.FC1(x))
        x = self.LeakyReLU(self.FC2(x))

        x = x.view(dims[0],dims[1],dims[2],dims[3])
        x = self.LeakyReLU(self.C6(x))
        x = self.LeakyReLU(self.B7(self.C7(x)))
        x = self.LeakyReLU(self.B8(self.C8(x)))
        x = self.LeakyReLU(self.B9(self.C9(x)))
        x = self.tanh(self.C10(x))

        return x
####################################################################################
####################################################################################

####################################################################################
####################################################################################
class autoencoder_64b(nn.Module):
    def __init__(self, BN_dim, hidden):
        super(autoencoder_64b, self).__init__()
        
        ##### first, contracting part #####
        self.FC1 = nn.Linear(64*64, 1000)
        self.FC2 = nn.Linear(1000,  500)
        self.FC3 = nn.Linear(500,   250)
        self.FC4 = nn.Linear(250,   BN_dim)
        
        ##### second, expanding part #####
        self.FC5 = nn.Linear(BN_dim, 250)
        self.FC6 = nn.Linear(250,    500)
        self.FC7 = nn.Linear(500,    1000)
        self.FC8 = nn.Linear(1000,   64*64)


        self.dropout   = nn.Dropout(p=0.3)
        self.ReLU      = nn.ReLU()
        self.LeakyReLU = nn.LeakyReLU(0.2)
        self.tanh      = nn.Tanh()

        """
        for m in self.modules():
            if isinstance(m, nn.BatchNorm2d) or isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 1)
            elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight)
        """


    def forward(self, image):
        x = image.view(image.size(0),-1)
        x = self.LeakyReLU(self.FC1(x))
        x = self.LeakyReLU(self.FC2(x))
        x = self.LeakyReLU(self.FC3(x))
        x = self.LeakyReLU(self.FC4(x))
        x = self.LeakyReLU(self.FC5(x))
        x = self.LeakyReLU(self.FC6(x))
        x = self.LeakyReLU(self.FC7(x))
        x = self.tanh(self.FC8(x))
        x = x.view(image.size(0),image.size(1),image.size(2),image.size(3))

        return x
####################################################################################
####################################################################################




# ConvTranspose2d(channels_in, channels_out, kernel, stride, padding)
class Generator_64(nn.Module):
    def __init__(self, Z_DIM, G_HIDDEN):
        super(Generator_64, self).__init__()
        self.main = nn.Sequential(
            # 1st layer (input: 100x1x1 ----> output: 512x4x4)
            nn.ConvTranspose2d(Z_DIM, G_HIDDEN * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(G_HIDDEN * 8),
            nn.ReLU(True),
            # 2nd layer (input: 512x4x4 ----> output: 256x8x8)
            nn.ConvTranspose2d(G_HIDDEN * 8, G_HIDDEN * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(G_HIDDEN * 4),
            nn.ReLU(True),
            # 3rd layer (input: 256x8x8 ----> output: 128x16x16)
            nn.ConvTranspose2d(G_HIDDEN * 4, G_HIDDEN * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(G_HIDDEN * 2),
            nn.ReLU(True),
            # 4th layer (input: 128x16x16 ----> output: 64x32x32)
            nn.ConvTranspose2d(G_HIDDEN * 2, G_HIDDEN, 4, 2, 1, bias=False),
            nn.BatchNorm2d(G_HIDDEN),
            nn.ReLU(True),
            # output layer (input: 64x32x32 ----> 1x64x64)
            nn.ConvTranspose2d(G_HIDDEN, 1, 4, 2, 1, bias=False),
            nn.Tanh()
        )

    def forward(self, input):
        return self.main(input)


#Conv2d(channels_in, channels_out, kernel, stride, padding)
class Discriminator_64(nn.Module):
    def __init__(self, D_HIDDEN):
        super(Discriminator_64, self).__init__()
        self.main = nn.Sequential(
            # 1st layer (input: 1x64x64 ----> output: 64x32x32)
            nn.Conv2d(1, D_HIDDEN, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # 2nd layer (input: 64x32x32 ----> output: 128x16x16)
            nn.Conv2d(D_HIDDEN, D_HIDDEN * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(D_HIDDEN * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # 3rd layer (input: 128x16x16 ----> output: 256x8x8)
            nn.Conv2d(D_HIDDEN * 2, D_HIDDEN * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(D_HIDDEN * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # 4th layer (input: 256x8x8 ----> output: 512x4x4)
            nn.Conv2d(D_HIDDEN * 4, D_HIDDEN * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(D_HIDDEN * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # output layer (input: 512x4x4 ----> output: 1x1x1)
            nn.Conv2d(D_HIDDEN * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid() #Returns a number from 0 to 1: probability
        )

    def forward(self, input):
        return self.main(input).view(-1, 1).squeeze(1)







# ConvTranspose2d(channels_in, channels_out, kernel, stride, padding)
class Generator_128(nn.Module):
    def __init__(self, Z_DIM, G_HIDDEN):
        super(Generator_128, self).__init__()
        self.main = nn.Sequential(
            # 1st layer (input: 100x1x1 ----> output: 512x8x8)
            nn.ConvTranspose2d(Z_DIM, G_HIDDEN * 8, 8, 1, 0, bias=False),
            nn.BatchNorm2d(G_HIDDEN * 8),
            nn.ReLU(True),
            # 2nd layer (input: 512x8x8 ----> output: 256x16x16)
            nn.ConvTranspose2d(G_HIDDEN * 8, G_HIDDEN * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(G_HIDDEN * 4),
            nn.ReLU(True),
            # 3rd layer (input: 256x16x16 ----> output: 128x32x32)
            nn.ConvTranspose2d(G_HIDDEN * 4, G_HIDDEN * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(G_HIDDEN * 2),
            nn.ReLU(True),
            # 4th layer (input: 128x32x32 ----> output: 64x64x64)
            nn.ConvTranspose2d(G_HIDDEN * 2, G_HIDDEN, 4, 2, 1, bias=False),
            nn.BatchNorm2d(G_HIDDEN),
            nn.ReLU(True),
            # output layer (input: 64x64x64 ----> 1x128x128)
            nn.ConvTranspose2d(G_HIDDEN, 1, 4, 2, 1, bias=False),
        )

    def forward(self, input):
        return self.main(input)


#Conv2d(channels_in, channels_out, kernel, stride, padding)
class Discriminator_128(nn.Module):
    def __init__(self, D_HIDDEN):
        super(Discriminator_128, self).__init__()
        self.main = nn.Sequential(
            # 1st layer (input: 1x128x128 ----> output: 64x32x32)
            nn.Conv2d(1, D_HIDDEN, 4, 4, 0, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # 2nd layer (input: 64x32x32 ----> output: 128x16x16)
            nn.Conv2d(D_HIDDEN, D_HIDDEN * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(D_HIDDEN * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # 3rd layer (input: 128x16x16 ----> output: 256x8x8)
            nn.Conv2d(D_HIDDEN * 2, D_HIDDEN * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(D_HIDDEN * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # 4th layer (input: 256x8x8 ----> output: 512x4x4)
            nn.Conv2d(D_HIDDEN * 4, D_HIDDEN * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(D_HIDDEN * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # output layer (input: 512x4x4 ----> output: 1x1x1)
            nn.Conv2d(D_HIDDEN * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid() #Returns a number from 0 to 1: probability
        )

    def forward(self, input):
        return self.main(input).view(-1, 1).squeeze(1)

