pip install virtualenv
pip install virtualenvwrapper-win
mkvirtualenv aulaDjango
 .\aula2018\Scripts\activate
cd ../git
mkdir aulaDjango
setprojectdir .
deactivate
../../pythonaula\aula2018\Scripts\activate




django-admin startproject meuSite
cd meuSite
python manage.py runserver


python manage.py startapp enquete

python manage.py makemigrations enquete
python manage.py sqlmigrate enquete 0001
python manage.py migrate 


python manage.py shell
from enquete.models import Opcao, Pergunta  
Pergunta.objects.all()
from django.utils import timezone
q = Pergunta(texto="E ai", pub_date=timezone.now())
q.save()
q.id

q.texto
q.texto = "Falae!"
q.save()
Pergunta.objects.all()
from enquete.models import Opcao, Pergunta
Pergunta.objects.all()
Pergunta.objects.filter(id=1)
Pergunta.objects.filter(Pergunta_text__startswith='F')
from django.utils import timezone
current_year = timezone.now().year
Pergunta.objects.get(pub_date__year=current_year)
Pergunta.objects.get(id=2)
Pergunta.objects.get(pk=1)
q = Pergunta.objects.get(pk=1)
q.was_published_recently()
q = Pergunta.objects.get(pk=1)
q.opcao_set.all()
q.opcao_set.create(opcao_pergunta='Beleza', votos=0)
q.opcao_set.create(opcao_pergunta='Tranquilo', votos=3)
q.opcao_set.create(opcao_pergunta='So prorgamando', votos=0)
q.opcao_set.all()
q.opcao_set.count()

c = q.opcao_set.filter(opcao_pergunta__startswith='So')
c.delete()