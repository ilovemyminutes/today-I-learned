import torch
from torch import nn
from torch.nn import functional as F


class PositionalEncoder(nn.Mudule):
    def __init__(self):
        super(PositionalEncoder, self).__init__()

    def forward(self, hidden_dim):
        pass