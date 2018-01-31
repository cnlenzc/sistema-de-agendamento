import requests
from datetime import datetime, timedelta


# incluir
dia = datetime.today()
for i in range(1, 101):
    dia += timedelta(days=1)
    dados = {
        "data": dia.strftime("%Y-%m-%d"),
        "hora_inicial": "8:00",
        "hora_final": "9:00",
        "paciente": "paciente %s" % i,
        "procedimento": "procedimento %s" % i,
    }
    response = requests.post("http://localhost:8000/agendamento/", data=dados)
    print(response.json())


# listar
response = requests.get("http://localhost:8000/agendamento/")
print('Lista de registros')
print('-' * 100)
for registro in response.json():
    print(registro)
print('-' * 100)
print('Total de %s registros' % len(response.json()))
