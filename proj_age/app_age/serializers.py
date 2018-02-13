from rest_framework import serializers
from app_age.models import Agendamento


class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = ('__all__')

    def validate(self, attrs):
        """
        Check that the start is before the stop.
        """
        if attrs['hora_inicial'] >= attrs['hora_final']:
            raise serializers.ValidationError(
                "O horário final da consulta deve ser depois do inicial")
        return attrs
