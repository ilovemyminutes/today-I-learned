import math

import torch
from torch import nn
from torch.nn import functional as F

class Transformer(nn.Module):
    def __init__(self, vocab_size: int, hidden_dim: int, num_encoders: int, num_decoders: int):
        """Transformer for Machine Translation

        Args:
            input (torch.Tensor): 토큰화된 Sequence
            vocab_size (int): 임베딩 딕셔너리 사이즈
            hidden_dim (int): 인코더, 디코더 내 hidden state의 차원. 입력 데이터에 대한 임베딩 차원과 같음
        """        
        super(Transformer, self).__init__()
        self.hidden_dim = hidden_dim
        
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=hidden_dim)
        self.Encoder = Encoder(num_blocks=num_encoders)
        self.Decoder = Decoder(num_blocks=num_decoders)
    
    def forward(self, X: torch.Tensor, output, train=True) -> torch.Tensor:
        batch_size = X.size(0)
        max_len = X.size(1)

        data_embedded = self.embedding(X) # (batch_size, max_len, hidden_dim)
        hidden_state = self.Encoder()


        return


class Encoder(nn.Module):
    def __init__(self, hidden_dim: int, num_blocks: int):
        """
        """        
        super(Encoder, self).__init__()

        self.w_query = nn.Linear(in_features=hidden_dim, out_features=hidden_dim) # Query
        self.w_key = nn.Linear(in_features=hidden_dim, out_features=hidden_dim) # Key
        self.w_value = nn.Linear(in_features=hidden_dim, out_features=hidden_dim) # Value

        self.attention = MultiHeadAttention(hidden_dim, num_heads) # not implemented yet
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

    def get_qkv(self):
        raise NotImplementedError()


class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int):
        super(MultiHeadAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.hidden_split_dim = hidden_dim // num_heads # for multi-head attention
        return

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        '''
        query, key, value가 입력되는 상황을 전제
        '''
        attn_score = F.softmax(torch.matmul(query, key.transpose(-1, -2)) / math.sqrt(self.hidden_dim))
        attn_value = torch.matmul(attn_score, value)
        return attn_value

    def self_attention(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        pass

class PositionalEncoder(nn.Module):
    def __init__():
        super(PositionalEncoder, self).__init__()
        pass






        
class Decoder(nn.Module):
    def __init__(self, num_blocks: int):
        super(Decoder, self).__init__()
        pass