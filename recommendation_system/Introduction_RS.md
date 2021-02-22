# Introduction to Recommender System

### Content-based RS

아이템에 대한 풍부한 정보(영화 상품의 장르, 감독, 배우 등)가 유저 간 상호작용/피드백보다 중요하게 작용하는 방법



### Collaborative Filtering, CF

가정: '사용자의 지난 취향은 앞으로도 이어진다'

특징: 유저의 지난 취향/선호도 정보를 제외하고는 어떤 정보도 필요하지 않음

유저 취향은 2가지로 나타낼 수 있음

- Explicit Rating: 표면적 평가. 아이템에 대한 유저의 직접적 평가. 영화에 평점을 매긴 것. 가장 직접적인 피드백
- Implicit Rating: 함축적 평가. 아이템에 대한 유적의 간접적 평가. 페이지 뷰 수, 클릭 수 등

Nearest Neighborhood

- CF의 가장 스탠다드한 방법론으로, User-based CF와 Item-based CF의 두 가지 방법이 있음

- User-based CF: *'한 아이템에 대해 두 유저의 평가가 비슷하면 두 유저는 유사하다'*

  - 절차
    1. 타깃 유저 i와 그 외의 유저 간 유사도를 측정

    2. 상위 X명의 유사한 유저를 추출

    3. 추출한 유저에 대한 유사도를 가중 평균

  - 편중의 문제

    - 사람들마다 평가 기준이 다르겠지만, 모든 상품들에 대해 어떤 사람은 전반적으로 높은 평가를, 어떤 사람은 전반적으로 낮은 평가를 매길 수도 있음 => bias 상승 위험
    - bias 문제를 방지하기 위해 점수를 예측하는 과정에서 추출한 사람들의 모든 상품에 대한 평점 평균을 각 평점에 뺀 뒤, 타깃 유저의 평점을 계산하고 타깃 유저의 모든 상품에 대한 평점 평균을 더함

    ![user_based_CF](C:\Users\iloveslowfood\Documents\workspace\iloveTIL\recommendation_system\images\user_based_CF.jpg)

  - 유사도 측정 방식: 피어슨 상관계수, 코사인 유사도

- Item-based CF: *'한 유저가 두 아이템에 비슷한 평점을 매겼다면 두 아이템은 유사하다'*

  - 절차
    1. 한 유저로부터 평가가 가장 유사한 X개의 상품을 추출
    2. 추출한 상품들의 평점을 가중 평균하여 타깃 유저의 해당 상품에 대한 평점을 예측
  - 장점: 안정성 - 시간이 많이 흐르더라도 급격히 예측값이 변하지 않음
  - 단점
    - Sparsity 핸들링의 어려움 - 아무도 특정 상품에 대해 평가를 내리지 않았을 경우, 타깃 유저의 해당 상품에 대한 평점 예측이 불가능
    - 연산의 비효율성 - 유저 수와 상품 수가 늘어날 수록 연산이 비효율적



> References

- [Introduction to Recommender System](https://towardsdatascience.com/intro-to-recommender-system-collaborative-filtering-64a238194a26)

