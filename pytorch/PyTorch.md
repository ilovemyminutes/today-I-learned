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

##### `torch.randint(low=0, high, size: tuple)`

- 임의의 정수로 채워진 텐서를 생성
- 각 정수는 [`low`, `high`)에서 무작위 복원추출
- `size`: 텐서의 크기

##### `torch.nn.LSTM(input_size, hidden_size, num_layers, bias: bool, batch_first: bool, dropout, bidirectional)`

- `bias`: False일 경우 bias 항을 제외하고 학습. Default - True
- `batch_first`: True일 경우 input/output 텐서의 shape가 (batch_size, sequence length, feature_size)로 설정됨. Default - False
- `dropout`: non-zero일 경우 마지막 레이어를 제외한 각 LSTM 레이어 간 output에 대해 Dropout 레이어를 적용
- 입력: `input, (h_0, c_0)`
  - `input`: (sequence_length, batch_size, input_size)
  - `h_0`: (num_layers \* num_directions, batch, hidden_size)
  - `c_0`: (num_layers \* num_directions, batch, hidden_size)
  - `(h_0, c_0)`가 입력되지 않을 경우 각각  0을 default로 설정

##### `torch.nn.Conv2(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros')`

- 2차원 합성곱 레이어
- 입력: (N, Cin, H, W)
- 출력: (N, Cout), Hout, Wout)

##### `torch.nn.BatchNorm2d(num_features, eps=1e-5, momentum=.1, affine=True, track_running_stats=True)`

- 입력: (N, C, H, W)
- 출력: (N, C, H, W)(그대로)

- `num_features`: (N, C, H, W)의 입력값 중 C값, 즉 이전 레이어의 출력 채널 수
- `eps`: 수치적 안정성을 위해 분모에 더할 값(zero division 문제를 방지하는 듯)
- `momentum`: running_mean, running_var 연산에 활용. None으로 설정시 단순 평균으로 설정됨
- `affine: bool`: True로 설정시, affine 파라미터가 학습 가능하게 설정됨
- `track_running_stats: bool`
  - True: running mean, variance를 트래킹
  - False: 트래킹 x, 즉, `running_mean`과 `running_var`가 모두 `None`

###### `torch.matmul(input: torch.Tensor, other: torch.Tensor) -> torch.Tensor`

- 두 텐서 간 행렬곱을 수행하는 함수
- 2차원의 두 행렬을 곱하는 건 주의할 점이 크게 없지만, 2차원이 넘는 고차원 텐서 간 행렬곱은 헷갈릴 수 있음.
- 핵심은, `matmul`은 기본적으로 **행의 차원과 열의 차원만** 사용한다는 것! 즉, 각 텐서 shape의 마지막 두 차원만을 고려하면 된다!

###### `F.softmax(input, dim)`

- 입력된 텐서에 대해 소프트맥스를 취하는 함수

- 주의해야할 것이 바로 `dim`인데, 축을 어떻게 설정하는지에 따라 소프트맥스를 취하는 방향이 달라짐. 가령,  row-wise 소프트맥스는 `dim=-1`로 설정하면 됨

  ```python
  >>> rands = torch.rand(1, 4, 5)
  >>> rands
  tensor([[[0.6611, 0.5318, 0.1099, 0.1732, 0.7478],
           [0.2951, 0.4061, 0.1075, 0.8161, 0.7739],
           [0.3400, 0.1615, 0.5076, 0.8063, 0.5073],
           [0.5689, 0.2168, 0.3346, 0.4579, 0.3236]]])
  
  >>> F.softmax(rands, dim=-1)
  tensor([[[0.2404, 0.2113, 0.1385, 0.1476, 0.2622],
           [0.1602, 0.1789, 0.1328, 0.2696, 0.2585],
           [0.1725, 0.1443, 0.2040, 0.2751, 0.2040],
           [0.2397, 0.1686, 0.1896, 0.2145, 0.1876]]])
  ```

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

`torch.triu(input, diagonal=0)`

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