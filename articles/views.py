from django.shortcuts import render, redirect
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

def detail(request, id): 
    article = Article.objects.get(id=id)

    context = {
        'article' : article,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')


    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', id=article.id)


def delete(request, id):

    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')


def edit(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article' : article,
    }
     
    return render(request, 'edit.html', context )

def update(request, id):
    # 기존 정보 가져오기
    article = Article.objects.get(id=id)

    # 새로운 정보 가져오기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 새로운 정보로 기존 정보를 덮어씌움.
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', id=article.id)