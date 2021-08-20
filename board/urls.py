from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
######################## 일반 게시판 ##############################
    path('free/', views.free_index, name='free_index'),
    path('free/answer/create/<int:postId>/', views.free_answer_create, name='free_answer_create'),
    path('free/answer/delete/<int:postId>/<int:answerId>/', views.free_answer_delete, name='free_answer_delete'),
    path('free/<int:postId>/', views.free_detail,name='free_detail'),
    path('free/write/', views.free_write, name='free_write'),
    path('free/delete/<int:postId>', views.free_boardDelete, name='free_delete'), # 수정함 : free를 붙임
    path('free/edit/<int:postId>', views.free_boardEdit, name='free_boardEdit'), # 수정함 : free를 붙임
######################## 공학 게시판 ##############################
    path('eng/', views.eng_index, name='eng_index'),
    path('eng/answer/create/<int:postId>/', views.eng_answer_create, name='eng_answer_create'),
    path('eng/answer/delete/<int:postId>/<int:answerId>/', views.eng_answer_delete, name='eng_answer_delete'),
    path('eng/<int:postId>/', views.eng_detail,name='eng_detail'),
    path('eng/write/', views.eng_write, name='eng_write'),
    path('eng/delete/<int:postId>', views.eng_boardDelete, name='eng_delete'), 
    path('eng/edit/<int:postId>', views.eng_boardEdit, name='eng_boardEdit'), 
######################## 자연과학 게시판 ##############################
    path('sci/', views.sci_index, name='sci_index'),
    path('sci/answer/create/<int:postId>/', views.sci_answer_create, name='sci_answer_create'),
    path('sci/answer/delete/<int:postId>/<int:answerId>/', views.sci_answer_delete, name='sci_answer_delete'),
    path('sci/<int:postId>/', views.sci_detail,name='sci_detail'),
    path('sci/write/', views.sci_write, name='sci_write'),
    path('sci/delete/<int:postId>', views.sci_boardDelete, name='sci_delete'), 
    path('sci/edit/<int:postId>', views.sci_boardEdit, name='sci_boardEdit'), 
######################## 의학/간호 게시판 ##############################
    path('med/', views.med_index, name='med_index'),
    path('med/answer/create/<int:postId>/', views.med_answer_create, name='med_answer_create'),
    path('med/answer/delete/<int:postId>/<int:answerId>/', views.med_answer_delete, name='med_answer_delete'),
    path('med/<int:postId>/', views.med_detail,name='med_detail'),
    path('med/write/', views.med_write, name='med_write'),
    path('med/delete/<int:postId>', views.med_boardDelete, name='med_delete'), 
    path('med/edit/<int:postId>', views.med_boardEdit, name='med_boardEdit'), 
######################## 예체능 게시판 ##############################
    path('art/', views.art_index, name='art_index'),
    path('art/answer/create/<int:postId>/', views.art_answer_create, name='art_answer_create'),
    path('art/answer/delete/<int:postId>/<int:answerId>/', views.art_answer_delete, name='art_answer_delete'),
    path('art/<int:postId>/', views.art_detail,name='art_detail'),
    path('art/write/', views.art_write, name='art_write'),
    path('art/delete/<int:postId>', views.art_boardDelete, name='art_delete'), 
    path('art/edit/<int:postId>', views.art_boardEdit, name='art_boardEdit'), 
######################## 인문/사회 게시판 ##############################
    path('soc/', views.soc_index, name='soc_index'),
    path('soc/answer/create/<int:postId>/', views.soc_answer_create, name='soc_answer_create'),
    path('soc/answer/delete/<int:postId>/<int:answerId>/', views.soc_answer_delete, name='soc_answer_delete'),
    path('soc/<int:postId>/', views.soc_detail,name='soc_detail'),
    path('soc/write/', views.soc_write, name='soc_write'),
    path('soc/delete/<int:postId>', views.soc_boardDelete, name='soc_delete'), 
    path('soc/edit/<int:postId>', views.soc_boardEdit, name='soc_boardEdit'), 
]