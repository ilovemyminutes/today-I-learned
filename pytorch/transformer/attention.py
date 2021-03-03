import math

import torch
from torch import nn
from torch.nn import functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.hidden_dim = hidden_dim
        self.hidden_dim_head = hidden_dim // num_heads
        return

    def forward(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor
    ) -> torch.Tensor:
        """Query, Key, Value 행렬을 입력 받아 Attention 행렬을 리턴

        Args:
            query (torch.Tensor): Query 행렬. (batch_size, max_len, hidden_dim)
            key (torch.Tensor): Key 행렬. (batch_size, max_len, hidden_dim)
            value (torch.Tensor): Value 행렬. (batch_size, max_len, hidden_dim)

        Returns:
            torch.Tensor: Attention 행렬. (batch_size, max_len, hidden_dim)
        """
        self.batch_size = query.size(0)
        query = query.view(
            self.batch_size, -1, self.num_heads, self.hidden_dim_head
        )
        key = key.view(self.batch_size, -1, self.num_heads, self.hidden_dim_head)
        value = value.view(self.batch_size, -1, self.num_heads, self.hidden_dim_head)

        query = query.transpose(1, 2)
        key = key.transpose(1, 2)
        value = value.transpose(1, 2)

        attention = self.get_self_attention(query, key, value)

        return attention

    def get_self_attention(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor
    ) -> torch.Tensor:
        """attention 행렬을 리턴. multi-head attention 수행 후, aggregate된 최종 attention 행렬을 리턴

        Args:
            query (torch.Tensor): Query 행렬. (batch_size, num_heads, max_len, hidden_dim_head)
            key (torch.Tensor): Key 행렬. (batch_size, num_heads, max_len, hidden_dim_head)
            value (torch.Tensor): Value 행렬. (batch_size, num_heads, max_len, hidden_dim_head)

        Returns:
            torch.Tensor: Attention 행렬. (batch_size, max_len, hidden_dim)
        """    
        attention_raw = F.softmax(
            torch.matmul(query, key.transpose(-1, -2)) / math.sqrt(self.hidden_dim)
        )
        attention = torch.matmul(attention_raw, value).view(
            self.batch_size, -1, self.hidden_dim
        )
        return attention