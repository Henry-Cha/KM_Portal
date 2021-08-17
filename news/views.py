from django.shortcuts import render
from .api import *

def index(request):
    st_data = check_standard()
    ac_data = check_academic()
    aw_data = check_award()
    cr_data = check_recruit()
    jo_data = check_job()
    #non_data = check_nonsub()
    do_data = check_dormitory()
    data = check_calendar()
    ca_data = {'ca_data':data}
    return render(request, 'news/news.html',{**st_data,**ac_data,**aw_data,**cr_data,**jo_data,**do_data,**ca_data})