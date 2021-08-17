from django.urls import path
from . import views

app_name = 'log_app'

urlpatterns = [
    path('', views.login_view, name='Login'),
    path('logout', views.logout_view, name='Logout'),
    path('signup', views.signup_view, name='Signup'),
    path('activate/<str:uidb64>/<str:token>/',views.activate,name="activate"),
]