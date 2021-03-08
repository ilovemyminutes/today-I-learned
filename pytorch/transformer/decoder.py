import torch
from torch import nn
from torch.nn import functional as F


class Decoder(nn.Module):
    def __init__(self, num_blocks: int):
        super(Decoder, self).__init__()
        

    def forward(self, X: torch.Tensor):
        