from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
# Read 기능 구현하기

    context = {
        'articles' : articles,
    }
    return render(request, 'index.html', context)
    # 이후 templates 폴더를 'articles'폴더 안에 만들고 index.html 파일을 만들어줌. 
