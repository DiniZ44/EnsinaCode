from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'core/index.html')

def register(request):
    return render(request, 'core/register.html')

def login(request):
    return render(request, 'core/login.html')

def linguagens(request):
    return render(request, 'core/linguagens.html')

def ranking(request):
    return render(request, 'core/ranking.html')

def questions(request):
    return render(request, 'core/questions.html')

def reg_done(request):
    reg_usuario = Usuario()

    nome_rec = request.GET.get('nome_register')
    email_rec = request.GET.get('email_register')
    senha_rec = request.GET.get('senha_register')

    reg_usuario.nome = nome_rec
    reg_usuario.email = email_rec
    reg_usuario.senha = senha_rec
    reg_usuario.save()
    return render(request, 'core/reg_done.html',)

def login_done(request):

        if Usuario.objects.filter(email= request.GET.get('email_login') ,senha=request.GET.get('senha_login')).exists() :
            return render(request, 'core/index.html',)
        else:
            context = {'msg': 'Email ou senha incorretos'}
            return render(request, 'core/login.html', context)


