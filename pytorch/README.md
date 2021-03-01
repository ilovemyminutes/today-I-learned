# PyTorch
*`Tensor`: 텐서 객체

`torch`

- 메인 네임스페이스. `Tensor` 등 다양한 수학 함수를 포함. NumPy와 유사한 방식으로 작동.

`torch.Autograd`

- 자동 미분 도구를 지원하는 모듈. 자동미분을 on/off하는 `enable_grad`, `no_grad` 등 지원

`torch.nn`

- 신경망 구축을 위한 다양한 데이터 구조/레이어가 정의된 모듈. Layer, Activation Function, Loss Function 등 포함

`torch.optim`

- 파라미터 최적화 알고리즘을 지원하는 모듈

`torch.utils.data`

- SGD의 반복 연산 실행시 활용되는 미니배치용 유틸리티 함수가 포함된 모듈

`torch.onnx`

- onnx(open neural network exchange)의 포맷으로 모델을 export할 떄 사용. onnx 포맷을 활용하면 서로 다른 딥러닝 프레임워크 간 모델 공유 가능

`torchvision.datasets`

- 파이토치에서 지원하는 데이터셋을 불러오기 위한 모듈

`torch.utils.data.DataLoader`

`torch.Tensor().sort(descending: bool=False) -> torch.return_types.sort`

- 텐서를 정렬하는 메서드. `values` 인스턴스를 통해 정렬된 텐서 성분에 접근, `indices` 인스턴스를 통해 정렬된 텐서 인덱스에 접근
- 언패킹 가능!

`torch.zeros(*size, dtype)`

- 영텐서를 생성. 순차적으로 shape값을 입력(tuple로 넣지 않아도 되는데 왠지 가독성 면에서 tuple로 넣는게 나을 것 같다)

`torch.nn.LSTM(input_size, hidden_size, num_layers, bias: bool, batch_first: bool, dropout, bidirectional)`

- bias: False일 경우 bias 항을 제외하고 학습. Default - True
- batch_first: True일 경우 input/output 텐서의 shape가 (batch_size, sequence length, feature_size)로 설정됨. Default - False
- dropout: non-zero일 경우 마지막 레이어를 제외한 각 LSTM 레이어 간 output에 대해 Dropout 레이어를 적용
- Input: input, (h_0, c_0)
  - input: (sequence_length, batch_size, input_size)
  - h_0: (num_layers \* num_directions, batch, hidden_size)
  - c_0: (num_layers \* num_directions, batch, hidden_size)
  - (h_0, c_0)가 입력되지 않을 경우 각각  0을 default로 설정

`torch.mul(input: torch.Tensor, other: torch.Tensor) -> torch.Tensor`: element-wise multiplication

`nn.Softmax()` vs `nn.functional.softmax()`

- `nn.Softmax()`: PyTorch 모델의 일부 레이어로 활용할 수 있는 Module 클래스 객체
- `nn.functional.softmax()`: 소프트맥스 연산을 수행하는 함수

`nn.Embedding(num_embeddings: int, embedding_dim: int)`: 임베딩 레이어

`nn.Linear(in_features: int, out_features: int, bias: bool=True)`: 선형변환(fully connected) 레이어

`Tensor.contiguous()`: 텐서의 복사본을 생성

- 엄밀하게 이해한 것은 아님!

`torch.tril(input, diagonal=0)`: 하삼각행렬을 리턴

- `diagonal`: 대각선의 인덱스
- masking에 활용

`Tensor.masked_fill_(mask: torch.BoolTensor, value: float)`: 텐서에 마스킹을 하는 함수. 마스킹할 위치에 `value` 값을 채워 넣음