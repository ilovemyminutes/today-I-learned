# Contents-based Recommendation System

##### 유저 프로필과 아이템 프로필을 바탕으로 상품을 추천하는 추천 방법론

- 유저 프로필: 유저에 대한 직·간접적 정보
- 아이템 프로필: 상품에 대한 속성
  - 영화의 장르, 감독 등
- 유저 프로필에 대한 속성과 아이템 프로필의 속성은 동일한 형태

##### 특징 및 장단점

- 유저의 활동이 활발할 수록, 활용하는 속성이 풍부할 수록 추천 정확도가 높아짐
- 텍스트 등 비정형 데이터를 활용하는 경우가 많음(뉴스 추천, 웹페이지 추천 등)

- 장점: 유저와 상품의 속성/특성만을 고려하기 때문에 유저 수가 적어서 발생하는 콜드 스타트 문제
- 단점:
  - 신규 유저 유입에 대한 콜드 스타트 문제는 해결하기 어려움
  - 상품의 속성, 유저의 속성만을 고려하기 때문에 신선하지 않은 추천이 이루어질 수 있음

##### 구축 과정

- Offline
  - Data Preprocessing: 데이터 전처리 및 속성 추출: 데이터를 학습 가능한 형태로 정제(domain-specific)
  - Content-based learning: 유저와 상품의 속성을 고려하여 추천할 상품 리스트업
- Online
  - Recommendation: 추천 정보 제공

##### 예시

- NOTE - *TF-IDF*: *'특정 문서에는 자주 등장하는데, 모든 문서를 통틀어서는 적게 등장한다면 중요한 단어일 것이다'*

  <img src="C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226175543557.png" alt="image-20210226175543557" style="zoom:67%;" />

  - 많은 문서에서 등장한 특정 단어들의 중요도를 매기기 위한 지표
    - 데이터로부터 상품 속성을 추출하고, 특정 속성에 대한 중요도를 매기기 위해 사용
  - tf(t, d): 한 문서 d 내에서 단어 t가 등장한 횟수를 의미
  - idf(t, D): df(t, D)의 역수
    - df(t, D): 문서 집합 D에서 단어 t가 등장한 문서의 수
  - TF-IDF: tf(t, d) x idf(t, D)
    - 단어가 해당 문서 내에서 등장하는 빈도, 모든 문서 내에서 등장하는 빈도를 반영한 중요도

- 예시 상황: 유저에게 10개의 article(상품) 중 추천할 만한 article을 선별![image-20210226181208303](C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226181208303.png)

  - 유저로부터 얻은 정보: 일부 article에 대한 좋아요(+1)/싫어요(-1) 기록
  - 상품으로부터 얻을 수 있는 정보: 'Big Data', 'R', 'Python' 등의 사전 정의된 속성(attribute)에 대해 각각 상품들이 해당 속성을 가졌는지 여부

1. Normalize

   ![image-20210226181914430](C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226181914430.png)

   - 각 상품(article)의 벡터 길이가 1이 되도록 정규화
   - 벡터화된 각 상품의 벡터 길이가 다르기 때문에 스케일을 맞춰주는 작업

2. 유저 프로필 추출

   ![image-20210226182125994](C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226182125994.png)

   - 유저 각각이 사전에 좋아요/싫어요 했던 기록을 바탕으로 해당 상품 벡터를 가중합하여 유저 프로필을 추출
   - 유저 각각 좋아요/싫어요를 표시했던 article만을 활용
   - 각 성분은 유저가 해당 속성에 대해서 얼마나 선호하는 지를 나타냄

3. IDF 계산

   <img src="C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226183125750.png" alt="image-20210226183125750" style="zoom:80%;" />

   - 각 속성이 10개의 article에 걸쳐 몇 번 등장했는지에 따른 IDF값 측정
   - 'big data'의 IDF
     - 10개의 article에서 2번 등장 => DF = 2
     - ![](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+IDF+%3D+log%28%7B%5Cfrac+%7B2%7D+%7B10%7D%7D%29%5E%7B-1%7D) 

   

4. 추천 가능성 추정

   ![image-20210226183445024](C:\Users\iloveslowfood\AppData\Roaming\Typora\typora-user-images\image-20210226183445024.png)

   - 각 속성별 IDF를 가중치로, 유저 속성 벡터와 상품 속성 벡터를 element-wise곱한 뒤 가중합

   - 유저 1의 Article 1에 대한 추천 가능성

     ![](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+0.6989%280.5773+%5Ctimes+1.2844%29+%2B+0.6989%280+%5Ctimes+-0.5773%29+%2B+0.5228%280.5773+%5Ctimes++0%29%2B+0.3979%280+%5Ctimes+0.1297%29+%2B+0.6989%280.5773+%5Ctimes+0.5773%29+%3D+0.7513)

     



> Attitude & Tips

Networks and Crowds and Markets

Linked