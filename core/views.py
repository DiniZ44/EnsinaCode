from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def register(request):
    return  render(request, 'core/register.html')

def login(request):
    return  render(request, 'core/login.html')

def linguagens(request):
    return  render(request, 'core/linguagens.html')

def ranking(request):
    return  render(request, 'core/ranking.html')

def questions(request):
    return  render(request, 'core/questions.html')
