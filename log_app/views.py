from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
# Create your views here.

def login_view(request) :
    if request.method == "POST":
        username = request.POST['ID']
        password = request.POST['Password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'log_app/login.html', {'error': '아이디나 비밀번호가 틀렸습니다.'})
    else:
        return render(request, 'log_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == "POST":
        if CustomUser.objects.filter(username=request.POST['username']).exists():
            return render(request, 'log_app/signup.html', {'error': '이 아이디로 가입한 계정이 존재합니다.'})
        
        elif CustomUser.objects.filter(email = str(request.POST['STUID'])+"@kmu.kr").exists():
             return render(request, 'log_app/signup.html', {'error': '이 이메일로 가입한 계정이 존재합니다.'})
            
        elif request.POST["password1"] == request.POST["password2"]:
            Email = str(request.POST['STUID'])+"@stu.kmu.ac.kr"
            user = CustomUser.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=Email)
            # user.is_active = False
            user.save()
            # current_site = get_current_site(request)
            # message = render_to_string('log_app/activation_email.html',{ 
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # mail_title = "계정 활성화 확인 이메일"
            # mail_to = request.POST["STUID"]+"@stu.kmu.ac.kr"
            # email = EmailMessage(mail_title,message,to=[mail_to])
            # email.send()
            return redirect('/')
        else:
            return render(request, 'log_app/signup.html', {'error': '비밀번호가 다릅니다.'})
    else:
        return render(request, 'log_app/signup.html')
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'home.html', {'error' : '계정 활성화 오류'})
    return 
    

