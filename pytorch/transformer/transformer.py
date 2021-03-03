import math

import torch
from torch import nn
from torch.nn import functional as F


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


class Encoder(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int, num_blocks: int):

        super(Encoder, self).__init__()

        self.w_query = nn.Linear(
            in_features=hidden_dim, out_features=hidden_dim
        )  # Query
        self.w_key = nn.Linear(in_features=hidden_dim, out_features=hidden_dim)  # Key
        self.w_value = nn.Linear(
            in_features=hidden_dim, out_features=hidden_dim
        )  # Value

        self.attention = MultiHeadAttention(
            hidden_dim=hidden_dim, num_heads=num_heads
        )  # not implemented yet
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
        query = query.view(self.batch_size, -1, self.num_heads, self.hidden_dim_head) # (batch_size, max_len, num_heads, hidden_dim)
        key = key.view(self.batch_size, -1, self.num_heads, self.hidden_dim_head)
        value = value.view(self.batch_size, -1, self.num_heads, self.hidden_dim_head)

        query = query.transpose(1, 2)
        key = key.transpose(1, 2)
        value = value.transpose(1, 2)
        
        attention_score = self.get_self_attention(query, key, value)

        return attention_score

    def get_self_attention(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        attention_raw = F.softmax(
            torch.matmul(query, key.transpose(-1, -2)) / math.sqrt(self.hidden_dim)
        )
        attention_score = torch.matmul(attention_raw, value).view(
            self.batch_size, -1, self.hidden_dim
        )
        return attention_score

    def split(self, X: torch.Tensor)



class PositionalEncoder(nn.Module):
    def __init__():
        super(PositionalEncoder, self).__init__()
        pass


class Decoder(nn.Module):
    def __init__(self, num_blocks: int):
        super(Decoder, self).__init__()
        pass
