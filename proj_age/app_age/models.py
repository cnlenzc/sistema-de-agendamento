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

    def __str__(self):
        return '%s %s paciente: %s' % (self.data, self.hora_inicial, self.paciente)
