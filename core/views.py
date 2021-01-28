from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

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

    nome = request.POST.get('nome_register')
    email = request.POST.get('email_register')
    senha = request.POST.get('senha_register')
    senhaConfirm = request.POST.get('senha_repeat_register')

    reg_usuario.nome = nome
    reg_usuario.email = email
    reg_usuario.senha = senha

    if(senha == senhaConfirm):
        reg_usuario.save()

    return render(request, 'core/reg_done.html',)

