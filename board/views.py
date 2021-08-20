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
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'free','boardname':'자유'} 
    return render(request, 'board/list.html', context)

def free_detail(request, postId): # 수정함 : 함수이름 free추가 num, lst 추가 url free 추가
    # 상세보기
    post = FreePosting.objects.get(id=postId)
    freeAnswer = FreeAnswer.objects.filter(post=postId).order_by('created') # detail에 freeAnswer는 건들지 말기 (게시물 내용 페이지에서 댓글 갯수 확인하는 함수 사용하지는 않음)
    freeAnswer_count = freeAnswer.exclude().count()
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    #num = post.free.count ### free_answer_create 말고 free_detail에서 context에 num(답글 갯수)이랑 lst(답글 리스트) 넣고 detail.html에서 바인딩하기
    lst = post.free_set.all
    context = {'post': post,'post_auth': post_auth,'url':'free','lst':lst,'FreeAnswers': FreeAnswer,'freeAnswer_count': freeAnswer_count,} # 수정 : 'num':num 넣었다가 뺌
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
def free_boardEdit(request, postId):
    # 수정 /: 함수이름 free 추가 if redirect /baord >> board/free/ 변경 else redirect /board/ >> /board/free/ 변경
    post = FreePosting.objects.get(id=postId) # 수정 : Post >> FreePosting
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = FreePosting(hits=post.hits,id=postId,user=request.user, title=title, content=content, date=timezone.now()) # 수정 : Post >> FreePosting
            freeAnswer_count = FreeAnswer.objects.filter(post=postId).exclude().count()
            post.comments = freeAnswer_count
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
    posting.free_set.create(user=request.user,content=request.POST.get('content'), date=timezone.now()) ### answer_set을 Models에 있는 class마다의 related_name으로 바꿔줌 
    freeAnswer_count = FreeAnswer.objects.filter(post=postId).exclude().count()
    posting.comments = freeAnswer_count
    posting.save()
    return redirect('board:free_detail', postId=postId)

@login_message_required
def free_answer_delete(request,postId,answerId):
    freePosting = get_object_or_404(FreePosting, pk=postId)
    target_answer = FreeAnswer.objects.get(id = answerId)
    if request.user == target_answer.user:
        target_answer.delete()
        freeAnswer_count = FreeAnswer.objects.filter(post=postId).exclude().count()
        freePosting.comments = freeAnswer_count
        freePosting.save()
    return redirect('board:free_detail', postId=postId)

###################### 공학 게시판 ############################
@login_message_required
def eng_write(request): 
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = EngPosting(user=user, title=title, content=content, date=timezone.now())
        post.save()
        return redirect('/board/eng')
    else:
        form = PostForm()
    return render(request, "board/write.html", {'form': form,'url':'eng'})

def eng_index(request): 
    postList = EngPosting.objects.all().order_by('-id')
    postNum = EngPosting.objects.count()
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'eng','boardname':'공학'} 
    return render(request, 'board/list.html', context)

def eng_detail(request, postId): 
    post = EngPosting.objects.get(id=postId)
    freeAnswer = FreeAnswer.objects.filter(post=postId).order_by('created')
    freeAnswer_count = freeAnswer.exclude().count()
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    lst = post.eng_set.all
    context = {'post': post,'post_auth': post_auth,'url':'eng','lst':lst,'FreeAnswers': FreeAnswer,'freeAnswer_count': freeAnswer_count,}
    return render(request, 'board/detail.html', context)

@login_message_required
def eng_boardDelete(request, postId):
    post = EngPosting.objects.get(id=postId)
    if post.user == request.user:
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/board/eng')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/board/eng/'+str(postId))

