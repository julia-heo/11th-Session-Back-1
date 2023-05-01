## 1. Django blogproject

1. 코드 Summary

models.py에 블로그 객체 생성 후 admin에 반영 <br>
CRUD 구현<br>
  R: url이 views의 함수 호출. views.py 함수에서 데이터를 객체의 묶음인 쿼리셋 형태로 html과 함께 반환하면 templates에서 하나하나 쪼개 출력<br>
  C: new.html에서 <form action"{% url 'create' %}" ... >으로 입력받은 정보 url로 전달. url이 blog.views.create 호출
      새로운 Blog객체에 입력받은 정보 저장 후 save()<br>
  D: delete 버튼에 'delete'링크 연결. delete url이 delete 함수 호출, delete()실행<br>
  U: update 버튼에 'update_page'링크 연결. 'update_page' url이 update_page 함수 호출, update.html반환<br>
    update.html에서 정보 입력 후 'update'링크 클릭, update함수 호출, 바뀐 정보로 save()수행<br>
  <br>
templates(html)에서 url호출. urls.py에서 해당 url이 views.py의 함수 호출. views.py의 해당 함수 수행(동작, html리턴)<br>


2. Key Changes
-


3. Reference
0406 Blog 세션 자료
  20230406 Blog #1(최유미).pdf
  20230406 Blog #2(최유미).pdf

4. Report
https://www.notion.so/0406-Blog-560f5695dc2a4a0b81b9e76a7c422663?pvs=4
