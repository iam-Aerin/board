from django.db import models

# base html을 만들어준 뒤, model 설정해주자
# Article

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 게시물이 작성된 그 순간의 시간을 저장