@login_message_required
def eng_boardEdit(request, postId):
    post = EngPosting.objects.get(id=postId)
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = EngPosting(hits=post.hits,id=postId,user=request.user, title=title, content=content, date=timezone.now())
            engAnswer_count = EngAnswer.objects.filter(post=postId).exclude().count()
            post.comments = engAnswer_count
            post.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/board/eng/'+str(postId))
    else:
        post = EngPosting.objects.get(id=postId)
        if post.user == request.user:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'edit': '수정하기',
                'url':'eng'
            }
            return render(request, "board/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/board/eng/'+str(postId))

def eng_answer_create(request,postId):
    posting = get_object_or_404(EngPosting, pk=postId)
    posting.eng_set.create(user=request.user,content=request.POST.get('content'), date=timezone.now())
    engAnswer_count = EngAnswer.objects.filter(post=postId).exclude().count()
    posting.comments = engAnswer_count
    posting.save()
    return redirect('board:eng_detail', postId=postId)

@login_message_required
def eng_answer_delete(request,postId,answerId):
    engPosting = get_object_or_404(EngPosting, pk=postId)
    target_answer = EngAnswer.objects.get(id = answerId)
    if request.user == target_answer.user:
        target_answer.delete()
        engAnswer_count = EngAnswer.objects.filter(post=postId).exclude().count()
        engPosting.comments = engAnswer_count
        engPosting.save()
    return redirect('board:eng_detail', postId=postId)

###################### 자연과학 게시판 ############################
@login_message_required
def sci_write(request): 
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = SciPosting(user=user, title=title, content=content, date=timezone.now())
        post.save()
        return redirect('/board/sci')
    else:
        form = PostForm()
    return render(request, "board/write.html", {'form': form,'url':'sci'})

def sci_index(request): 
    postList = SciPosting.objects.all().order_by('-id')
    postNum = SciPosting.objects.count()
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'sci','boardname':'자연과학'} 
    return render(request, 'board/list.html', context)

def sci_detail(request, postId): 
    post = SciPosting.objects.get(id=postId)
    freeAnswer = FreeAnswer.objects.filter(post=postId).order_by('created')
    freeAnswer_count = freeAnswer.exclude().count()
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    lst = post.sci_set.all
    context = {'post': post,'post_auth': post_auth,'url':'sci','lst':lst,'FreeAnswers': FreeAnswer,'freeAnswer_count': freeAnswer_count,}
    return render(request, 'board/detail.html', context)

@login_message_required
def sci_boardDelete(request, postId):
    post = SciPosting.objects.get(id=postId)
    if post.user == request.user:
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/board/sci')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/board/sci/'+str(postId))

@login_message_required
def sci_boardEdit(request, postId):
    post = SciPosting.objects.get(id=postId)
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = SciPosting(hits=post.hits,id=postId,user=request.user, title=title, content=content, date=timezone.now())
            sciAnswer_count = SciAnswer.objects.filter(post=postId).exclude().count()
            post.comments = sciAnswer_count
            post.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/board/sci/'+str(postId))
    else:
        post = SciPosting.objects.get(id=postId)
        if post.user == request.user:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'edit': '수정하기',
                'url':'sci'
            }
            return render(request, "board/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/board/sci/'+str(postId))

def sci_answer_create(request,postId):
    posting = get_object_or_404(SciPosting, pk=postId)
    posting.sci_set.create(user=request.user,content=request.POST.get('content'), date=timezone.now())
    sciAnswer_count = SciAnswer.objects.filter(post=postId).exclude().count()
    posting.comments = sciAnswer_count
    posting.save()
    return redirect('board:sci_detail', postId=postId)

@login_message_required
def sci_answer_delete(request,postId,answerId):
    sciPosting = get_object_or_404(SciPosting, pk=postId)
    target_answer = SciAnswer.objects.get(id = answerId)
    if request.user == target_answer.user:
        target_answer.delete()
        sciAnswer_count = SciAnswer.objects.filter(post=postId).exclude().count()
        sciPosting.comments = sciAnswer_count
        sciPosting.save()
    return redirect('board:sci_detail', postId=postId)
###################### 의학/간호 게시판 ############################
@login_message_required
def med_write(request):   #@
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = MedPosting(user=user, title=title, content=content, date=timezone.now())   #@
        post.save()
        return redirect('/board/med')   #@
    else:
        form = PostForm()
    return render(request, "board/write.html", {'form': form,'url':'med'})   #@

def med_index(request):    #@
    postList = MedPosting.objects.all().order_by('-id')   #@
    postNum = MedPosting.objects.count()   #@
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'med','boardname':'의학간호'}   #@
    return render(request, 'board/list.html', context)

