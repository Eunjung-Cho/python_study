
# EDA WITH PYTHON 
---
studying source from : https://www.udemy.com/course/python-for-statistical-analysis/
---

#### **EDA란 : Exploratory Data Analsis 탐색적 데이터 분석**
- 데이터를 시각적으로 탐색
- 데이터와 데이터 내의 관계 파악
- 데이터의 특성 파악


#### 1. 데이터 로드 하기
  1) 수동으로 파일 로드
  2) numpy.loadtext : 모든 숫자가 동일한 유형인 정수의 배열과 같은 간단하고 서로 같은 종류의 파일에 적용할 수 있다. 
  3) numpy.genfromtxt: 서로 다르 종류의 파일들을 처리할 수 있다. -> 2번보다 좀 더 유연함 (열 생성, 열에 이름 추가, 해당열에 데이터 유형 지정)
  4) pandas.read_csv: 방대한 데이터 셋으로 작업하는 경우 파일의 압축을 풀 필요가 없고 유연성이 뛰어나다. 
  5) pickle: 기계 언어가 파일이 직접 저장하는 바이너리이다. 따라서 꼭 2차원(행,열) 데이터일 필요가 없다. 3,4차원 데이터를 저장할 수도 있고 딕셔너리나 작업을 수행하는 객체를 저장할 수도 있다. -> 큰 데이터셋이나 미묘한 구조의 파일을 다룰 때 주로 사용
