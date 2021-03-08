import torch
from torch import nn
from torch.nn import functional as F


class Decoder(nn.Module):
    def __init__(self, encoder_hidden_state: torch.Tensor, outputnum_blocks: int=1):
        super(Decoder, self).__init__()
        return
        
    def forward(self, X: torch.Tensor):
        pass