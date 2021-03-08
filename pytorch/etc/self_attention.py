import math
from tqdm import tqdm
from typing import List, Union
import numpy as np

import torch
from torch import nn
from torch.nn import functional as F


def padding(data: list) -> Union[List, int]:
    max_len = len(max(data, key=len))
    output = [sample + [0] * (max_len - len(sample)) for sample in tqdm(data)]
    return output, max_len


class MultiheadAttention(nn.Module):
    INF = 1e12

    def __init__(self, d_model: int = 512, num_heads: int = 8):
        super(MultiheadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.d_k = d_model // num_heads

        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)

        self.w_0 = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        batch_size = q.size(0)

        # (batch_size, max_len, d_model) -> (batch_size, max_len, num_heads, d_k) -> (batch_size, num_heads, max_len, d_k)
        q = self.w_q(q).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        k = self.w_k(k).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        v = self.w_v(v).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)

        attn_values = self.self_attention(q, k, v)
        attn_values = attn_values.contiguous().view(batch_size, -1, self.d_model)

        return self.w_0(attn_values)

    def self_attention(self, q, k, v, mask=None):
        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)

        if mask is not None:
            inf = 1e12
            mask = mask.unsqueeze(1)
            attn_scores = attn_scores.masked_fill_(mask == False, -1 * inf)
        attn_dists = F.softmax(attn_scores, dim=-1)

        attn_values = torch.matmul(attn_dists, v)

        return attn_values
