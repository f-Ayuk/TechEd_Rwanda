from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('create_course', views.create_course, name="create_course"),
    path('get_user_info', views.get_user_info, name="get_user_info"),
    ]
