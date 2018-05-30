from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pergunta
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'enquetes/resultados.html', {'question': question})


def votar(request, question_id):
    print(request)
    print(question_id)
    # return HttpResponse("cotando em  %s." % question_id)
    try:
        selected_choice = Pergunta.opcao_set.get(pk=request.POST['choice'])
    except (KeyError, Pergunta.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'enquete/detalhes.html', {
            'question': Pergunta,
            'error_message': "Nao tema  aopcao.",
        })
    else:
        selected_choice.votos += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('enquetes:resultados', args=(question.id)))