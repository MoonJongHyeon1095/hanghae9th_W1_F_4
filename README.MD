# 항해99 9기 1주차 F반 4조 
- 미니 프로젝트 "분서갱유"

## 와이어 프레임
### 활용 사이트 : https://excalidraw.com
- Starting Assignment : https://purple-nation-d93.notion.site/99-9-F-4-4e3159d0a9204f34a4b2f9df74ed3594
- 9기 미니 프로젝트 대시보드 : https://docs.google.com/spreadsheets/d/1AMbQhhldjrD2fnw-15f7gQFmDt0OWAyzuipKJRiaVCQ/edit#gid=222246930

## API 설계
### DB 구성

users

- _id : 회원 고유 아이디. (MongoDB ObjectId)
- email : 로그인 아이디. (이메일 주소 형식 확인)
- password : 비밀번호. (암호화하여 저장)
- username : 서비스 내에서 표시되는 사용자 이름
- image : 프로필 이미지 이름
- image_data : 프로필 이미지 실제 데이터(경로)
- reviews : 작성한 리뷰. [Arrays: review_id]
- likes : 좋아요 누른 책. [Arrays: book_id]

books

- _id : 책 고유 아이디. (MongoDB ObjectId)
- title : 책 제목
- image : 표지 이미지
- author : 작가
- pubdate : 출판년도
- publisher : 출팔사
- discount : 판매 가격
- description : 요약 줄거리
- isbn : 국제표준책번호
- likes : 좋아요. [Array: user_id]
- reviews : 책 리뷰. [Array: review_id]

reviews

- _id : 리뷰 고유 아이디. (MongoDB ObjectId)
- book_id : 리뷰가 달린 책의 고유 아이디
- username : 리뷰를 작성한 사용자 이름
- content : 리뷰 내용
- rating : 별점
- time : 작성/수정 시간. (unix time으로 저장)

![Untitled](https://user-images.githubusercontent.com/109948801/191673539-dd40225c-4dd4-4b5f-ace3-f3ec3eec847a.png)




## Git 관리 전략
![git전략](https://user-images.githubusercontent.com/109948801/191664853-12f0a919-aab1-4877-9b2e-ee8025a335f1.png)
- 각자 최신 메인을 Pull 받아 local main 에서 작업 aka N
- 이후 origin/main 에서 임의의 브랜치 X를 만들기 (소스트리와 같으 local 환경이 아닌, github에서!)
- 1) N을 X에 Push
- 2) origin/main 에서 X로 Pull -> github에서 충돌검사, 예컨대 origin/main을 지키기 위한 서스펜션
- 3) X를 origin/main 으로 merge
- 4) git에 익숙치 못하 인원들을 위한 일종의 우회전략

## 회고
### 로그인 및 회원가입기능 관련

1. path variable 경로 혼동 문제 

- a) api > user.py > user_bp = Blueprint("user", __name__, url_prefix="/user") 

- b) 상기 엔드포인트에서  url_prefix="/user" 지정된 프리픽스 값을 간과함. 클라이언트 코드에서 url 경로 잘못 지정.


2. Jquery load 메서드로 로그인 창 모달 기능구현

- a) 잘못된 사례 : 
`<li><a onclick="$().load('/modals/signin.html', [activateModal(), complete] )">로그인</a></li> `


- b) load 메서드의 매개변수 형태 혼동 

- 일단 모양이 예쁘지 않다. 

- 매개변수 load 메서드의 매개변수는 1) url, 2) data, 3) 콜백함수(complete로 이름이 지정되어 있음) 

- data와 같은 다른 매개변수를 생략하고 순서를 건너뛸 요량이면, 지정된 이름(complete) 으로 함수를 불러주어야 함 

- 혹은 아래의 형태로 익명 함수 선언을 해주어야 함 
- ` $().load('url', function(){} ) `

- 따라서 아래와 같은 함수호출은 곤란하다. 
- ` $().load('/modals/signin.html', activateModal())`

- load 메서드의 콜백함수가 아니라, 기껏 load로 가져왔더니만 곧바로  다른 함수를 시행하라는 이상한 뜻이 되어 버리는 것이다.
 
- c) 해결된 형태 : 
` <li><a onclick="$('#section-post').load('/user/sign_in', complete=activateModal )">로그인</a></li> `


3. 회원가입 서버 에러  

- a) 몽고DB로 회원가입 데이터를 넘기는 데에 있어 서버 에러가 발생 

- b) certifi 를 임포트한 후 tls 통신을 무시(?) 하는 모종의 코드로 해결
 

4. flask 문제 

- a) 각종 환경변수를 추가하여 해결했으나 왜 해결됐는지 명확하지 않음 

- b) 이후 파이참 실행 구성편집으로 DEBUG 체크를 해주는 것으로 해결 


5. 3과 4로 인한 git 에러  

- a) 3과 4로 인해 추가된 구문들은 중요한 파일들에 포함되어 있음. 때문에 커밋하거나 푸시하기에도, 그렇다고 gitignore에 넣기에도 곤란함. 

- b) 3은 그냥 해당 코드를 팀원들과 공유하는 것으로 해결.  

### 샘플
- 깃강의 강사의 샘플 : https://github.com/siyoungoh/til
- 샘플 폴더 https://github.com/siyoungoh/til/tree/main/sample
- 회고 https://github.com/siyoungoh/til/blob/main/sample/retrospective.md 

-----
항해99 9기 F반 4조 1주차 미니프로젝트 레포지토리


