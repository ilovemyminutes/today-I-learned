import torch
from torch import nn

from encoder import Encoder
from decoder import Decoder
from positional_encoding import PositionalEncoder
from utils import MultipleInputSequential


class Transformer(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        max_len: int,
        d_model: int,
        num_heads: int,
        num_encoders: int = 1,
        num_decoders: int = 1,
    ):
        """Transformer for Machine Translation

        Args:
            vocab_size (int): 임베딩 딕셔너리 사이즈
            max_len (int): 문장의 최대 길이(최대 토큰 수)
            hidden_dim (int): 인코더, 디코더 내 hidden state의 차원. 입력 데이터에 대한 임베딩 차원과 같음
            num_heads (int): Attention 헤드 수
            num_encoders (int): 인코더 블록 수
            num_decoders (int): 디코더 블록 수

        Reference: https://arxiv.org/abs/1706.03762
        """
        super(Transformer, self).__init__()
        self.d_model = d_model
        self.max_len = max_len
        self.num_heads = num_heads

        self.embedder = nn.Embedding(num_embeddings=vocab_size, embedding_dim=d_model)
        self.positional_encoder = PositionalEncoder(d_model=d_model)
        self.encoders = self._get_encoders(num_encoders=num_encoders)
        self.decoders = self._get_decoders(num_decoders=num_decoders)
        self.linear = nn.Linear(in_features=d_model, out_features=vocab_size)

    def forward(self, input: torch.Tensor, output: torch.Tensor) -> torch.Tensor:
        """다음과 같은 과정으로 feed-forward 진행
            *P.E: Positional Encoding

                Input ->  Embedded input with P.E -> [Encoder Block] -> Encoder hidden state
                                     ┌───────────────────────────────────────────┘
                          Encoder hidden state ──────┐
                                              [Decoder Block] -> Linear -> Output 
                Output -> Embedded output with P.E ──┘

        Args:
            input (torch.Tensor): [description]
            output (torch.Tensor): [description]

        Returns:
            torch.Tensor: Output

        Reference: http://jalammar.github.io/illustrated-transformer/
        """        
        input_embedded = self._get_embedding_with_positional_encoding(input)
        output_embedded = self._get_embedding_with_positional_encoding(output)

        enc_hidden_state = self.encoders(input_embedded)
        dec_hidden_state = self.decoders(output_embedded, enc_hidden_state)

        output = self.linear(dec_hidden_state)
        return output

    def _get_encoders(self, num_encoders: int) -> nn.Sequential:
        """Encoder 블록을 생성

        Args:
            num_encoders (int): 블록에 넣을 Encoder 수

        Returns:
            nn.Sequential: Encoder 블록
        """        
        encoders = [
            Encoder(
                d_model=self.d_model, num_heads=self.num_heads, max_len=self.max_len
            )
            for _ in range(num_encoders)
        ]
        return nn.Sequential(*encoders)

    def _get_decoders(self, num_decoders: int) -> nn.Sequential:
        """Decoder 블록을 생성

        Args:
            num_decoders (int): 블록에 넣을 Decoder 수

        Returns:
            nn.Sequential: Decoder 블록
        """        
        decoders = [
            Decoder(d_model=self.d_model, num_heads=self.num_heads)
            for _ in range(num_decoders)
        ]
        return MultipleInputSequential(*decoders)

    def _get_embedding_with_positional_encoding(
        self, input: torch.Tensor
    ) -> torch.Tensor:
        """Positional Encoding 벡터를 생성

        Args:
            input (torch.Tensor): Positional Encoding 벡터의 차원을 결정하는데 참조할 input 텐서

        Returns:
            torch.Tensor: Positional Encoding 벡터
        """    
        input_embedded = self.embedder(input)
        input_embedded += self.positional_encoder(max_len=self.max_len)
        return input_embedded
