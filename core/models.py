from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length= 50)
    descricao = models.TextField(default='')
    fundador = models.CharField(max_length= 50)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome

class Perguntas(models.Model):
    descricao = models.CharField(max_length= 250)
    opcao_1 = models.CharField(max_length=100)
    opcao_2 = models.CharField(max_length=100)
    opcao_3 = models.CharField(max_length=100)
    correta = models.CharField(max_length=100)
    pontuacao = models.IntegerField()
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE)

class Ranking (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    score = models.IntegerField()