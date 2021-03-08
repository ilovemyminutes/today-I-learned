from typing import Tuple

import torch
from torch import nn

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
        self.attention = MultiHeadAttention(
            d_model=d_model, num_heads=num_heads, mask=False
        )
        self.attn_layer_norm = nn.LayerNorm(normalized_shape=d_model)

        self.linear = nn.Linear(in_features=d_model, out_features=d_model)
        self.linear_layer_norm = nn.LayerNorm(normalized_shape=d_model)

    def forward(self, input_embedded: torch.Tensor) -> torch.Tensor:
        """
        Args:
            input_embedded (torch.Tensor): Positional Encoding 벡터가 더해진 임베딩 벡터. (B, L, d_model)
        """
        # multi-head attention
        residual = input_embedded.clone()
        qkv = self.get_qkv(input_embedded)
        attn_scores = self.attention(*qkv)
        attn_scores += residual
        attn_scores = self.attn_layer_norm(attn_scores)

        # feed forward
        residual = attn_scores.clone()
        hidden_state = self.linear(attn_scores)
        hidden_state += residual
        hidden_state = self.linear_layer_norm(hidden_state)

        return hidden_state

    def get_qkv(
        self, input_embedded: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Query, Key, Value 텐서를 리턴

        Args:
            input_embedded (torch.Tensor): Positional Encoding 벡터가 더해진 임베딩 벡터. (B, L, d_model)

        Returns:
            query/key/value: Query/Key/Value 텐서
        """
        query = self.w_query(input_embedded)
        key = self.w_key(input_embedded)
        value = self.w_value(input_embedded)
        return query, key, value
