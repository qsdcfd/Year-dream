
### 1. [NOSQL의 대표 데이터 베이스인 MongoDB를 실습](https://github.com/qsdcfd/Year-dream/tree/TIL/Example/MongoDB)

보통 우리는 SQL을 통해서 데이터베이스에 접근 후에 데이터 수정 및 추출을 하는 것이 익숙할 것입니다.

허나, 재미있는 것은 실제 데이터를 분석하고 추출할 때 SQL을 사용하지 않고 다른 방법을 사용합니다. 그것이 바로 몽고DB입니다.

이번 이어드림에서 첫 실습은 바로 파이썬으로 몽고디비를 활용하여 데이터 베이스를 생성, 추가 그리고 조건에 맞게 추출했습니다.

이제 그 코드에 관해서 이야기하겠습니다.


### CODE

1. MongoDB회원가입하기

   MongoDB의 Altas를 활용하여 Databse 만들었습니다.

2. DB의 링크를 가져와서 Python으로 설정

   mongo_path = "링크"
 
3. 라이브러리 호출 및 변수명 할당

4. DB생성

5. DB추출 및 추가

6. 조건에 맞게 DB에서 데이터 값 추출하기

- and

- $or 

- $gte

7. API를 불러와서 text형태로 부르기 혹은 json파일 형태로 부르기



<br>

### 2. [Flask 실습](https://github.com/qsdcfd/Year-dream/tree/TIL/Example/Flask)

1. [정적routing실습](https://github.com/qsdcfd/Year-dream/blob/TIL/Example/Flask/main%20(1).py)

   데코레이션을 활용하여서 route() 설정

   함수 구문을 활용하여 지정 주소에 문구 삽입

   URI타고 들아가서 문구 확인

   외부 API를 활용하여 json파일 가져오기

   추가적으로 이름을 삽입한 후에 그 이름과 함께 출력

2. [rendering실습](https://github.com/qsdcfd/Year-dream/blob/TIL/Example/Flask/main%20(1).py)

   html문서를 미리 작성 후에 연동 시키기

   메인 페이지에 html문서 내용 띄우기

3. [동적 라우팅 실습](https://github.com/qsdcfd/Year-dream/blob/TIL/Example/Flask/main.py)
  
   신발 가격과 통화량에 대한 내용
   
 ![image](https://user-images.githubusercontent.com/86671456/162491002-410d1bae-5a54-4ee6-9fb2-14363584feb9.png)

![image](https://user-images.githubusercontent.com/86671456/162491116-e1a549f3-612f-4aa7-915d-9f95b4dabb36.png)

![image](https://user-images.githubusercontent.com/86671456/162491141-4d9f013f-24bd-4deb-8bde-da0e3f380295.png)


<br>

### 3. [데이터 크롤링 실습](https://github.com/qsdcfd/Year-dream/blob/TIL/Example/Crawler/04_python_crawler%20(2).ipynb)

   웹 크롤링의 정의
   
   HTML, CSS의 활용
   
   API,requests, BeautifulSoup를 활용하여 데이터 크롤릴
   
   html.select()를 사용하여 데이터 전처리 
   
   Pandas를 이용하여 DataFrame 형성 및 Seaborn를 활용한 시각화
   
   사례
   
   - 드라마: 줄거리 추출
   - 키워드별로 헤드라인 뽑기
   - 하이퍼 링크 걸어서 추출
   - 로또번호
  
  
  동적 크롤링
  
  사례
  
  - 주가데이터 가져오기 및 Pandas, Numpy를 활용하여 DataFrame 구축 후 시계열 시각화
  - 네이버 데이터랩 인기 검색어 크롤링

   API 활용
   
   - 파파고 API
   - 공공데이터 API

