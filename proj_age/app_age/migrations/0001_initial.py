# Generated by Django 2.0.1 on 2018-01-26 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Data do agendamento da consulta/exame')),
                ('hora_inicial', models.TimeField(help_text='Hora do início')),
                ('hora_final', models.TimeField(help_text='Hora do final')),
                ('paciente', models.CharField(help_text='Nome do Paciente', max_length=40)),
                ('procedimento', models.TextField(default='consulta', help_text='Descrição da consulta, exame ou cirurgia')),
            ],
            options={
                'ordering': ('data', 'hora_inicial'),
            },
        ),
        migrations.AddIndex(
            model_name='agendamento',
            index=models.Index(fields=['data', 'hora_inicial'], name='data_hora_inicial_idx'),
        ),
        migrations.AddIndex(
            model_name='agendamento',
            index=models.Index(fields=['data', 'hora_final'], name='data_hora_final_idx'),
        ),
        migrations.AddIndex(
            model_name='agendamento',
            index=models.Index(fields=['paciente'], name='paciente_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='agendamento',
            unique_together={('data', 'hora_inicial')},
        ),
    ]
