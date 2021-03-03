import math

import torch
from torch import nn
from torch.nn import functional as F

from transformer.encoder import Encoder


class Transformer(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        hidden_dim: int,
        num_heads: int,
        num_encoders: int,
        num_decoders: int,
    ):
        """Transformer for Machine Translation

        Args:
            vocab_size (int): 임베딩 딕셔너리 사이즈
            hidden_dim (int): 인코더, 디코더 내 hidden state의 차원. 입력 데이터에 대한 임베딩 차원과 같음
            num_heads (int): Attention 헤드 수
            num_encoders (int): 인코더 블록 수
            num_decoders (int): 디코더 블록 수
        """
        super(Transformer, self).__init__()
        self.hidden_dim = hidden_dim

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size, embedding_dim=hidden_dim
        )
        self.Encoder = Encoder(
            hidden_dim=hidden_dim, num_blocks=num_encoders, num_heads=num_heads
        )
        self.Decoder = Decoder(num_blocks=num_decoders)

    def forward(self, X: torch.Tensor, output, train=True) -> torch.Tensor:
        batch_size = X.size(0)
        max_len = X.size(1)

        data_embedded = self.embedding(X)  # (batch_size, max_len, hidden_dim)
        hidden_state = self.Encoder()

        return

class PositionalEncoder(nn.Module):
    def __init__(self, hidden_dim):
        super(PositionalEncoder, self).__init__()
        pass


class Decoder(nn.Module):
    def __init__(self, num_blocks: int):
        super(Decoder, self).__init__()
        pass
