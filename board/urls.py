from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('answer/create/<int:postId>/', views.answer_create, name='answer_create'),
    path('<int:postId>/', views.detail,name='detail'),
    path('write/create/', views.write_create, name='write_create'),
    path('write/', views.write, name='write'),
]