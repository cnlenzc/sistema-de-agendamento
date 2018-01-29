# Roteiro para construção da API REST

#### Criar e ativar o ambiente virtual do python
```
$ mkdir sistema-de-agendamento
$ cd sistema-de-agendamento
$ pipenv install
$ pipenv shell
```

#### Instalar as dependências (pacotes do python)
```
pipenv install django
pipenv install djangorestframework
```


#### Criar o projeto e app do Django
```
django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile proj_age
cd prog_age
python manage.py startapp app_age
```


#### Testar o servidor Http
```
python manage.py runserver
```
Abra o browser com url
http://localhost:8000/


#### Adicione o app na lista de apps instalados
Adicione também o app da rest_framework
Arquivo prog_age/setting.py
```
INSTALLED_APPS = [
   …
    'rest_framework',
    'app_age',
]
```


#### Crie sua primeira view em Django
Arquivo prog_age/view.py
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Pytonistas! Bem vindo ao Grupy!")
```


#### Adicione a view na lista de url do app
Arquivo app_age/urls.py
```
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```


#### Adicione a lista de url do app na lista de url do projeto
Arquivo prog_age/urls.py
```
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('app_age.urls')),
    url(r'^admin/', admin.site.urls),
]
```


#### Teste novamente o servidor e veja se se a view apresenta a frase corretamente
```
control+C
python manage.py runserver
http://localhost:8000/
```


#### Construção do Modelo de Objetos (models.py)
Obs: O modelo relacional (BD) é gerado pelo Django a partir do modelo de objetos.
Arquivo app_age/models.py
```
from django.db import models

class Agendamento(models.Model):
    data = models.DateField(
        help_text='Data do agendamento da consulta/exame')
    hora_inicial = models.TimeField(
        help_text='Hora do início')
    hora_final = models.TimeField(
        help_text='Hora do final')
    paciente = models.CharField(
        help_text='Nome do Paciente',
        max_length=40)
    procedimento = models.TextField(
        help_text='Descrição da consulta, exame ou cirurgia',
        default='consulta')

    class Meta:
        indexes = [
            models.Index(fields=['data', 'hora_inicial'], name='data_hora_inicial_idx'),
            models.Index(fields=['data', 'hora_final'], name='data_hora_final_idx'),
            models.Index(fields=['paciente'], name='paciente_idx'),
        ]
        unique_together = ('data', 'hora_inicial')
        ordering = ('data', 'hora_inicial')

```


#### Criação do Banco Relacional
```
python manage.py makemigrations
python manage.py migrate
```

#### Consultar os comandos SQL gerados pelo Django
```
python manage.py sqlmigrate app_age 0001
```

#### Criando o primeiro Agendamento
```
python manage.py shell
from app_age.models import Agendamento
c = Agendamento(data=  '2017-01-30', hora_inicial='17:00', hora_final='17:15', paciente='Felipe')
c.save()
```

#### Shell SQL do sqlite
```
python manage.py dbshell
.table
.schema app_age_app_age
select * from app_age_app_age; 
.header on
.mode column
.exit
```

#### Shell SQL do Postegres (psql)
```
python manage.py dbshell
\dt
select * from app_age_agendamento; 
\q
```

#### Configuração da Rota URL
Arquivo app_age/urls.py
```
from django.conf.urls import url, include
from app_age import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'agendamento', views.AgendamentoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
]
```

#### Criação da view
Arquivo app_age/views.py
```
from rest_framework import viewsets, permissions
from app_age.models import Agendamento
from app_age.serializers import AgendamentoSerializer
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Pytonistas! Bem vindo ao Sistema de Agendamento!")

class AgendamentoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = (permissions.AllowAny,)
```

#### Criação do serializer
Arquivo app_age/serializers.py
```
from rest_framework import serializers
from app_age.models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
   class Meta:
        model = Agendamento
        fields = ('__all__')
```


## Deployment by heroku
How to deploy this on a live system
```
$ git add .
$ git commit -m "Added a file"
$ heroku login
    Enter your Heroku credentials…
$ heroku create
    Creating app... done, ⬢ nameless-fortress-70834
    https://nameless-fortress-70834.herokuapp.com/ | https://git.heroku.com/nameless-fortress-70834.git
$ git push heroku master
    -----> Python app detected
    -----> Launching... done, v7
```

## Comandos do heroku
To run your application locally
```
$ heroku local web
```

To view your application remote
```
$ heroku open
```

View logs
```
$ heroku logs --tail
```

View info running
```
$ heroku ps
```
Processing static files
```
$ python manage.py collectstatic
```

shell remote
```
$ heroku run bash
$ heroku run python
$ heroku run python manage.py shell
$ heroku run python manage.py migrate
$ heroku run python proj_age/manage.py migrate
$ heroku config:set DEBUG=False
$ heroku config:set SECRET_KEY=')z*j%sx=d3zq9h_m-ovw-hq!p2()yzg!ydft_+smpw=#n(l0h*'

```


#### Chamando a API pela linha de comando
```
curl https://sistema-de-agendamento-lenz.herokuapp.com/agendamento/
curl -i https://sistema-de-agendamento-lenz.herokuapp.com/agendamento/
http get https://sistema-de-agendamento-lenz.herokuapp.com/agendamento/
http get https://sistema-de-agendamento-lenz.herokuapp.com/agendamento/1/
```

#### Chamando a API em outro programa python
```
import requests
# listar
response = requests.get("http://localhost:8000/app_age/")
print(response.content)

# incluir
dados = {"nome": "João", "email": "john11@doe.com"}
response = requests.post("http://localhost:8000/app_age/", data=dados)
print(response.content)

# consultar
response = requests.get("http://localhost:8000/app_age/1/")
print(response.content)

# extraindo os valores
registro = response.json()
registro['nome']
registro[‘email’]
for nome_campo in registro:
    print('%s: %s' % (nome_campo, registro[nome_campo]))
```
