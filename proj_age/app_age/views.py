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

    list:
    Retorna a lista de agendamentos.

    create:
    Cria um novo agendamento.
    
    retrieve:
    Consulta um agendamento específico.

    update:
    Altera todas as informações de um agendamento.
    
    partial_update:
    Altera um campo de um agendamento.
    
    destroy:
    Remove um agendamento.
    
    """
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = (permissions.AllowAny,)