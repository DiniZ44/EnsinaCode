from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login),
    path('register/', views.register),
    path('register/reg_done/', views.reg_done),

]