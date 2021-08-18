from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import * # import post >> import * 변경
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import PostForm
from .decorators import *
from django.contrib import messages


###################### 일반 게시판 ############################
@login_message_required
def free_write(request): # 수정 : 함수이름 free 추가 redirect /board >> /board/free 변경
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = FreePosting(user=user, title=title, content=content, date=timezone.now()) # 수정 : Post >> FreePosting
        post.save()
        return redirect('/board/free')
    else:
        form = PostForm()

    return render(request, "board/write.html", {'form': form,'url':'free'})



def free_index(request): # 수정함 : context url free 추가 함수이름 free추가 postList, postNum Post >> FreePosting 변경
        # 게시물 목록 출력
    postList = FreePosting.objects.all().order_by('-id')
    postNum = FreePosting.objects.count()
        #페이징처리
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
    
    context = {'postList': postList,'postNum':postNum,'page_obj':page_obj,'url':'free'}
    return render(request, 'board/list.html', context)

def free_detail(request, postId): # 수정함 : 함수이름 free추가 num, lst 추가 url free 추가
    # 상세보기
    post = FreePosting.objects.get(id=postId)
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    #num = post.free.count ### free_answer_create 말고 free_detail에서 context에 num(답글 갯수)이랑 lst(답글 리스트) 넣고 detail.html에서 바인딩하기
    lst = post.free_set.all
    context = {'post': post,'post_auth': post_auth,'url':'free','lst':lst} # 수정 : 'num':num 넣었다가 뺌
    return render(request, 'board/detail.html', context)

@login_message_required
def free_boardDelete(request, postId): # 수정 : 함수이름 free 추가 if redirect /board >> /baord/free else redirect /board >> board/free/
    post = FreePosting.objects.get(id=postId) # 수정 : Post >> FreePosting
    if post.user == request.user:
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/board/free')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/board/free/'+str(postId))

@login_message_required
def free_boardEdit(request, postId): # 수정 /: 함수이름 free 추가 if redirect /baord >> board/free/ 변경 else redirect /board/ >> /board/free/ 변경
    post = FreePosting.objects.get(id=postId) # 수정 : Post >> FreePosting
    
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = FreePosting(id=postId,user=request.user, title=title, content=content, date=timezone.now()) # 수정 : Post >> FreePosting
            post.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/board/free/'+str(postId))
    else:
        post = FreePosting.objects.get(id=postId) # 수정 : Post >> FreePosting
        if post.user == request.user:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'edit': '수정하기',
                'url':'free'
            }
            return render(request, "board/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/board/free/'+str(postId))

def free_answer_create(request,postId): # 수정함 : 변수이름 free 추가 post>>posting 변경 models별칭 answer_set에서 free로 변경 board:detail >> board:free_detail 변경
    # 답글 추가
    posting = get_object_or_404(FreePosting, pk=postId)
    posting.free_set.create(content=request.POST.get('content'), date=timezone.now()) ### answer_set을 Models에 있는 class마다의 related_name으로 바꿔줌 
    return redirect('board:free_detail', postId=postId)
