import torch
from torch import nn
from torch.nn import functional as F

from encoder import Encoder
from positional_encoding import PositionalEncoder


class Transformer(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        max_len: int, 
        d_model: int,
        num_heads: int,
        num_encoders: int=1,
        num_decoders: int=1,
    ):
        """Transformer for Machine Translation

        Args:
            vocab_size (int): 임베딩 딕셔너리 사이즈
            max_len (int): 문장의 최대 길이(최대 토큰 수)
            hidden_dim (int): 인코더, 디코더 내 hidden state의 차원. 입력 데이터에 대한 임베딩 차원과 같음
            num_heads (int): Attention 헤드 수
            num_encoders (int): 인코더 블록 수
            num_decoders (int): 디코더 블록 수
        """
        super(Transformer, self).__init__()
        self.d_model = d_model
        self.max_len = max_len

        self.embedding_layer = nn.Embedding(
            num_embeddings=vocab_size, embedding_dim=d_model
        )
        self.positional_encoder = PositionalEncoder(d_model=d_model)

        self.encoders = [Encoder(hidden_dim=d_model, num_heads=num_heads, max_len=max_len) for _ in range(num_encoders)]
        self.decoders = [Decoder(num_blocks=num_decoders, num_heads=num_heads, max_len=max_len) for _ in range(num_decoders)]

    def forward(self, X: torch.Tensor, output, train=True) -> torch.Tensor:
        batch_size = X.size(0)
        max_len = X.size(1)

        X_embedded = self.embedding_layer(X)  # (batch_size, max_len, hidden_dim)
        X_embedded += self.positional_encoder.forward(max_len=self.max_len)
        hidden_state = self.Encoder()

        return


class Decoder(nn.Module):
    def __init__(self, num_blocks: int):
        super(Decoder, self).__init__()
        pass
