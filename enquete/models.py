from django.db import models


class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Opcao(models.Model):
    questao = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    opcao_pergunta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)