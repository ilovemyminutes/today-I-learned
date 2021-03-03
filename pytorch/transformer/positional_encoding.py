import torch
from torch import nn
from torch.nn import functional as F


class PositionalEncoder(nn.Module):
    def __init__(self, d_model):
        super(PositionalEncoder, self).__init__()
        self.d_model = d_model

    def forward(self, max_len: int) -> torch.Tensor:
        enc_vector = []
        for k in range(max_len):
            if k % 2 == 0: # 짝수번째 위치
                i = k // 2
                w_k = 1e4 ** (2*i / self.d_model)
                enc_vector.append(w_k)
            else: # 홀수번째 위치
                i = k // 2
                w_k = 1e4 ** (2*i / self.d_model)
                enc_vector.append(w_k)
        enc_vector = torch.tensor(enc_vector).view(1, max_len, 1)
        return enc_vector