from django.shortcuts import render, redirect

# Create your views here.

from article.models import Article

from django.core.paginator import Paginator

def index(request):      # 게시글 목록을 보여주는 함수 작성
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)  # 한 페이지에 5개씩 보여주기

    page = request.GET.get('page')  # 현재 페이지 번호 가져오기
    articles = paginator.get_page(page)

    return render(request, 'index.html', {'articles': articles})

def show(request, pk):    # 게시글 디테일하게 보기
    article = Article.objects.get(pk=pk)

    return render(request, 'show.html', {'article' : article})

# def new(request):   # 게시글 작성
    # return render(request, 'new.html')

def create(request):    # 실질적으로 게시글을 작성하는 로직 함수 만들기
    if request.method == 'POST':
        article = Article()
        article.author = request.user
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()

        return redirect('article:show', pk=article.pk)
    else:
        return render(request, 'new.html')

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'edit.html', {"article" : article})

def update(request, pk):    # 수정하는 함수 만들기
    article = Article.objects.get(pk=pk)

    if article.author != request.user:
        return redirect('article:show', pk=pk)

    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()

    return redirect('article:show', pk=pk)

def delete(request, pk):    # 삭제하는 함수 만들기
    article = Article.objects.get(pk=pk)

    if article.author == request.user:
        article.delete()

    return redirect('article:index')

# 댓글 기능 추가

from article.models import Comment

def create_comment(request, pk):    # 댓글 기능 추가
    if request.method == 'POST':
        comment = Comment()
        comment.article = Article.objects.get(pk=pk)
        comment.author = request.user
        comment.content = request.POST['content']
        comment.save()

    return redirect('article:show', pk=pk)


def delete_comment(request, comment_pk):    # 댓글 삭제
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('article:show', pk=comment.article.pk)
