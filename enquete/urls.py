from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detalhes, name='detalhes'),
    # ex: /polls/5/results/
    path('<int:question_id>/resultados/', views.resultados, name='resultados'),
    # ex: /polls/5/vote/
    path('<int:question_id>/votar/', views.votar, name='votar'),
]