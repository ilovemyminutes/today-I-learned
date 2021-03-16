from collections import OrderedDict

import torch
from torch import nn


class ResNet(nn.Module):
    def __init__(self):
        super(ResNet, self).__init__()
        self.layers = nn.Sequential(
            OrderedDict([
                ('conv1', nn.Conv2d(in_channels=3, out_channels=64, kernel_size=7, stride=2, padding=(3, 3), bias=False)),
                ('bn1', nn.BatchNorm2d(num_features=64, eps=1e-5, momentum=.1, affine=True, track_running_stats=True)),
                ('relu', nn.ReLU(inplace=True)),
                ('maxpool', nn.MaxPool2d(kernel_size=3, stride=2, padding=1, dilation=1, ceil_mode=False)),
                ('layer1', self.layer1),
                ('layer2', self.layer2),
                ('layer3', self.layer3),
                ('layer4', self.layer4),
            ])
        )
        self.avgpool = nn.AdaptiveAvgPool2d(output_size=(1,1))
        self.fc = nn.Linear(in_features=512, out_features=2, bias=True)

    def forward(self, input):
        output = self.layers(input)
        output = self.avgpool(output)
        output = output.view(output.size(0), -1)
        output = self.fc(output)
        return output

    @property
    def layer1(self):
        basicblocks = [BasicBlock(in_channels=64, out_channels=64) for _ in range(2)]
        layers = nn.Sequential()
        for idx in range(len(basicblocks)):
            layers.add_module(name=f'{idx}', module=basicblocks[idx])
        return layers
    
    @property
    def layer2(self):
        basicblock0 = BasicBlock(in_channels=64, out_channels=128, downsample=True)
        basicblock1 = BasicBlock(in_channels=128, out_channels=128)
        layers = nn.Sequential(OrderedDict([('0', basicblock0), ('1', basicblock1)]))
        return layers
    
    @property
    def layer3(self):
        basicblock0 = BasicBlock(in_channels=128, out_channels=256, downsample=True)
        basicblock1 = BasicBlock(in_channels=256, out_channels=256)
        layers = nn.Sequential(OrderedDict([('0', basicblock0), ('1', basicblock1)]))
        return layers

    @property
    def layer4(self):
        basicblock0 = BasicBlock(in_channels=256, out_channels=512, downsample=True)
        basicblock1 = BasicBlock(in_channels=512, out_channels=512, downsample=True)
        layers = nn.Sequential(OrderedDict([('0', basicblock0), ('1', basicblock1)]))
        return layers

class BasicBlock(nn.Module):
    def __init__(self, in_channels: int=64, out_channels: int=128, downsample: bool=False):
        super(BasicBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        self.bn1 = nn.BatchNorm2d(num_features=out_channels, eps=1e-5, momentum=.1, affine=True, track_running_stats=True)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(in_channels=out_channels, out_channels=out_channels, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        if downsample:
            self.downsample = nn.Sequential(
                OrderedDict([
                        ('0', nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=(1,1), stride=(1,1), bias=False)),
                        ('1', nn.BatchNorm2d(num_features=out_channels, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True))
                        ])
                )
        else:
            self.downsample = None

    def forward(self, input) -> torch.Tensor:
        residual = input

        output = self.conv1(input)
        output = self.bn1(output)
        output = self.relu(output)
        output = self.conv2(output)

        # downsampling
        if self.downsample is not None:            
            residual = self.downsample(input)

        output += residual
        output = self.relu(output)
        return output