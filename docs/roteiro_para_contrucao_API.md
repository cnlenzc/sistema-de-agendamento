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

enum_sexo = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))

class Pythonista(models.Model):
    nome = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    telefone = models.CharField(max_length=15, null=True)
    sexo = models.CharField(choices=enum_sexo, max_length=1, null=True)
    site = models.URLField(null=True)
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

#### Criando o primeiro app_age
```
python manage.py shell
from app_age.models import Pythonista
c = Pythonista(nome='Pedro', email='pedro@g.com')
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

#### Configuração da Rota URL
Arquivo app_age/urls.py
```
from django.conf.urls import url
from app_age import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^app_age/$', views.PythonistaList.as_view()),
    url(r'^app_age/(?P<pk>[0-9]+)/$', views.PythonistaDetail.as_view()),
]
```


#### Criação da view
Arquivo app_age/views.py
```
from django.http import HttpResponse
from rest_framework import generics
from app_age.models import Pythonista
from app_age.serializers import PythonistaSerializer

def index(request):
    return HttpResponse("Olá Pytonistas! Bem vindo ao Grupy!")

class PythonistaList(generics.ListCreateAPIView):
    '''
    Este método realiza 2 operações de acordo com o método Http:
    GET - consulta lista de app_ages
    POST - inclui um novo app_age
    '''
    queryset = Pythonista.objects.all()
    serializer_class = PythonistaSerializer

class PythonistaDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Este método realiza 3 operações de acordo com o método Http:
    GET - consulta app_age
    PUT - altera dados do app_age
    DELETE - remove app_age
    '''
    queryset = Pythonista.objects.all()
    serializer_class = PythonistaSerializer
```


#### Criação do serializer
Arquivo app_age/serializers.py
```
from rest_framework import serializers
from app_age.models import Pythonista

class PythonistaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Pythonista
        fields = ('__all__')
```

#### Chamando a API pela linha de comando
```
curl localhost:8000/app_age/
curl -i localhost:8000/app_age/
http get localhost:8000/app_age/
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
