import torch
from torch import nn
from torch.nn import functional as F

from transformer.attention import MultiHeadAttention


class Encoder(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int, num_blocks: int):

        super(Encoder, self).__init__()

        # Layers for Query, Key, Value matrices
        self.w_query = nn.Linear(
            in_features=hidden_dim, out_features=hidden_dim
        ) 
        self.w_key = nn.Linear(in_features=hidden_dim, out_features=hidden_dim)
        self.w_value = nn.Linear(
            in_features=hidden_dim, out_features=hidden_dim
        )

        # multi-head attention layer
        self.attention = MultiHeadAttention(
            hidden_dim=hidden_dim, num_heads=num_heads
        ) 

        self.linear = nn.Linear(in_features=hidden_dim, out_features=hidden_dim)

    def forward(self, X: torch.Tensor):
        """
        Args:
            data (torch.Tensor): Positional Encoding 벡터가 더해진 임베딩 벡터. (batch_size, max_len, hidden_dim)
        """
        residual = X
        query = self.w_query(X)
        key = self.w_key(X)
        value = self.w_value(X)
        attention = self.attention(query, key, value)

        return