def med_detail(request, postId):    #@
    post = MedPosting.objects.get(id=postId)     #@
    freeAnswer = FreeAnswer.objects.filter(post=postId).order_by('created')
    freeAnswer_count = freeAnswer.exclude().count()
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    lst = post.med_set.all    #@
    context = {'post': post,'post_auth': post_auth,'url':'med','lst':lst,'FreeAnswers': FreeAnswer,'freeAnswer_count': freeAnswer_count,}  #@
    return render(request, 'board/detail.html', context)

@login_message_required
def med_boardDelete(request, postId):  #@
    post = MedPosting.objects.get(id=postId)   #@
    if post.user == request.user:
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/board/med')   #@
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/board/med/'+str(postId))   #@

@login_message_required
def med_boardEdit(request, postId):   #@
    post = MedPosting.objects.get(id=postId)   #@
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = MedPosting(hits=post.hits,id=postId,user=request.user, title=title, content=content, date=timezone.now())   #@
            medAnswer_count = MedAnswer.objects.filter(post=postId).exclude().count()
            post.comments = medAnswer_count
            post.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/board/med/'+str(postId))   #@
    else:
        post = MedPosting.objects.get(id=postId)   #@
        if post.user == request.user:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'edit': '수정하기',
                'url':'med'   #@
            }
            return render(request, "board/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/board/med/'+str(postId))   #@

def med_answer_create(request,postId):   #@
    posting = get_object_or_404(MedPosting, pk=postId)  #@
    posting.med_set.create(user=request.user,content=request.POST.get('content'), date=timezone.now())  #@
    medAnswer_count = MedAnswer.objects.filter(post=postId).exclude().count()   #@
    posting.comments = medAnswer_count    #@
    posting.save()
    return redirect('board:med_detail', postId=postId)  #@

@login_message_required
def med_answer_delete(request,postId,answerId):  #@
    medPosting = get_object_or_404(MedPosting, pk=postId)   #@
    target_answer = MedAnswer.objects.get(id = answerId)   #@
    if request.user == target_answer.user:
        target_answer.delete()
        medAnswer_count = MedAnswer.objects.filter(post=postId).exclude().count()   #@
        medPosting.comments = medAnswer_count   #@
        medPosting.save()   #@
    return redirect('board:med_detail', postId=postId)   #@
###################### 예체능 게시판 ############################
@login_message_required
def art_write(request):   #@
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = ArtPosting(user=user, title=title, content=content, date=timezone.now())   #@
        post.save()
        return redirect('/board/art')   #@
    else:
        form = PostForm()
    return render(request, "board/write.html", {'form': form,'url':'art'})   #@

def art_index(request):    #@
    postList = ArtPosting.objects.all().order_by('-id')   #@
    postNum = ArtPosting.objects.count()   #@
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'art','boardname':'예체능'}   #@2
    return render(request, 'board/list.html', context)

def art_detail(request, postId):    #@
    post = ArtPosting.objects.get(id=postId)     #@
    freeAnswer = FreeAnswer.objects.filter(post=postId).order_by('created')
    freeAnswer_count = freeAnswer.exclude().count()
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    lst = post.art_set.all    #@
    context = {'post': post,'post_auth': post_auth,'url':'art','lst':lst,'FreeAnswers': FreeAnswer,'freeAnswer_count': freeAnswer_count,}  #@
    return render(request, 'board/detail.html', context)

@login_message_required
def art_boardDelete(request, postId):  #@
    post = ArtPosting.objects.get(id=postId)   #@
    if post.user == request.user:
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/board/art')   #@
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/board/art/'+str(postId))   #@

