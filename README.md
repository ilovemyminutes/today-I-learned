# ✔I Love Today I Learned
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

#### matplotlib | Python

* 가상환경에서 글꼴 변경

* 다음과 같이 코드별로 글꼴 정보를 입력하여 변경. 가상환경에서 전사적인 변경 방법은 아직 찾지 못함

  ```python
  path = './fonts/AppleSDGothicNeoM.ttf'
  fontprop = fm.FontProperties(fname=path, size=18)
  plt.rc('font', family=font_name)
  
  plt.title('한글 제목', fontproperties=fontprop)
  plt.show()
  ```


#### re | Python

- Meta characters: `.` `^` `$` `*` `+` `?` `{` `}` `[` `]` `\` `|` `(` `)`

- Character Class(`[ ]`): `[ ]` 사이의 문자들과 매치

  - 예: `[abc]`

    - 'a': a가 포함되어 매치
    - 'before': b가 포함되어 매치
    - 'dude': 해당되는 것이 없어 매치 X

  - `[0-9]`: 0부터 9까지, `[a-c]` - a부터 c까지

  - `[^0-9]`: 숫자가 아닌 것들만 매치(^ - not)

  - `\d`: 숫자와 매치(=`[0-9]`)

  - `\D`: 숫자가 아닌 것과 매치(=`[^0-9]`)

  - `\s`: whitespace 문자와 매치(=`[ \t\n\r\f\v]`)

  - `\S`: whitespace 문자가 아닌 것과 매치(=`[^ \t\n\r\f\v]`)

  - `\w`: 문자 + 숫자와 매치(=`[^a-zA-Z0-9_]`)

    \*대문자로 사용된 것은 소문자의 반대

- Reference. [점프 투 파이썬 - 정규표현식](https://wikidocs.net/4308)

#### Essentials | Python

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

* `global`, `nonlocal`: 지역변수를 전역변수에 영향줄 수 있도록 해주는 명령어

    * `global`: 함수 내 함수로 겹겹이 쌓이더라도, `global`이 사용된 지역변수는 전역변수로 연결. 권장되지 않는 명령어

    * `nonlocal`: 사용된 함수의 바로 한 단계 바깥에 위치한 변수와 바인딩

        * 함수를 한 개 정의하고 전역변수에 영향을 주는 것은 불가능

            ```python
            x = 70
            def foo():
                nonlocal x
                x = 140
            foo()
            print(x) # SyntaxError: no binding for nonlocal 'x' found
            ```

    * Reference. https://devbruce.github.io/python/py-13-global,nonlocal/
    
* pyenv와 virtualenv는 다른 개념이다.

    * pyenv: 로컬 파이썬과 별개의 파이썬 버전을 마련하는 것
    * virtualenv: 기존 파이썬 패키지 폴더와 독립적인 파이썬 패키지 폴더를  마련하는 것. venv 간 파이썬 버전을 공유할 수 있음
    
* `string.isalnum()`: 문자열이 영어, 한글 또는 숫자로 구성되어 있으면 True, 아니면 False

* `string.isalpha()`: 문자열이 영어 또는 한글로 구성되어 있으면 True, 아니면 False

### Notions

* Name Mangling(=Name Decoration)
  - 함수를 선언하거나 전역 변수 등을 선언했을 때 컴파일 단계에서 일정한 규칙을 갖고 변경되는 것
  - Linker가 다른 Scope에 있는 같은 이름의 함수와 변수에 대해 구별할 수 있도록 하는 요소로, 컴파일러 입장에서 중요한 작업
  - 컴파일러는 함수에 대하여 함수의 이름, 파라미터 타입, Calling Convention 등을 사용하여 이름을 생성
  
* (Python)for문은 iterable 객체의 __next__() 메소드를 호출하는 역할을 수행

* 클래스 메서드 | Python

  * 인스턴스 메서드와 달리 self 인자를 전달하는 것이 아닌 cls(클래스 자기 자신)을 전달
  * 인스턴스 메서드는 인스턴스에 국한하여 데이터를 사용하나, 클래스 메서드는 인스턴스가 공유하는 클래스 데이터 활용 가능

  ```python
  class Store:
      def __init__(self, temp1, temp2):
          self.temp1 = temp1
          self.temp2 = temp2
  
      @classmethod
      def foo(cls, double):
          return cls(double, double)
      
      def foo2(self):
          return self.temp1 + self.temp2
  
  origin = Store(1,2)
  print(origin.foo2()) # 1 + 2 = 3
  
  shared = origin.foo(3) # 내부 인스턴스를 변경한 채로 새로운 객체에 할당
  print(shared.foo2()) # 3 + 3 = 6
  ```

  
## Data Visualization

### Matplotlib



### Seaborn



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
      
## DL

### Model

#### RNN | TensorFlow

* Input Shape: (batch size, time steps, input length)
* `TimeDistributed`: 각 time에서 출력된 output을 내부에 선언해준 layer와 연결해주는 역할

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
* 함수 내에 함수를 구성하는 걸 껄끄럽게 생각하지 말자
* 컴퓨터 언어도 언어임. 국룰을 따르자.

## Reference
- [Name Mangling](https://thepassion.tistory.com/61)
- [Categorical Value Encoding 과 Mean Encoding](https://dailyheumsi.tistory.com/120)
