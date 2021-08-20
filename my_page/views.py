from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from log_app.models import CustomUser
# Create your views here.


def out_view(request):
    if request.method == "POST":
        pw_del = request.POST["pw_del"]
        user = request.user
        if not check_password(pw_del, user.password):
            return render(request,"my_page/out.html", {'error': '비밀번호가 틀렸습니다.'}) 
        else:
            logout(request)
            user.delete()
            return render(request,"main.html")
    else:
        return render(request,'my_page/out.html')

def modify_view(request):
    return render(request,'my_page/modify.html')

def modify_id(request):
    if request.method == "POST":
        user = request.user
        if user.username == request.POST['change_ID']:
            return render(request,'my_page/modify.html',{'error_id':'같은 아이디로는 변경되지않습니다.'})
        else:
            userList = CustomUser.objects.all()
            for userl in userList:
                if userl.username == request.POST['change_ID']:
                    return render(request,'my_page/modify.html',{'error_id':'이미 동일한 계정이 존재합니다.'})
            user.username = request.POST['change_ID']
            user.save()
            return render(request,'main.html')
    else:
        return render(request,'main.html')

def modify_pw(request):
    if request.method == "POST":
        user = request.user
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        if check_password(old_password,user.password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                login(request,user)
                return render(request,'main.html')
            
            else:
                return render(request,'my_page/modify.html',{'error':'비밀번호가 다릅니다.'})
        else:
            return render(request,'my_page/modify.html',{'error':'비밀번호가 틀렸습니다.'})
    else:
        return render(request,'my_page/modify.html')
    