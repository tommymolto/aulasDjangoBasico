from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Vamos as perguntas?")


def detalhes(request, question_id):
    return HttpResponse("pergunta %s." % question_id)


def resultados(request, question_id):
    response = "resultado da questao %s."
    return HttpResponse(response % question_id)


def votar(request, question_id):
    return HttpResponse("cotando em  %s." % question_id)