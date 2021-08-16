from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('serviceagreement/',views.service),
    path('privacy/',views.privacy),
    path('rules/',views.rules),
]