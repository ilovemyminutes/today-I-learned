# Latent Factor Recommendation System

##### 상품에 부여된 평점으로부터 추출한 상품과 유저의 잠재 속성을 활용한 추천 방법

- 기존 Collaborative Filtering, Content-based RS 방법을 뛰어넘은 추천 방법
- 학습 가능한 가중치가 존재하여, 손실 함수를 최소화함으로써 최적의 latent vector 추출

구축 과정

![image-20210226184928621](C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226184928621.png)

- R: 크기가 (유저수 x 상품 수)인 평점 희소 행렬

- X: 크기가 (유저수 x 잠재 벡터 차원)인 유저 행렬

- Y: 크기가 (상품 수 x 잠재 벡터 차원)인 상품 행렬

  - 일반적으로 잠재 벡터의 차원은 10~250으로 설정하나, 튜닝 과정을 통해 최적 차원을 찾아야 함

- transpose(X)와 Y를 행렬곱한 결과가 행렬 R과 유사해지는 방향으로 학습

- 손실함수:

  <img src="C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226185856647.png" alt="image-20210226185856647" style="zoom:50%;" />

- 최적화 방법: SGD

1. 초기화: X, Y를 가우시안 분포를 따르는 임의 값으로 초기화
2. 최적화
   - 실제 평점(label)을 가진 유저와 상품의 잠재 벡터를 개별적으로 추출한 뒤, 실제 평점과의 오차를 계산
   - Learning Rate와 오차를 활용하여 유저, 상품의 해당 잠재 벡터에 대한 업데이트 진행