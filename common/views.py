from django.shortcuts import render
from .models import *
from board.models import *


def index(request):
    coor = Coordinate.objects.get(id=1)
    context = { 'centerLat':coor.latitude,'centerLon':coor.longitude}
    
    return render(request, 'home.html',context)

def service(request):
    return render(request,'serviceagreement.html')

def privacy(request):
    return render(request,'privacy.html')

def rules(request):
    return render(request,'rules.html')