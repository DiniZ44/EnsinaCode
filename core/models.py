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


class Perguntas (models.Model):
    numeracao = models.CharField(max_length= 20)
    decricao = models.CharField(max_length= 350)
    pontuacao = models.IntegerField()
    linguagem = models.ForeignKey(Linguagem, on_delete= models.CASCADE)

    def __str__(self):
        return self.numeracao


class Alternativas(models.Model):
    letras = models.CharField(max_length=10)
    descricao = models.CharField(max_length=300)
    letraCerta = models.BooleanField(default=False)
    pergunta = models.ForeignKey(Perguntas,on_delete= models.CASCADE)

    def __str__(self):
        return self.letras


class Ranking (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    score = models.IntegerField()