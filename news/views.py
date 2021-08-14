from django.shortcuts import render
from .api import check_standard

def index(request):
    data = check_standard()
    return render(request, 'news/news.html', {'sub1':data[0],'href1':data[1],'wrt1':data[2],'date1':data[3],'sub2':data[4],'href2':data[5],'wrt2':data[6],'date2':data[7],'sub3':data[8],'href3':data[9],'wrt3':data[10],'date3':data[11],'sub4':data[12],'href4':data[13],'wrt4':data[14],'date4':data[15],'sub5':data[16],'href5':data[17],'wrt5':data[18],'date5':data[19]})