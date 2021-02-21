import torch
from torch import nn
from torch.nn import functional as F
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence


class Seq2Seq(nn.Module):
    def __init__(self, encoder: Encoder, decoder: Decoder):
        super(Seq2Seq, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(
        self,
        source_batch,
        source_batch_lens,
        target_batch,
        vocab_size,
        teacher_forcing: float = 0.5,
    ):
        encoder_outputs, hidden = self.encoder(source_batch, source_batch_lens)

        input_ids = target_batch[:, 0]
        batch_size = source_batch.size(0)
        outputs = torch.zeros(trg_max_len, batch_size, vocab_size)

        for t in range(1, trg_max_len):
            decoder_outputs, hidden = self.decoder(input_ids, encoder_outputs, hidden)
            outputs[i] = decoder_outputs
            _, top_ids = torch.max(decoder_outputs, dim=-1)
            input_ids = (
                trg_batch[:, t] if random.radom() > teacher_forcing_prob else top_ids
            )
        return outputs


class Encoder(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        embedding_size: int = 256,
        hidden_size: int = 512,
        num_layers: int = 2,
        num_dirs: int = 2,
        dropout: float = 0.1,
    ):
        """
        Args
        ---
        vocab_size: vocabulary에 참조할 vocab 수
        embedding_size: 임베딩 후 맵핑할 차원 수
        hidden_size: 인코딩 후 맵핑할 차원 수. RNN 모델의 hidden size
        num_layers: 쌓을 RNN 레이어 수
        num_dirs: 1일 경우 single direction, 2일 경우 bidirectional
        dropout: 드롭아웃 probability
        """
        super(Encoder, self).__init__()
        self.num_layers = num_layers
        self.num_dirs = num_dirs
        self.hidden_size = hidden_size
        self.bidirectional = True if num_dirs > 1 else False

        # define layers
        self.embedding = nn.Embedding(
            num_embeddings=vocab_size, embedding_dim=embedding_size
        )  # 임베딩 레이어
        self.gru = nn.GRU(
            input_size=embedding_size,  # RNN 레이어에 들어가게 되는 input size == 임베딩 벡터 size
            hidden_size=hidden_size,  # Seq2Seq에 활용할 hidden size
            num_layers=num_layers,
            bidirectional=self.bidirectional,
            dropout=dropout,
        )
        self.linear = nn.Linear(
            in_features=num_dirs * hidden_size, out_features=hidden_size
        )

    def forward(
        self, batch: torch.Tensor, batch_lens: torch.Tensor
    ) -> (torch.Tensor, torch.Tensor):
        batch_embedded = self.embedding(
            batch
        )  # (batch_size, seq_length, embedding_size)
        batch_embedded = batch_embedded.transpose(
            0, 1
        )  # (seq_length, batch_size, embedding_size)

        packed_batch = pack_padded_sequence(batch_embedded, batch_lens)

        h_0 = torch.zeros(
            self.num_layers * self.num_dirs, batch.shape[0], self.hidden_size
        )  # initialize
        packed_outputs, h_n = self.gru(packed_batch, h_0)
        outputs = pad_packed_sequence(packed_outputs)[0]
        outputs = torch.tanh(self.linear(outputs))

        hidden_list = [h_n[i] for i in range(self.num_dirs)]
        hidden = torch.tanh(self.linear(torch.cat(hidden_list, dim=-1))).unsqueeze(0)

        return outputs, hidden


# 기본적이 Attention 구조
class DotAttention(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, decoder_hidden: torch.Tensor, encoder_outputs: torch.Tensor):
        """
        Args
        ---
        decoder_hidden: 디코더의 현재 hidden state 사이즈. (1, batch_size, seq_length)
        encoder_outputs: 인코더의 모든 hidden state 사이즈. (seq_length, batch_size, decoder_hidden)
        """
        query = decoder_hidden.squeeze(0)  # (batch_size, decoder_hidden)
        key = encoder_outputs.transpose(
            0, 1
        )  # (batch_size, seq_length, decoder_hidden)
        energy = torch.sum(
            torch.mul(key, query.unsqueeze(dim=1)), dim=-1
        )  # (batch_size, seq_length)

        attn_scores = F.softmax(energy, dim=-1)  # (batch_size, seq_length)
        attn_values = torch.sum(
            torch.mul(encoder_outputs.transpose(0, 1), attn_scores.unsqueeze(dim=2)),
            dim=1,
        )

        return attn_values, attn_scores


class Decoder(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        embedding_size: int,
        attention: nn.Module,
        hidden_size: int,
        num_dirs: int = 2,
    ):
        super(Decoder, self).__init__()

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size, embedding_dim=embedding_size
        )  # 인코더의 임베딩 레이어와 같은 형태
        self.attention = attention
        self.rnn = nn.GRU(input_size=embedding_size, hidden_size=hidden_size)
        self.output_linear = nn.Linear(num_dirs * hidden_size, vocab_size)

    def forward(self, batch, encoder_outputs, encoder_hidden):
        batch_embedded = self.embedding(batch).unsqueeze(
            0
        )  # (batch_size, decoder_hidden) -> (1, batch_size, decoder_hidden)
        outputs, hidden = self.rnn(batch_embedded, encoder_hidden)
        attn_values, attn_scores = self.attention(
            hidden, encoder_outputs
        )  # (batch_size, decoder_hidden), (1, batch_size, seq_length)
        concat_outputs = torch.cat(
            [outputs, attn_values.unsqueeze(dim=0)], dim=-1
        )  # (1, batch_size, decoder_hidden)

        return (
            self.output_linear(concat_outputs).squeeze(0),
            hidden,
        )  # (batch_size, vocab_size), (1, batch_size, decoder_hidden)
