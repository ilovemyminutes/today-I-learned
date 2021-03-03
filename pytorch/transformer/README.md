# Transformer by myself

## Task
- Transformer 모델을 활용한 NMT

## Issues
### 파트별 Input/Output
- Transformer(overall)
    - Input: 두 가지 케이스로 나눌 수 있을 듯
        1. 토큰화된 시퀀스
            - shape: `(batch_size, max_len)`
        2. 토큰화도 거치지 않은 문장 자체
            - Shape: `(batch_size, )`
    - Output: 번역된 문장
- Positional Encoding
    - Input: ???
        - shape: `(batch_size, max_len, embedding_size)`
    - Output: ???
        - shape: `(batch_size, max_len, embedding_size)`
    - 가장 모르겠는 부분
        - 학습 가능한 파라미터가 있는가? 있다면 어떻게 구조화해야 하고, 없다면 또 어떻게?
- Encoder
    - Input: 임베딩된 입력 x
        - shape: `(batch_size, max_len, embedding_Size)`
    - Output: 인코딩 결과
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


> etc
- 클래스 단위로 구성한 모델들은 backpropagation 일괄적으로 되나?
- Encoder, Decoder 등 각 클래스별 input과 output의 구성을 명확히 하고 짜야겠다
- [?] Query, Key, Value를 구하는 부분은 Transformer 클래스에 들어가야 하지 않을까?

