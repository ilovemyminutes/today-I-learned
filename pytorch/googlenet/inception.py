import torch
from torch import nn

class Inception(nn.Module):
    def __init__(self, in_channels: int, reduction: bool=True, auxiliary: bool=False):
        super(Inception, self).__init__()
        
        self.branch_1 = nn.Conv2d(in_channels=in_channels, out_channels=64, kernel_size=1)
        self.branch_2 = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=1, kernel_size=1),
            nn.Conv2d(in_channels=3, out_channels=123)
        )
        
        self.conv_3 = nn.Conv2d(in_channels=in_channels, out_channels=1, kernel_size=1)

        self.pooling_1 = nn.MaxPool2d(kernel_size=3, stride=1)

    def forward(self, input):
        pass

    
