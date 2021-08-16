from django.shortcuts import render


def index(request):
    return render(request, 'main.html')

def service(request):
    return render(request,'serviceagreement.html')

def privacy(request):
    return render(request,'privacy.html')

def rules(request):
    return render(request,'rules.html')