from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import * # import post >> import * 변경
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import PostForm
from .decorators import *
from django.contrib import messages
from log_app.models import CustomUser
import operator

@login_message_required
def write(request): # 수정 : 함수이름 free 추가 redirect /board >> /board/free 변경
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = Post(user=user, title=title, content=content, date=timezone.now()) # 수정 : Post >> FreePosting
        post.save()
        return redirect('/qnaboard')
    else:
        form = PostForm()
    return render(request, "qna/write.html", {'form': form,'url':'qnaboard'})

def index(request): # 수정함 : context url free 추가 함수이름 free추가 postList, postNum Post >> FreePosting 변경
        # 게시물 목록 출력
    postList = Post.objects.all().order_by('-id')
    postNum = Post.objects.count()
        #페이징처리
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
     #랭킹
    userList = CustomUser.objects.all().order_by('-naegong')
    rankList = {}
    for user in userList:
        rankList[user.username] = user.naegong
        
    rankList = sorted(rankList.items(), key=operator.itemgetter(1), reverse=True)
    rankList=rankList[:20]
    
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'qnaboard','boardname':'질문이','rankList':rankList} 
    return render(request, 'qna/list.html', context)

def detail(request, postId): # 수정함 : 함수이름 free추가 num, lst 추가 url free 추가
    # 상세보기
    post = Post.objects.get(id=postId)
    qnaAnswer = Answer.objects.filter(post=postId).order_by('created') # detail에 freeAnswer는 건들지 말기 (게시물 내용 페이지에서 댓글 갯수 확인하는 함수 사용하지는 않음)
    qnaAnswer_count = qnaAnswer.exclude().count()
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    #num = post.free.count ### free_answer_create 말고 free_detail에서 context에 num(답글 갯수)이랑 lst(답글 리스트) 넣고 detail.html에서 바인딩하기
    lst = post.answer_set.all
    context = {'post': post,'post_auth': post_auth,'url':'qnaboard','lst':lst,'Answers': Answer,'qnaAnswer_count': qnaAnswer_count,} # 수정 : 'num':num 넣었다가 뺌
    return render(request, 'qna/detail.html', context)

@login_message_required
def boardDelete(request, postId): # 수정 : 함수이름 free 추가 if redirect /board >> /baord/free else redirect /board >> board/free/
    post = Post.objects.get(id=postId) # 수정 : Post >> FreePosting
    if post.user == request.user:
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/qnaboard')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/qnaboard/'+str(postId))

@login_message_required
def boardEdit(request, postId):
    # 수정 /: 함수이름 free 추가 if redirect /baord >> board/free/ 변경 else redirect /board/ >> /board/free/ 변경
    post = Post.objects.get(id=postId) # 수정 : Post >> FreePosting
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = Post(hits=post.hits,id=postId,user=request.user, title=title, content=content, date=timezone.now()) # 수정 : Post >> FreePosting
            qnaAnswer_count = Answer.objects.filter(post=postId).exclude().count()
            post.comments = qnaAnswer_count
            post.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/qnaboard/'+str(postId))
    else:
        post = Post.objects.get(id=postId) # 수정 : Post >> FreePosting
        if post.user == request.user:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'edit': '수정하기',
                'url':'qnaboard'
            }
            return render(request, "qna/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/qnaboard/'+str(postId))

def answer_create(request,postId): # 수정함 : 변수이름 free 추가 post>>posting 변경 models별칭 answer_set에서 free로 변경 board:detail >> board:free_detail 변경
    # 답글 추가
    posting = get_object_or_404(Post, pk=postId)
    posting.answer_set.create(user=request.user,content=request.POST.get('content'), date=timezone.now()) ### answer_set을 Models에 있는 class마다의 related_name으로 바꿔줌 
    Answer_count = Answer.objects.filter(post=postId).exclude().count()
    posting.comments = Answer_count
    posting.save()
    return redirect('qnaBoard:detail', postId=postId)

@login_message_required
def answer_delete(request,postId,answerId):
    Posting = get_object_or_404(Post, pk=postId)
    target_answer = Answer.objects.get(id = answerId)
    if request.user == target_answer.user:
        target_answer.delete()
        Answer_count = Answer.objects.filter(post=postId).exclude().count()
        Posting.comments = Answer_count
        Posting.save()
    return redirect('qnaBoard:detail', postId=postId)

def selectAnswer(request,postId,answerId):
    post = Post.objects.get(id=postId)
    answer = Answer.objects.get(id=answerId)
    print(postId)
    print(answerId)
    post.complete = True
    answer.select = True
    post.save()
    answer.save()
    user = CustomUser.objects.get(username=answer.user)
    user.naegong = user.naegong + 10
    user.save()
    return redirect('qnaBoard:detail', postId=postId)
