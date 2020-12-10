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

