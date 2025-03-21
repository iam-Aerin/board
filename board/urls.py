"""
URL configuration for board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

 # 이번 프로젝트에서 할 방법 
 include 함수

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))ㅋ
"""
from django.contrib import admin
from django.urls import path, include
# include 함수를 불러와주세요 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))


]
