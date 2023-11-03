from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('login', views.login, name='login')
]
