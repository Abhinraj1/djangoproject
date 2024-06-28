from django.contrib import admin
from django.urls import path, include
from .views import add_task, mark_task_done, mark_task_undone, signup, verify_otp, user_login, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", user_login, name="login"),
    path("home/", home, name="home"),
    path("", signup, name="signup"),  
    path("verify-otp/", verify_otp, name="verify_otp"), 
    path('add_task/', add_task, name='add_task'),
    path('mark_task_done/<int:task_id>/', mark_task_done, name='mark_task_done'),
    path('mark_task_undone/<int:task_id>/', mark_task_undone, name='mark_task_undone'),
]
