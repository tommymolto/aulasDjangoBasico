from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pergunta
from django.template import loader
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Pergunta.objects.order_by('-pub_date')[:5]
    template = loader.get_template('enquetes/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detalhes(request, question_id):
    question = get_object_or_404(Pergunta, pk=question_id)
    return render(request, 'enquetes/detalhes.html', {'question': question})


def resultados(request, question_id):
    response = "resultado da questao %s."
    return HttpResponse(response % question_id)


def votar(request, question_id):
    return HttpResponse("cotando em  %s." % question_id)