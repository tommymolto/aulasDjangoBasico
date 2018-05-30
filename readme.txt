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