import torch
from torch import nn
from torch.nn import functional as F

from attention import MultiHeadAttention


class Encoder(nn.Module):
    def __init__(self, d_model: int, num_heads: int, max_len: int):
        super(Encoder, self).__init__()
        self.d_model = d_model
        self.max_len = max_len

        # Layers for Query, Key, Value matrices
        self.w_query = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_key = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_value = nn.Linear(in_features=d_model, out_features=d_model)

        # multi-head attention layer
        self.attention = MultiHeadAttention(d_model=d_model, num_heads=num_heads)
        self.attn_layer_norm = nn.LayerNorm(normalized_shape=d_model)

        self.linear = nn.Linear(in_features=d_model, out_features=d_model)
        self.linear_layer_norm = nn.LayerNorm(normalized_shape=d_model))

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        """
        Args:
            data (torch.Tensor): Positional Encoding 벡터가 더해진 임베딩 벡터. (batch_size, max_len, hidden_dim)
        """
        # multi-head attention
        residual = X.view(self.max_len, -1, self.d_model)
        query, key, value = self.get_qkv(X)
        attn_scores = self.attention(query, key, value)
        attn_scores += residual
        attn_scores = self.attn_layer_norm(attn_scores)
        
        # feed forward
        residual = attn_scores
        hidden_state = self.linear(attn_scores)
        hidden_state += residual
        hidden_state = self.linear_layer_norm(hidden_state)

        return hidden_state


    def get_qkv(self, X: torch.Tensor) -> torch.Tensor:
        """Query, Key, Value 텐서를 리턴

        Args:
            X (torch.Tensor): [description]

        Returns:
            torch.Tensor: [description]
        """
        query = self.w_query(X)
        key = self.w_key(X)
        value = self.w_value(X)
        return query, key, value
