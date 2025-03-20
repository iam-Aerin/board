from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # 이후 templates 폴더를 'articles'폴더 안에 만들고 index.html 파일을 만들어줌. 