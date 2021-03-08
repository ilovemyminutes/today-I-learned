import math

import torch
from torch import nn
from torch.nn import functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int, mask: bool = False):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.d_k = d_model // num_heads
        self.mask = mask
        return

    def forward(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor
    ) -> torch.Tensor:
        """Query, Key, Value 텐서를 입력 받아 Attention 텐서를 리턴. mask 인스턴스가 True일 경우 Masked Multi-headed Attention을 수행

        Args:
            query (torch.Tensor): Query 텐서. (batch_size, max_len, hidden_dim)
            key (torch.Tensor): Key 텐서. (batch_size, max_len, hidden_dim)
            value (torch.Tensor): Value 텐서. (batch_size, max_len, hidden_dim)

        Returns:
            torch.Tensor: Attention 텐서. (batch_size, max_len, hidden_dim)
        """
        self.batch_size = query.size(0)
        query = query.view(self.batch_size, -1, self.num_heads, self.d_k)
        key = key.view(self.batch_size, -1, self.num_heads, self.d_k)
        value = value.view(self.batch_size, -1, self.num_heads, self.d_k)

        query = query.transpose(1, 2)
        key = key.transpose(1, 2)
        value = value.transpose(1, 2)

        attention = self.get_self_attention(query, key, value)

        return attention

    def get_self_attention(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor
    ) -> torch.Tensor:
        """attention 텐서를 리턴. multi-head attention 수행 후, aggregate된 최종 attention 텐서를 리턴

        Args:
            query (torch.Tensor): Query 텐서. (batch_size, num_heads, max_len, d_k)
            key (torch.Tensor): Key 텐서. (batch_size, num_heads, max_len, d_k)
            value (torch.Tensor): Value 텐서. (batch_size, num_heads, max_len, d_k)

        Returns:
            torch.Tensor: Attention 텐서. (batch_size, max_len, d_model)
        """
        attention_raw = F.softmax(
            torch.matmul(query, key.transpose(-1, -2)) / math.sqrt(self.d_model), dim=-1
        )
        if self.mask:
            max_len = attention_raw.shape[-1]
            mask = torch.triu(torch.ones(max_len, max_len), diagonal=1).bool()
            attention_raw = F.softmax(
                attention_raw.masked_fill(mask=mask, value=float("-inf")), dim=-1
            )

        attention = torch.matmul(attention_raw, value).view(
            self.batch_size, -1, self.d_model
        )
        return attention
