# K-Digital-Web 프로젝트
**참여자**<br>
2조_심상진<br><br>
**제작 목적**<br>
영화 소개 및 평점 부여 사이트 제작<br><br>
**활용 툴**
- **부트스트랩 템플릿**
https://startbootstrap.com/previews/modern-business <br>
- **Django 환경 셋팅**
https://goni99developer.tistory.com/3 <br>
- **Django 웹 생성**
https://goni99developer.tistory.com/4 <br>
- **Django ORM 적용**
https://goni99developer.tistory.com/5 <br>
- **PythonAnywhere 적용**
https://goni99developer.tistory.com/6 <br>
- **차트 적용**
https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/chart-update <br>

- **summernote 적용**

https://summernote.org/getting-started/#without-bootstrap <br>

**시스템 구성도 및 ERD**

https://github.com/Jokwanhee/K_DigitalWebProject 의 README.md참조


**본인이 했던 작업**
- 웹 페이지 회원가입 및 로그인 기능 구현
- 로그인 시 회원 정보 수정 및 탈퇴 기능 구현

홈페이지 상단 내비게이션 메뉴에 User 드롭다운 버튼을 만들고 로그인 여부에 따라 드롭다운 메뉴를 구성. <br><br>
<img src="https://user-images.githubusercontent.com/99372311/158532611-7e0af2cb-f13c-40cd-a8ce-ad0b611b8e62.jpg" style="width:50%">

|로그인 전|로그인 후|
|:-:|:-:|
|![로그인전](https://user-images.githubusercontent.com/99372311/158534170-3242affa-0950-4599-9530-7093b686f144.jpg)|![로그인 후](https://user-images.githubusercontent.com/99372311/158534264-7a6ac49a-686f-4fff-91b6-85da96d22705.jpg)|<br>


로그인 후 메뉴를 확인하려면 우선 회원가입을 진행해야 한다.<br>
로그인 전 메뉴 중 Register 버튼을 누르면 회원가입 페이지가 나오고 정보들을 기입하여 가입하도록 만들었다.<br>


<img src="https://user-images.githubusercontent.com/99372311/158537746-5c6c80e6-eb2d-4445-86fe-cc24493489fe.jpg" style="width:50%">

각 항목들은 기입하지 않거나 지정된 글자 수 이내로 기입할 시 경고가 표시되도록 조치를 취하였고 <br>
화면 상단의 아이콘은 부트스트랩 양식에서 아이콘 부분만 따와서 상황에 맞게 수정해주었다. 이는 후술할 다른 페이지에서도 적용했다.<br>
회원 가입이 완료되면 가입 완료했으니 로그인 해달라는 알림창과 함께 홈페이지로 이동하게 된다.<br>
가입한 회원의 정보는 데이터베이스에 저장이 된다.<br>

<img src="https://user-images.githubusercontent.com/99372311/158542768-fedb8071-4897-4dd9-b625-5ddb5f1ccbde.jpg" style="width:50%">

이제 로그인을 할 차례다.Login 버튼을 눌러 해당 화면으로 이동한다.<br>
<img src="https://user-images.githubusercontent.com/99372311/158539239-c339e4b5-6870-40ce-91fa-8a8765204cd5.jpg" style="width:50%"><br>
아이콘은 열쇠모양으로 바꿔주었고 ID랑 비밀번호를 입력할 수 있는 양식 을 만들었다.<br>
여기서 로그인 실패시 알림창이 뜨고 성공시 해당 ID를 django에서 제공하는 sessionid에 저장한 뒤 홈페이지로 이동한다.<br><br>
sessionid가 저장되면 사이트 메뉴의 User 버튼이 바뀌고 앞서 말했듯이 드롭다운 메뉴가 바뀐다.<br>
비밀번호 찾기 기능까지 구현했고 이는 나중에 후술하기로 한다.<br><br>

로그인 성공시 드롭다운 메뉴가 사용자 ID, Logout으로 바뀌는데 로그아웃을 선택하면 sessionid값을 삭제하여 말 그대로 로그아웃을 하게 된다.<br>
그리고 홈페이지로 이동. 사용자ID를 클릭시 사용자가 가입 할 때 입력했던 정보들을 열람하게되며 여기서 탈퇴와 정보 수정이 가능하다.<br><br>
탈퇴버튼을 누르면 먼저 sessionid를 삭제해 로그아웃을 한 다음 해당 아이디를 데이터베이스에서 검색해 해당하는 요소를 전부 삭제하게 된다.<br>
즉 회원 정보를 모두 삭제한다.<br>
dark4로 접속해 회원 탈퇴를 해 보겠다. 우선 회원 정보로 들어간다.<br>
<img src="https://user-images.githubusercontent.com/99372311/158544667-ff3baea8-6bbe-4ca7-9be4-243a2aa2ef8b.jpg" style="width:50%">
<br>여기서 회원 탈퇴를 누르면<br><br>
<img src="https://user-images.githubusercontent.com/99372311/158544745-2f342788-27a1-4467-9008-5852e09636e1.jpg" style="width:50%"><br>
명단들 중 dark4 아이디에 해당하는 행이 사라졌음을 알수있다.
