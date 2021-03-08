import torch
from torch import nn
from torch.nn import functional as F

from attention import MultiHeadAttention


class Decoder(nn.Module):
    def __init__(self, d_model: int, num_heads: int, max_len: int):
        super(Decoder, self).__init__()
        self.w_query_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_key_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_value_attn = nn.Linear(in_features=d_model, out_features=d_model)

        self.w_query_masked_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_key_masked_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_value_masked_attn = nn.Linear(in_features=d_model, out_features=d_model)
        
        self.masked_attention = MultiHeadAttention(d_model=d_model, num_heads=num_heads, mask=True)
        self.masked_attn_layer_norm = nn.LayerNorm(normalized_shape=d_model)

        self.attention = MultiHeadAttention(d_model=d_model, num_heads=num_heads, mask=False)
        self.attn_layer_norm = nn.LayerNorm(normalized_shape=d_model)

        self.linear = nn.Linear(in_features=d_model, out_features=d_model)
        self.linear_layer_norm = nn.LayerNorm(normalized_shape=d_model)
        return
        
    def forward(self, encoder_hidden_state: torch.Tensor, output_embedded: torch.Tensor) -> torch.Tensor:
        residual = output_embedded.contiguous()
        query, key, value  = self._get_qkv_attn(output_embedded)
        output_masked_attn = self.attention(query, key, value)
        output_masked_attn = self.attn_layer_norm(output_masked_attn)

        key_encoder = self.w_      

        pass

    def _get_qkv_masked_attn(self, encoder_hidden_state, output_embedded):
        query = self.w_query_masked_attn(encoder_hidden_state)
        key = self.w_key_masked_attn(encoder_hidden_state)
        value = self.w_value_masked_attn(output_embedded)
        return query, key, value

    def _get_qkv_attn(self, output_embedded):
        query = self.w_query_attn(output_embedded)
        key = self.w_key_attn(output_embedded)
        value = self.w_value_attn(output_embedded)