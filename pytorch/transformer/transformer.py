import torch
from torch import nn
from torch.nn import functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int):
        super(MultiHeadAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.hidden_split_dim = hidden_dim // num_heads

        return

    def forward(self, data) -> torch.Tensor:
        '''
        query, key, value가 입력되는 상황을 전제

        '''
        
        query = self.w_query(query).view()
        key = self.w_key(key).view()
        value = self.w_value(value).view()
        torch.matmul(query, key.transpose(-1, -2)) / 
        
        
        F.softmax()

class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()
        pass


class Decoder(nn.Module):
    def __init__(self):
        super(Decoder, self).__init__()
        pass



class Transformer(nn.Module):
    def __init__(self, vocab_size, hidden_dim):
        super(Transformer, self).__init__()
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=hidden_dim)
        self.w_q = nn.Linear(in_feauters=self.hidden_dim, out_features=self.hidden_dim)
        self.w_k = nn.Linear(in_feauters=self.hidden_dim, out_features=self.hidden_dim)
        self.w_v = nn.Linear(in_feauters=self.hidden_dim, out_features=self.hidden_dim)
    
    def forward(self, input, output):    
        pass

    def get_QKV(self, data):
        query = self.w_q(data)
        key = self.w_k(data)
        value = self.w_v(data)
        return query, key, value
        
