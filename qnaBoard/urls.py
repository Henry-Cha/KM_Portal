from django.urls import path
from . import views

app_name = 'qnaBoard'

urlpatterns = [
    path('', views.index, name='index'),
    path('answer/create/<int:postId>/', views.answer_create, name='answer_create'),
    path('answer/delete/<int:postId>/<int:answerId>/', views.answer_delete, name='answer_delete'),
    path('<int:postId>/', views.detail,name='detail'),
    path('write/', views.write, name='write'),
    path('delete/<int:postId>', views.boardDelete, name='delete'),
    path('edit/<int:postId>', views.boardEdit, name='boardEdit'),
    path('select/<int:postId>/<int:answerId>', views.selectAnswer, name='selectAnswer'),
]