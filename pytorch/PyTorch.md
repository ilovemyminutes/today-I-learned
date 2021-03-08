# PyTorch
*`Tensor`: 텐서 객체

##### `torch`

- 메인 네임스페이스. `Tensor` 등 다양한 수학 함수를 포함. NumPy와 유사한 방식으로 작동.

##### `torch.Autograd`

- 자동 미분 도구를 지원하는 모듈. 자동미분을 on/off하는 `enable_grad`, `no_grad` 등 지원

##### `torch.nn`

- ##### 신경망 구축을 위한 다양한 데이터 구조/레이어가 정의된 모듈. Layer, Activation Function, Loss Function 등 포함

##### `torch.optim`

- 파라미터 최적화 알고리즘을 지원하는 모듈

##### `torch.utils.data`

- SGD의 반복 연산 실행시 활용되는 미니배치용 유틸리티 함수가 포함된 모듈

##### `torch.onnx`

- onnx(open neural network exchange)의 포맷으로 모델을 export할 떄 사용. onnx 포맷을 활용하면 서로 다른 딥러닝 프레임워크 간 모델 공유 가능

##### `torchvision.datasets`

- 파이토치에서 지원하는 데이터셋을 불러오기 위한 모듈

##### `torch.utils.data.DataLoader`

##### `torch.Tensor().sort(descending: bool=False) -> torch.return_types.sort`

- 텐서를 정렬하는 메서드. `values` 인스턴스를 통해 정렬된 텐서 성분에 접근, `indices` 인스턴스를 통해 정렬된 텐서 인덱스에 접근
- 언패킹 가능!

##### `torch.zeros(*size, dtype)`

- 영텐서를 생성. 순차적으로 shape값을 입력(tuple로 넣지 않아도 되는데 왠지 가독성 면에서 tuple로 넣는게 나을 것 같다)

##### `torch.nn.LSTM(input_size, hidden_size, num_layers, bias: bool, batch_first: bool, dropout, bidirectional)`

- bias: False일 경우 bias 항을 제외하고 학습. Default - True
- batch_first: True일 경우 input/output 텐서의 shape가 (batch_size, sequence length, feature_size)로 설정됨. Default - False
- dropout: non-zero일 경우 마지막 레이어를 제외한 각 LSTM 레이어 간 output에 대해 Dropout 레이어를 적용
- Input: input, (h_0, c_0)
  - input: (sequence_length, batch_size, input_size)
  - h_0: (num_layers \* num_directions, batch, hidden_size)
  - c_0: (num_layers \* num_directions, batch, hidden_size)
  - (h_0, c_0)가 입력되지 않을 경우 각각  0을 default로 설정

##### `torch.nn.Conv2(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros')`

- 2차원 합성곱 레이어
- input: (N, Cin, H, W)
- output: (N, Cout), Hout, Wout)

##### `torch.nn.BatchNorm2d(num_features, eps=1e-5, momentum=.1, affine=True, track_running_stats=True)`

- Input: (N, C, H, W)
- Output: (N, C, H, W)(그대로)

- `num_features`: (N, C, H, W)의 입력값 중 C값, 즉 이전 레이어의 출력 채널 수
- `eps`: 수치적 안정성을 위해 분모에 더할 값(zero division 문제를 방지하는 듯)
- `momentum`: running_mean, running_var 연산에 활용. None으로 설정시 단순 평균으로 설정됨
- `affine: bool`: True로 설정시, affine 파라미터가 학습 가능하게 설정됨
- `track_running_stats: bool`
  - True: running mean, variance를 트래킹
  - False: 트래킹 x, 즉, `running_mean`과 `running_var`가 모두 `None`

##### `torch.mul(input: torch.Tensor, other: torch.Tensor) -> torch.Tensor`

- element-wise multiplication
- NOTE: element-wise 곱은 1×N 또는 N×N의 관계에만 성립

##### `nn.Softmax()` vs `nn.functional.softmax()`

- `nn.Softmax()`: PyTorch 모델의 일부 레이어로 활용할 수 있는 Module 클래스 객체
- `nn.functional.softmax()`: 소프트맥스 연산을 수행하는 함수

##### `nn.Embedding(num_embeddings: int, embedding_dim: int)`

- `num_embeddings`: 임베딩 딕셔너리 수

##### `nn.Linear(in_features: int, out_features: int, bias: bool=True)`

##### `Tensor.contiguous()`

- 텐서의 복사본을 생성

- 엄밀하게 이해한 것은 아님!

##### `torch.tril(input, diagonal=0)`: 하삼각행렬을 리턴

- `diagonal`: 대각선의 인덱스
- masking에 활용

##### `Tensor.masked_fill_(mask: torch.BoolTensor, value: float)`

- 텐서에 마스킹을 하는 함수
- 마스킹할 위치에 `value` 값을 채워 넣음

##### Initialization

```python
# 방법1
embedding_layer = nn.Embedding(num_embeddings=vocab_size, embedding_dim=3)
embedding_layer.weight.data.uniform_(-1, 1)

# 방법2 
embedding_layer = nn.Embedding(num_embeddings=vocab_size, embedding_dim=3)
nn.init.uniform_(embedding_layer.weight, -1, 1)
```

##### `Tensor.view()`

- 텐서의 shape를 변경. 입력한 shape에 맞게 변경하고, 단순히 가장 우선적으로 등장하는 값부터 채워넣는 식

##### `nn.LayerNorm(normalized_shape)`