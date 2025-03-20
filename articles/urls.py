# 이 파일은 원래 존재하지는 않았고, 내가 따로 new file로 추가해준  `urls.py` 파일임. 
# settings.py에서 include('articles.urls') 라는 함수로 이 urls.py의 경로가 반복되서 사용될 수 있도록 만들어줌. 

from django.urls import path
# 이제 path 앞에는 articles를 빼고 적어도된다. 
from . import views
# 현재 폴더에 있는 views를 가져와요. 

app_name = 'articles'
# 지금 app이 하나 여서 파악이 쉽지만
# 만일, app이 여러개 생기고, 그 안에도 detail이라는 이름을 가진 경로가 있다면
# 헷갈릴 수 있기 때문에
# app_name 설정까지 추가해줌.

# => base.html에 nav가 동작하게끔 넣어줌. 
#  <a class="navbar-brand" href="{% url 'articles: index' %}">  이 부분

urlpatterns = [
    # index = 'articles/' python 스럽게 표현해보자면 
# Read

    path('', views.index, name='index'),
    # name뒤에는 경로에 대한 이름을 지정해줌
    # 유지보수를 편하게 하기 위해서
    path('<int:id>/', views.detail, name='detail'),
    # ''비어 있는 string=> articles경로를 포함하고 있구나.
    # views.py 파일에 이제 함수를 넣어줄 것임. 

# Create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), 


# Delete
    path('<int:id>/delete/', views.delete, name='delete'),

# Update
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update' ),

]