@login_message_required
def art_boardEdit(request, postId):   #@
    post = ArtPosting.objects.get(id=postId)   #@
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = ArtPosting(hits=post.hits,id=postId,user=request.user, title=title, content=content, date=timezone.now())   #@
            artAnswer_count = ArtAnswer.objects.filter(post=postId).exclude().count()
            post.comments = artAnswer_count
            post.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/board/art/'+str(postId))   #@
    else:
        post = ArtPosting.objects.get(id=postId)   #@
        if post.user == request.user:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'edit': '수정하기',
                'url':'art'   #@
            }
            return render(request, "board/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/board/art/'+str(postId))   #@

def art_answer_create(request,postId):   #@
    posting = get_object_or_404(ArtPosting, pk=postId)  #@
    posting.art_set.create(user=request.user,content=request.POST.get('content'), date=timezone.now())  #@
    artAnswer_count = ArtAnswer.objects.filter(post=postId).exclude().count()   #@2
    posting.comments = artAnswer_count    #@
    posting.save()
    return redirect('board:art_detail', postId=postId)  #@

@login_message_required
def art_answer_delete(request,postId,answerId):  #@
    artPosting = get_object_or_404(ArtPosting, pk=postId)   #@2
    target_answer = ArtAnswer.objects.get(id = answerId)   #@
    if request.user == target_answer.user:
        target_answer.delete()
        artAnswer_count = ArtAnswer.objects.filter(post=postId).exclude().count()   #@2
        artPosting.comments = artAnswer_count   #@2
        artPosting.save()   #@
    return redirect('board:art_detail', postId=postId)   #@
###################### 인문/사회 게시판 ############################
@login_message_required
def soc_write(request):   #@
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = SocPosting(user=user, title=title, content=content, date=timezone.now())   #@
        post.save()
        return redirect('/board/soc')   #@
    else:
        form = PostForm()
    return render(request, "board/write.html", {'form': form,'url':'soc'})   #@

def soc_index(request):    #@
    postList = SocPosting.objects.all().order_by('-id')   #@
    postNum = SocPosting.objects.count()   #@
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'soc','boardname':'인문사회'}   #@2
    return render(request, 'board/list.html', context)

def soc_detail(request, postId):    #@
    post = SocPosting.objects.get(id=postId)     #@
    freeAnswer = FreeAnswer.objects.filter(post=postId).order_by('created')
    freeAnswer_count = freeAnswer.exclude().count()
    if request.user == post.user:
        post_auth = True
    else:
        post_auth = False
    lst = post.soc_set.all    #@
    context = {'post': post,'post_auth': post_auth,'url':'soc','lst':lst,'FreeAnswers': FreeAnswer,'freeAnswer_count': freeAnswer_count,}  #@
    return render(request, 'board/detail.html', context)

@login_message_required
def soc_boardDelete(request, postId):  #@
    post = SocPosting.objects.get(id=postId)   #@
    if post.user == request.user:
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/board/soc')   #@
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/board/soc/'+str(postId))   #@

@login_message_required
def soc_boardEdit(request, postId):   #@
    post = SocPosting.objects.get(id=postId)   #@
    if request.method == "POST":
        if(post.user == request.user):
            title = request.POST['title']
            content = request.POST['content']
            post = SocPosting(hits=post.hits,id=postId,user=request.user, title=title, content=content, date=timezone.now())   #@
            socAnswer_count = SocAnswer.objects.filter(post=postId).exclude().count()
            post.comments = socAnswer_count
            post.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/board/soc/'+str(postId))   #@
    else:
        post = SocPosting.objects.get(id=postId)   #@
        if post.user == request.user:
            form = PostForm(instance=post)
            context = {
                'form': form,
                'edit': '수정하기',
                'url':'soc'   #@
            }
            return render(request, "board/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/board/soc/'+str(postId))   #@

def soc_answer_create(request,postId):   #@
    posting = get_object_or_404(SocPosting, pk=postId)  #@
    posting.soc_set.create(user=request.user,content=request.POST.get('content'), date=timezone.now())  #@
    socAnswer_count = SocAnswer.objects.filter(post=postId).exclude().count()   #@2
    posting.comments = socAnswer_count    #@
    posting.save()
    return redirect('board:soc_detail', postId=postId)  #@

@login_message_required
def soc_answer_delete(request,postId,answerId):  #@
    socPosting = get_object_or_404(SocPosting, pk=postId)   #@2
    target_answer = SocAnswer.objects.get(id = answerId)   #@
    if request.user == target_answer.user:
        target_answer.delete()
        socAnswer_count = SocAnswer.objects.filter(post=postId).exclude().count()   #@2
        socPosting.comments = socAnswer_count   #@2
        socPosting.save()   #@
    return redirect('board:soc_detail', postId=postId)   #@