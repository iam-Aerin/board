from django.contrib import admin
from .models import Article


# Register your models here.
admin.site.register(Article)
# 관리자 페이지들어가서 article 작성해보려고 이 과정을 진행함. 
# createsuperuser 그 부분