from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

def write(request):
    #게시글 작성화면
    return render(request, 'board/write.html')
    
def write_create(request):
    #게시글 작성
    if request.method == "POST":
        writer = ""
        title = request.POST['title']
        content = request.POST['content']
        post = Post(writer=writer, title=title, content=content, date=timezone.now())
        post.save()
        return HttpResponseRedirect('/board')
    else:
        return render(request, 'board/list.html')

def index(request):
        # 게시물 목록 출력
    postList = Post.objects.all().order_by('-date')
    postNum = Post.objects.count()
        #페이징처리
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '3')
    page_obj = paginator.page(page)
    
    context = {'postList': postList,'postNum':postNum,'page_obj':page_obj}
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
    return redirect('board:detail', postId=postId)
