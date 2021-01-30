from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    data = {}
    data['linguagens'] = Linguagem.objects.all()
    return render(request, 'core/index.html',data)

def register(request):
    return render(request, 'core/register.html')

def login(request):
    return render(request, 'core/login.html')


def reg_done(request):
    reg_usuario = Usuario()

    nome_rec = request.GET.get('nome_register')
    email_rec = request.GET.get('email_register')
    senha_rec = request.GET.get('senha_register')
    senha_rec1 = request.GET.get('senha_repeat_register')

    reg_usuario.nome = nome_rec
    reg_usuario.email = email_rec
    reg_usuario.senha = senha_rec

    if  nome_rec == ""  or senha_rec=="" or email_rec=='' or senha_rec1=="":
        context = {'msg': 'Existem campos obrigatorios vazios'}
        return render(request, 'core/register.html', context)

    if senha_rec1 == senha_rec :
        reg_usuario.save()
        return render(request, 'core/reg_done.html', )

    else:
        context = {'msg': 'As senhas diferem'}
        return render(request, 'core/register.html', context)


def login_done(request):

        if Usuario.objects.filter(email= request.GET.get('email_login') ,senha=request.GET.get('senha_login')).exists() :
            return render(request, 'core/index.html',)

        if request.GET.get('email_login') == "" or request.GET.get('senha_login') == "":
            context = {'msg': 'Email ou Senha vazio'}
            return render(request, 'core/login.html', context)

        else:
            context = {'msg': 'Email ou senha incorretos'}
            return render(request, 'core/login.html', context)


