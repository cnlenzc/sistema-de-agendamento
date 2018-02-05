from rest_framework import viewsets, permissions
from app_age.models import Agendamento
from app_age.serializers import AgendamentoSerializer
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFilter


def index(request):
    return HttpResponse("Olá Pytonistas! Bem vindo ao Sistema de Agendamento!")


class AgendamentoFilter(FilterSet):
    min_data = DateFilter(name="data", lookup_expr='gte')
    max_data = DateFilter(name="data", lookup_expr='lte')

    class Meta:
        model = Agendamento
        fields = ['data', 'paciente']


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
    filter_backends = (DjangoFilterBackend,)
    filter_class = AgendamentoFilter