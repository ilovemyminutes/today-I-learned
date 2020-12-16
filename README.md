# ✔ilovemyWIKI
본 저장소는 분야에 관계 없이 공부하며 얻은 것들을 정리하는 공간입니다.

## Programming
### Libraries
#### NumPy | Python
- `np.iinfo(type=)`: int, float 데이터 타입의 표현 가능한 수의 한계를 반환
#### Pandas | Python
- `pd.Categorical`: 컬럼 속성을 Categorical로 변환. Label Encoding을 진행할 떄 유용.
  ```python
  temp = pd.Series([10,20,30,20,10]).to_frame('cat')
  temp['cat'] = pd.Categorical(temp['cat']) # 해당 변수 type이 Categorical이 됨
  temp['cat_ID'] = temp['cat'].cat.codes # 각 클래스별 ID는 cat.codes 인스턴스를 호출하여 구함
  ```
### Notions
* Name Mangling(=Name Decoration)
  - 함수를 선언하거나 전역 변수 등을 선언했을 때 컴파일 단계에서 일정한 규칙을 갖고 변경되는 것
  - Linker가 다른 Scope에 있는 같은 이름의 함수와 변수에 대해 구별할 수 있도록 하는 요소로, 컴파일러 입장에서 중요한 작업
  - 컴파일러는 함수에 대하여 함수의 이름, 파라미터 타입, Calling Convention 등을 사용하여 이름을 생성
  
## ML
### Model
#### Time-Series
* ARIMA
* Data Structure for time-series
### Feature Engineering
#### Encoding
* One-Hot Encoding
  - 👍: 쉬운 구현
  - 👎: 차원의 저주, 0과 1로만 구성되어 낮은 정보 이득, tree의 경우 Depth만 깊어지는 참사, RF의 SubSampling 사용시 One-Hot 피쳐만 추출될 수 있음

* Label Encoding
  - 👍: 모델 학습 시 One-Hot Encoding보다 빠름
  - 👎: Numeric의 함정에 빠질 수 있음. 즉, 선형회귀 모델에 적합하지 않은 방법
  
* Target Encoding
  - 👍: 차원의 저주 해결, 회귀/분류 문제 모두 bias를 줄이는 효과
  - 👎: Data Leakage(학습 데이터에는 예측값에 대한 정보가 종속되는 문제), 검증 데이터의 타깃 분포가 학습 데이터와 다르면 과적합 발생
    - 단점 해결
      - Smoothing
      ![](https://latex.codecogs.com/svg.latex?Encoded\,Value(after\,smoothing)%20=%20\frac%20{mean(target)%20*%20nrow%20+%20global\,mean%20*%20\alpha}%20{nrow%20+%20\alpha})
      - CV Loop
      - Expanding Mean
      
#### Basis Expansion
#### Dimension Reduction

## DL
### Preprocessing
* Batch Normalization

## Attitude
* 무식한 접근이 나을 때도 꽤 많다.
* 디버깅 대충하지 말 것

## Reference
- [Name Mangling](https://thepassion.tistory.com/61)
- [Categorical Value Encoding 과 Mean Encoding](https://dailyheumsi.tistory.com/120)
