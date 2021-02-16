# Machine Learning

### Feature Engineering

#### Encoding

One-Hot Encoding

- 장점: 쉬운 구현
- 단점: 차원의 저주, 0과 1로만 구성되어 낮은 정보 이득, tree의 경우 Depth만 깊어지는 참사, RF의 SubSampling 사용시 One-Hot 피쳐만 추출될 수 있음

Label Encoding

- 장점: 모델 학습 시 One-Hot Encoding보다 빠름
- 단점: Numeric의 함정에 빠질 수 있음. 즉, 선형회귀 모델에 적합하지 않은 방법

Target Encoding

- 장점: 차원의 저주 해결, 회귀/분류 문제 모두 bias를 줄이는 효과

- 단점: Data Leakage(학습 데이터에는 예측값에 대한 정보가 종속되는 문제), 검증 데이터의 타깃 분포가 학습 데이터와 다르면 과적합 발생

  - 단점 해결

  1. Smoothing
     ![](https://latex.codecogs.com/svg.latex?Encoded\,Value(after\,smoothing)%20=%20\frac%20{mean(target)%20*%20nrow%20+%20global\,mean%20*%20\alpha}%20{nrow%20+%20\alpha})

  2. CV Loop

  3. Expanding Mean

- Reference. [Categorical Value Encoding 과 Mean Encoding](https://dailyheumsi.tistory.com/120)