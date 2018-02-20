from datetime import datetime, timedelta
from rest_framework import viewsets, permissions
from django.http import HttpResponse
from django_filters.rest_framework\
    import DjangoFilterBackend, FilterSet, DateFilter
from app_age.models import Agendamento
from app_age.serializers import AgendamentoSerializer


# pylint: disable=unused-argument
def index(request):
    return HttpResponse("Olá! Bem vindo ao Sistema de Agendamento!")


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

    def get_queryset(self):
        queryset = AgendamentoViewSet.queryset

        if self.action == 'list':
            param_data = self.request.query_params.get('data', None)
            param_min_data = self.request.query_params.get('min_data', None)
            param_max_data = self.request.query_params.get('max_data', None)

            if not param_data:
                if not (param_min_data or param_max_data):
                    min_data = datetime.today()
                    max_data = min_data + timedelta(days=7)
                    queryset = queryset.filter(
                        data__gte=min_data,
                        data__lt=max_data)

        return queryset
