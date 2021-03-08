# Transformer by myself

## Task
- Transformer 모델을 활용한 NMT

## Issues
### 파트별 Input/Output
###### Transformer

- Input: 두 가지 케이스로 나눌 수 있을 듯
    1. 토큰화된 시퀀스
        - shape: `(batch_size, max_len)`
    2. 토큰화도 거치지 않은 문장 자체
        - Shape: `(batch_size, )`
- Output: 번역된 문장

###### Positional Encoding

- Input: 임베딩 차원(`d_model`)
- Output: shape가 `(batch_size, max_len, embedding_size)`인 인코딩 벡터
- 가장 모르겠는 부분
    - 학습 가능한 파라미터가 있는가? 있다면 어떻게 구조화해야 하고, 없다면 또 어떻게?
      => 후속 모델은 학습 가능한 파라미터를 두는 것 같지만, Transformer에서는 단지 차원에 따른 constant벡터를 생성!

###### Encoder

- Input: 임베딩된 Input *X*
    - shape: `(batch_size, max_len, embedding_Size)`
- Output: 인코딩 결과, *hidden_state*
    - shape: `(batch_size, max_len, embedding_Size)`
- Phase #1: Multi-head Attention
    - Input: 임베딩된 입력 x
        - shape: `(batch_size, max_len, embedding_Size)`
    - Output: Attention Matrix
        - shape: `(batch_size, max_len, embedding_Size)`
- Phase #2: Add & Norm
    - Input: 임베딩된 입력 x, Multi-head Attention의 출력
    - Output: 입력값이 모두 더해진 뒤 normalization된 값
        - shape: `(batch_size, max_len, embedding_Size)`

###### Decoder

- Input: 인코더의 `hidden_state`, 디코더의 임베딩된 Input *X'*
  - shape of 인코더의 `hidden_state`: `(batch_size, max_len, embedding_size)`
  - shape of 디코더의 임베딩된 Input *X'*: `(batch_size, max_len, embedding_size)`
- NOTE
  - 학습 동안 시퀀스의 각 성분에 Masked Attention이 적용되고, 최종적인  loss는 시퀀셜하게 생성된 모든 decoder의 output을 갖고 계산됨


> etc
- 클래스 단위로 구성한 모델들은 backpropagation 일괄적으로 되나?
- Encoder, Decoder 등 각 클래스별 input과 output의 구성을 명확히 하고 짜야겠다
- [?] Query, Key, Value를 구하는 부분은 Transformer 클래스에 들어가야 하지 않을까?

