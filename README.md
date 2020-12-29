# ✔iloveCookBook
본 저장소는 분야에 관계 없이 공부하며 얻은 것들을 정리하는 공간입니다.

## Programming
#### NumPy | Python
- `np.random.rand(d1, d2, ... , dn)`: n차원 배열 생성. 각 값은 \[0, 1)
- `np.arange(start, stop, step)`: `range()`와 같은 역할 + 실수값의 step 사용 가능
- `np.linspace(start, stop, num)`: 구간 [start, stop]을 균등하게 분할한 num개 지점에 대한 배열 생성
- `np.iinfo(type=)`: int, float 데이터 타입의 표현 가능한 수의 한계를 반환
- `np.linalg.solve(a, b)`: 선형 연립 방정식 풀이(a: 계수, b: 상수) 
- `np.vectorize(func)`: 함수를 element-wise하게 활용될 수 있도록 변환

    ```python
    >>> np.vectorize(lambda x: x-1)(np.array([1, 2, 3])) # 원소 하나에 대해 1을 빼는 연산 실행
    array([0, 1, 2])
    ```

- `배열.ndim`: 객체의 차원 반환
- `배열.itemsize`: 배열 내 자료형 메모리 크기(byte)
- `배열.size`: 배열 내 성분 개수
- 32bit 배열 + 64bit 배열: 결과값은 64bit 배열
#### Pandas | Python
- `pd.Categorical`: 컬럼 속성을 Categorical로 변환. Label Encoding을 진행할 떄 유용.
  
  ```python
  temp = pd.Series([10,20,30,20,10]).to_frame('cat')
  temp['cat'] = pd.Categorical(temp['cat']) # 해당 변수 type이 Categorical이 됨
  temp['cat_ID'] = temp['cat'].cat.codes # 각 클래스별 ID는 cat.codes 인스턴스를 호출하여 구함
  ```
#### datatime | Python

* `from datetime import datetime as dt` 로 사용하는게 편리
* `dt.strptime(date_string, format)`
* `dt.timedelta(hours, seconds, days=)` : datetime 객체에 시차를 주고자 할 때 사용

#### Essential | Python

- `iter()`: iterable 객체를 iterator로 변환. `next()` 함수를 통해 iterating이 가능ㅏ
```python
iterable_ = range(10)
iterator = iter(iterable_) # type: range_iterator
next(iterator) # 0, 1, 2, ... , 9 / 마지막 이후에는 StopIteration
```
- `all()`: iterable 객체의 모든 원소가 True인 경우 True
- `any()`: iterable 객체의 적어도 한 원소가 True인 경우 True
- `yield`: generator에 활용. 쥐고 있던 원소를 다 털어내면 아무 값도 뱉지 않고 에러도 나지 않음
```python
def gen():
    ls = range(10)
    for value in ls:
        yield value
temp = gen()
for i in range(temp):
    print(i) # 0, 1, 2, ... , 9
```

### Notions
* Name Mangling(=Name Decoration)
  - 함수를 선언하거나 전역 변수 등을 선언했을 때 컴파일 단계에서 일정한 규칙을 갖고 변경되는 것
  - Linker가 다른 Scope에 있는 같은 이름의 함수와 변수에 대해 구별할 수 있도록 하는 요소로, 컴파일러 입장에서 중요한 작업
  - 컴파일러는 함수에 대하여 함수의 이름, 파라미터 타입, Calling Convention 등을 사용하여 이름을 생성
* (Python)for문은 iterable 객체의 __next__() 메소드를 호출하는 역할을 수행
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

### Model

#### RNN | TensorFlow

* Input Shape: (batch_size, time steps, input length)

### Preprocessing
* Batch Normalization

### 



* Loss function
    * Custom Loss
        * [Stock Price Prediction](https://towardsdatascience.com/customize-loss-function-to-make-lstm-model-more-applicable-in-stock-price-prediction-b1c50e50b16c)

## Attitude
* 헷갈리는 함수 인지
* 무식한 접근이 나을 때도 많다.
* 디버깅 대충하지 말 것

## Reference
- [Name Mangling](https://thepassion.tistory.com/61)
- [Categorical Value Encoding 과 Mean Encoding](https://dailyheumsi.tistory.com/120)
