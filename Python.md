# Python

## NumPy

***`arr`: 넘파이 배열

`np.random.rand(d1, d2, ... , dn)`: n차원 배열 생성. 각 값은 \[0, 1)

`np.arange(start, stop, step)`: `range()`와 같은 역할 + 실수값의 step 사용 가능

`np.linspace(start, stop, num)`: 구간 [start, stop]을 균등하게 분할한 num개 지점에 대한 배열 생성

`np.iinfo(type=)`: int, float 데이터 타입의 표현 가능한 수의 한계를 반환

`np.linalg.solve(a, b)`: 선형 연립 방정식 풀이(a: 계수, b: 상수) 

`np.vectorize(func)`: 함수를 element-wise하게 활용될 수 있도록 변환

```python
>>> np.vectorize(lambda x: x-1)(np.array([1, 2, 3])) # 원소 하나에 대해 1을 빼는 연산 실행
array([0, 1, 2])
```

`arr.ndim`: 객체의 차원 반환

`arr.itemsize`: 배열 내 자료형 메모리 크기(byte)

`arr.size`: 배열 내 성분 개수

`np.argsort(arr)`: 배열을 정렬했을 때, 순서가 바뀐 인덱스 리스트를 반환

32bit 배열 + 64bit 배열: 결과값은 64bit 배열

## Pandas

***`df`: 판다스 데이터프레임, `srs`: 판다스 시리즈

`pd.Categorical`: 컬럼 속성을 Categorical로 변환. Label Encoding을 진행할 떄 유용.

```python
temp = pd.Series([10,20,30,20,10]).to_frame('cat')
temp['cat'] = pd.Categorical(temp['cat']) # 해당 변수 type이 Categorical이 됨
temp['cat_ID'] = temp['cat'].cat.codes # 각 클래스별 ID는 cat.codes 인스턴스를 호출하여 구함
```

`df.itertuples(index: bool)`: 데이터프레임의 각 row를 튜플 형태로 iterating. iterating되는 객체는 `pandas.core.frame.Pandas` type을 지님

```python
for row in df_ratings.itertuples(index=True): # index를 False로 설정할 경우 index 미포함
    print(row)
'''
...
Pandas(Index=30386, userId=212, movieId=59369, rating=3.0)
Pandas(Index=30387, userId=212, movieId=59784, rating=4.0)
Pandas(Index=30388, userId=212, movieId=60069, rating=4.0)
Pandas(Index=30389, userId=212, movieId=61024, rating=2.5)
Pandas(Index=30390, userId=212, movieId=64034, rating=3.0)
...
'''
row[0] # 30390 <- 인덱싱을 통한 접근
row.Index # 30390 <- 키값을 통한 접근
```

`df.iterrows()`: 데이터프레임의 각 row를 `(index, srs)`의 형태로 iterating. 

```python
for row in df_ratings.iterrows():
    print(row)
'''
...
(2658, userId       19.0
movieId    2052.0
rating        2.0
Name: 2658, dtype: float64)
(2659, userId       19.0
movieId    2053.0
rating        2.0
Name: 2659, dtype: float64)
...
'''
```



## matplotlib

* 가상환경에서 글꼴 변경

* 다음과 같이 코드별로 글꼴 정보를 입력하여 변경. 가상환경에서 전사적인 변경 방법은 아직 찾지 못함

  ```python
  path = './fonts/AppleSDGothicNeoM.ttf'
  fontprop = fm.FontProperties(fname=path, size=18)
  plt.rc('font', family=font_name)
  
  plt.title('한글 제목', fontproperties=fontprop)
  plt.show()
  ```

## Built-in Modules & Functions

### re

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

### datatime

* `from datetime import datetime as dt` 로 사용하는게 편리
* `dt.strptime(date_string, format)`
* `dt.timedelta(hours, seconds, days=)` : datetime 객체에 시차를 주고자 할 때 사용

`iter()`: iterable 객체를 iterator로 변환. `next()` 함수를 통해 iterating이 가능ㅏ

```python
iterable_ = range(10)
iterator = iter(iterable_) # type: range_iterator
next(iterator) # 0, 1, 2, ... , 9 / 마지막 이후에는 StopIteration
```

`all()`: iterable 객체의 모든 원소가 True인 경우 True

`any()`: iterable 객체의 적어도 한 원소가 True인 경우 True

`yield`: generator에 활용. 쥐고 있던 원소를 다 털어내면 아무 값도 뱉지 않고 에러도 나지 않음

```python
def gen():
    ls = range(10)
    for value in ls:
        yield value
temp = gen()
for i in range(temp):
    print(i) # 0, 1, 2, ... , 9
```

`global`, `nonlocal`: 지역변수를 전역변수에 영향줄 수 있도록 해주는 명령어

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

`string.isalnum()`: 문자열이 영어, 한글 또는 숫자로 구성되어 있으면 True, 아니면 False

`string.isalpha()`: 문자열이 영어 또는 한글로 구성되어 있으면 True, 아니면 False

## etc

pyenv와 virtualenv는 다른 개념이다.

* pyenv: 로컬 파이썬과 별개의 파이썬 버전을 마련하는 것
* virtualenv: 기존 파이썬 패키지 폴더와 독립적인 파이썬 패키지 폴더를  마련하는 것. venv 간 파이썬 버전을 공유할 수 있음

Name Mangling(=Name Decoration)

- 함수를 선언하거나 전역 변수 등을 선언했을 때 컴파일 단계에서 일정한 규칙을 갖고 변경되는 것
- Linker가 다른 Scope에 있는 같은 이름의 함수와 변수에 대해 구별할 수 있도록 하는 요소로, 컴파일러 입장에서 중요한 작업
- 컴파일러는 함수에 대하여 함수의 이름, 파라미터 타입, Calling Convention 등을 사용하여 이름을 생성
- Reference. [Name Mangling](https://thepassion.tistory.com/61)

for문은 iterable 객체의 \__next__() 메소드를 호출하는 역할을 수행한다.

클래스 메서드

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

for문은 적을 수록 좋다.

- 같은 내용의 연산이더라도 loop를 적게 하는 것이 무조건 빠름

- 여러 리스트를 공유된 loop에서 만드려고 할 때는 list comprehension이 아닌 일반적인 for loop를 활용하는 것이 좋다고 한다.

  - Reference. [Python list comprehensions to create multiple lists duplicate](https://stackoverflow.com/questions/21023482/python-list-comprehensions-to-create-multiple-lists)

  ```python
  def foo():
      a1, a2 = [], []
      for i in range(10):
          a1.append(i)
      for j in range(10):
          a2.append(j)
      return a1, a2
  
  %timeit foo # 10000000 loops, best of 3: 28.4 ns per loop
  
  def foo():
      a1, a2 = [], []
      for i in range(10):
          a1.append(i)
          a2.append(j)
      return a1, a2
  
  %timeit foo # 10000000 loops, best of 3: 28 ns per loop
  ```

길이를 반복적으로 호출할 경우 미리 할당하는 것이 좋다

- *`len()`의 시간 복잡도는 O(1)이지만, 반복적으로 호출할 때는 `len()`값을 변수에 할당해둔 뒤, 해당 변수를 불러오는 것이 좋음*

- 라고 생각했는데 다시 측정해보니 별 차이 없음


함수명과 해당 함수 내 variable의 이름이 같아도 문제가 발생하지 않는다

```python
def foo():
    foo = 1
    return foo

temp = foo()
print(temp, type(foo), foo) # 1 <class 'function'> <function foo at 0x7f9bf305b488>
```

`max(dict, key=dict.get)`: 딕셔너리의 value값이 가장 큰 키값을 추출