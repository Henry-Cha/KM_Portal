from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    ########## 일반 게시판 #############
    path('free/', views.free_index, name='free_index'),
    path('free/answer/create/<int:postId>/', views.free_answer_create, name='free_answer_create'),
    path('free/answer/delete/<int:postId>/<int:answerId>/', views.free_answer_delete, name='free_answer_delete'),
    path('free/<int:postId>/', views.free_detail,name='free_detail'),
    path('free/write/', views.free_write, name='free_write'),
    path('free/delete/<int:postId>', views.free_boardDelete, name='free_delete'), # 수정함 : free를 붙임
    path('free/edit/<int:postId>', views.free_boardEdit, name='free_boardEdit'), # 수정함 : free를 붙임
]