from typing import Tuple

import torch
from torch import nn

from attention import MultiHeadAttention


class Decoder(nn.Module):
    def __init__(self, d_model: int, num_heads: int) -> None:
        super(Decoder, self).__init__()
        self.w_query_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_key_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_value_attn = nn.Linear(in_features=d_model, out_features=d_model)

        self.w_query_masked_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_key_masked_attn = nn.Linear(in_features=d_model, out_features=d_model)
        self.w_value_masked_attn = nn.Linear(in_features=d_model, out_features=d_model)

        self.masked_attention = MultiHeadAttention(
            d_model=d_model, num_heads=num_heads, mask=True
        )
        self.masked_attn_layer_norm = nn.LayerNorm(normalized_shape=d_model)

        self.attention = MultiHeadAttention(
            d_model=d_model, num_heads=num_heads, mask=False
        )
        self.attn_layer_norm = nn.LayerNorm(normalized_shape=d_model)

        self.linear = nn.Linear(in_features=d_model, out_features=d_model)
        self.linear_layer_norm = nn.LayerNorm(normalized_shape=d_model)
        return

    def forward(
        self, encoder_hidden_state: torch.Tensor, output_embedded: torch.Tensor
    ) -> torch.Tensor:
        """Transformer 모델 디코더의 forward-propagation 결과 출력

        Args:
            encoder_hidden_state (torch.Tensor): 인코더 블록(들)에서 최종적으로 얻은 hidden state
            output_embedded (torch.Tensor): 디코더에 입력되는 출력 시퀀스
                - 가령, 언어 번역 task의 경우, 번역된 문장에 대한 시퀀스를 의미
                - Train 단계에서는 마스킹을 통해 디코딩 진행
                - Inference 단계에서는 순차적으로 임베딩된 토큰을 입력

        Returns:
            torch.Tensor: forward 출력 텐서
        """
        # masked multi-head attention
        residual = output_embedded.clone()
        qkv_masked_attn = self._get_qkv_masked_attn(output_embedded)
        output_masked_attn = self.attention(*qkv_masked_attn)
        output_masked_attn = self.attn_layer_norm(output_masked_attn)
        output_masked_attn += residual

        # multi-head attention
        residual = output_masked_attn.clone()
        qkv_attn = self._get_qkv_attn(encoder_hidden_state, output_masked_attn)
        output_attn = self.masked_attention(*qkv_attn)
        output_attn = self.masked_attn_layer_norm(output_attn)
        output_attn += residual
        return output_attn

    def _get_qkv_attn(
        self, encoder_hidden_state: torch.Tensor, output_masked_attn: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Multi-head Attention 셀에 입력할 Query, Key, Value 텐서를 출력

        Args:
            encoder_hidden_state (torch.Tensor): 인코더 블록(들)에서 최종적으로 얻은 hidden state
            output_masked_attn (torch.Tensor): Masked Multi-head Attention 셀에서 출력된 hidden state

        Returns:
            Query/Key/Value: Query/Key/Value 텐서
        """
        query = self.w_query_masked_attn(encoder_hidden_state)
        key = self.w_key_masked_attn(encoder_hidden_state)
        value = self.w_value_masked_attn(output_masked_attn)
        return query, key, value

    def _get_qkv_masked_attn(
        self, output_embedded: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Masked Multi-head Attention 셀에 입력할 Query, Key, Value 텐서를 출력

        Args:
            output_embedded (torch.Tensor): Positional Encoding이 더해진 임베딩 output 텐서

        Returns:
            Query/Key/Value: Query/Key/Value 텐서
        """
        query = self.w_query_attn(output_embedded)
        key = self.w_key_attn(output_embedded)
        value = self.w_value_attn(output_embedded)
        return query, key, value
