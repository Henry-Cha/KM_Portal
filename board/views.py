# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return render(request, 'board/list.html')

# def write(request):
#     return render(request, 'board/write.html')

# ##################################################

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

from django.http import HttpResponse

def write(request):
    return render(request, 'board/write.html')

def index(request):
    # 게시물 목록 출력
    postList = Post.objects.order_by('-date')
    context = {'postList': postList}
    return render(request, 'board/list.html', context)

def detail(request, postId):
    # 상세보기
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'board/detail.html', context)

def answer_create(request,postId):
    # 답글 추가
    post = get_object_or_404(Post, pk=postId)
    post.answer_set.create(content=request.POST.get('content'),writer="",date=timezone.now())
    return redirect('board:index')
