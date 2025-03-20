Django
0. setting
.gitignore
windows, python, macOS, Django

가상환경 설정 (venv)
python -m venv venv source venv/Scripts/activate

README.md 작성하는 습관 들이기
1. Django 프로젝트
django 설치
pip install django

git init
git add .
git commit -m "내용"

프로젝트 생성
django-admin startproject <pjt-name> <path>
django-admin startproject first_pjt .` : 프로젝트의 이름이 first_pjt고 그걸 현재 폴더에 만들거야 (.)
- 프로젝트의 이름은 보통 서비스의 이름으로 짓기

서버 실행 (종료: ctrl + c)
python manage.py runserver
manage파일을 실행해요~

앱 생성
django-admin startapp <app-name>
앱등록 (settings.py)
INSTALLED_APPS = [
    ...,

]
`first_apps'를 first_pjt의 setting.py에 추가함.

mtv

templates (폴더), models.py, views.py

fist_app안에 새로운 폴더 templates -> 그 안에 index.html
기능 추가 흐름의 순서서

urls.py => views.py => templates (html 추가)
