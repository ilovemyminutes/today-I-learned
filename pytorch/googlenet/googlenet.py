import torch
from torch import nn


class GoogLeNet(nn.Module):

    def __init__(self):
        super(GoogLeNet, self).__init__()
        self.conv_1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=7, stride=2, padding=3)
        self.pooling_1 = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.reduce_1 = nn.Conv2d(in_channels=64, out_channels=1, kernel_size=1, stride=1)
        self.conv_2 = nn.Conv2d(in_channels=64, out_channels=192, kernel_size=3, stride=1, padding=1)
        self.pooling_2 = nn.MaxPool2d(kernel_size=3, stride=1, padding=1)

    def forward(input):
        pass
