# Natural Entity Recognition

### 국립국어원 모두의말뭉치 NER 데이터셋 구조

> 최상위

`id`: 텍스트 데이터셋 ID

`metadata`

- `annotation_level`: 어노테이션 수준
- `category`: 텍스트 내용의 카테고리
- `creator`: 데이터 제공처/자
- `distributor`: 관련처/자
- `sampling`: 샘플링 방식
- `title`: 데이터 제목
- `year`: 제작 년도

**`document`: 텍스트의 도큐먼트 리스트**

> 하위: `document`

-  `id`: document ID
- `metadata`: 도큐먼트 메타 데이터
- **`sentence`: 도큐먼트 내 문장 리스트**

> 하위: `sentence`

- `NE`: Named Entity 정보 리스트에 대한 key
- `begin`: Named Entity 시작 위치
- `end`: Named Entity 마지막 위치
- `form`: Named Entity 문자열
- `id`: 해당 Named Entity ID
- `label`: 해당 Named Entity 레이블
- `form`: 문장 문자열
- `id`: 문장 ID
- **`word`: 문장 내 각 단어 정보**

> 하위: `word`

- `begin`: 헤딩 단어 시작 위치
- `end`: 해당 단어 마지막 위치
- `form`: 단어 문자열
- `id`: 단어 ID