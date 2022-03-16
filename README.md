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

홈페이지 상단 내비게이션 메뉴에 User 드롭다운 버튼을 만들고 로그인 여부에 따라 드롭다운 메뉴를 구성. <br>
<img src="https://user-images.githubusercontent.com/99372311/158532611-7e0af2cb-f13c-40cd-a8ce-ad0b611b8e62.jpg" style="width:50%">

|로그인 전|로그인 후|
|:-:|:-:|
|![로그인전](https://user-images.githubusercontent.com/99372311/158534170-3242affa-0950-4599-9530-7093b686f144.jpg)|![로그인 후](https://user-images.githubusercontent.com/99372311/158534264-7a6ac49a-686f-4fff-91b6-85da96d22705.jpg)|<br>


로그인 후 메뉴를 확인하려면 우선 회원가입을 진행해야 한다.<br>
로그인 전 메뉴 중 Register 버튼을 누르면 회원가입 페이지가 나오고 정보들을 기입하여 가입하도록 만들었다.<br>
각 항목들은 기입하지 않거나 지정된 글자 수 이내로 기입할 시 경고가 표시되도록 조치를 취하였고 <br>
화면 상단의 아이콘은 부트스트랩 양식에서 아이콘 부분만 따와서 상황에 맞게 수정해주었다. 이는 후술할 다른 페이지에서도 적용했다.

