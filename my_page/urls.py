from django.urls import path
from . import views

app_name = 'my_page'

urlpatterns = [
    path('out/',views.out_view, name="out"),
    path('modify/',views.modify_view, name="modify"),
    path('modify_id',views.modify_id,name="modify_id"),
    path('modify_pw',views.modify_pw,name="modify_pw"),
]