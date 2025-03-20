# 이 파일은 원래 존재하지는 않았고, 내가 따로 new file로 추가해준  `urls.py` 파일임. 
# settings.py에서 include('articles.urls') 라는 함수로 이 urls.py의 경로가 반복되서 사용될 수 있도록 만들어줌. 

from django.urls import path
# 이제 path 앞에는 articles를 빼고 적어도된다. 
from . import views
# 현재 폴더에 있는 views를 가져와요. 

urlpatterns = [
    path('', views.index)
    # ''비어 있는 string=> articles경로를 포함하고 있구나.
    # views.py 파일에 이제 함수를 넣어줄 것임. 
]