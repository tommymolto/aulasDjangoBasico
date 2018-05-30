import datetime

from django.db import models
from django.utils import timezone
from django.db import models


class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.texto

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Opcao(models.Model):
    questao = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    opcao_pergunta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao_pergunta