from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login),
    path('register/', views.register),
    path('reg_done/', views.reg_done),
    path('login_done/', views.login_done),
    path('profile/', views.profile),
    path('logado/', views.index_logado),

    path('questionespecific/<int:pk>/', views.linguagen_especific, name='url_perguntaDaLinguagem'),


]