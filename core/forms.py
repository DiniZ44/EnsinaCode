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


class RankingForm(forms.ModelForm):
    score = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(),
                                       widget=forms.Select(attrs={'class': 'fomr-control'}))

    class Meta:
        model = Ranking
        fields = ("score", 'usuario')