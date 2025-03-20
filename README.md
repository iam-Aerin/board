# Django 프로젝트 설정 가이드

---

## 0. 기본 설정

### .gitignore 설정
Django 프로젝트를 시작할 때, 불필요한 파일을 git에 올리지 않도록 `.gitignore` 파일을 설정합니다.

#### 예시 (`.gitignore`)
```
# 가상환경 폴더
venv/

# 파이썬 캐시 파일
__pycache__/

# 환경 변수 파일 (보안)
.env

# Django 마이그레이션 파일
*.pyc
*.pyo
*.sqlite3
```

### 가상환경 설정 (venv)
운영체제에 따라 가상환경을 설정합니다.

#### Windows
```sh
python -m venv venv
venv\Scripts\activate
```
#### macOS / Linux
```sh
python -m venv venv
source venv/bin/activate
```

---

## 1. Django 프로젝트 설정

### Django 설치
```sh
pip install django
```

### Git 초기화
```sh
git init
git add .
git commit -m "프로젝트 초기 설정"
```

### Django 프로젝트 생성
```sh
django-admin startproject <pjt-name> <path>
```
예시:
```sh
django-admin startproject first_pjt .
```
> 현재 디렉토리에 `first_pjt`라는 프로젝트를 생성합니다.

### 서버 실행 (서버 종료: `Ctrl + C`)
```sh
python manage.py runserver
```
> `manage.py` 파일을 실행하여 개발 서버를 실행합니다.

---

## 2. 앱 생성 및 설정

### 앱 생성
```sh
django-admin startapp <app-name>
```
예시:
```sh
django-admin startapp first_app
```

### 앱 등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    'first_app',
]
```

---

## 3. Django MTV 패턴

Django는 **MTV (Model - Template - View) 패턴**을 따릅니다.

- **Model**: 데이터베이스를 관리하는 곳 (`models.py`)
- **Template**: HTML을 포함한 프론트엔드 (`templates/` 폴더)
- **View**: 비즈니스 로직을 처리 (`views.py`)

### 폴더 및 파일 구조
```
first_pjt/
│── first_app/
│   ├── migrations/
│   ├── templates/      # HTML 파일이 들어가는 폴더
│   │   ├── index.html
│   ├── models.py       # 데이터 모델 정의
│   ├── views.py        # 화면(View) 로직 처리
│   ├── urls.py         # URL 매핑
│── first_pjt/
│   ├── settings.py     # Django 설정 파일
│   ├── urls.py         # 프로젝트 전체 URL 설정
│── manage.py           # Django 실행 파일
```

---

## 4. 기능 추가 흐름

1. `urls.py` 수정 - URL 라우팅 설정
2. `views.py` 수정 - 화면 로직 처리
3. `templates/` 폴더에 `HTML` 추가 - 템플릿 렌더링


---

##  마무리
- `.gitignore` 설정 후 **가상환경** 생성 및 활성화
- Django 설치 후 **프로젝트 생성**
- **앱 생성** 및 `settings.py`에 등록
- `urls.py` → `views.py` → `templates/` 흐름으로 개발 진행


`python manage.py makemigrations`
`python manage.py migration`
sql 세상으로 python 코드들을 보내줌.

`admin.py` 파일에 내용을 적고 `python manage.py createsuperuser` 로 계정을 생성함 => url접속후 /admin 으로 페이지에 접속하고 관리자 모드로 게시물을 관리
