from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha')


class LinguagemForm(forms.ModelForm):

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fundador = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Linguagem
        fields = ('nome','fundador','descricao','ano')


class PerguntasForm(forms.ModelForm):

    numeracao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pontuacao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    linguagem = forms.ModelChoiceField(queryset=Linguagem.objects.all(),widget=forms.Select(attrs={'class': 'fomr-control'}))

    class Meta:
        model = Perguntas
        fields = ('numeracao','descricao','pontuacao','linguagem')


class AlternativasForm(forms.ModelForm):

    letras = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    letraCerta = forms.BooleanField(widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    pergunta = forms.ModelChoiceField(queryset=Perguntas.objects.all(),
                                       widget=forms.Select(attrs={'class': 'fomr-control'}))

    class Meta:
        model = Alternativas
        fields = ("letras",'descricao','letraCerta','pergunta')


class RankingForm(forms.ModelForm):
    score = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(),
                                       widget=forms.Select(attrs={'class': 'fomr-control'}))

    class Meta:
        model = Usuario
        fields = ("socre", 'usuario')