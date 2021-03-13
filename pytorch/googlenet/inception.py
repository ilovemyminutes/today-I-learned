import torch
from torch import nn

class Inception(nn.Module):
    def __init__(self, reduction: bool=True, auxiliary: bool=False):
        super(Inception, self).__init__()
        self.conv_11 = nn.Conv2d(in_channels=)

    def forward(self, input):
