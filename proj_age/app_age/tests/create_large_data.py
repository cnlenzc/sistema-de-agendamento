import requests
from datetime import datetime, timedelta

# incluir
data_hora = datetime.today()
for i in range(1, 1111):
    hora_inicial = data_hora.strftime("%H:%M")
    data_hora += timedelta(hours=1)
    hora_final = data_hora.strftime("%H:%M")
    dados = {
        "data": data_hora.strftime("%Y-%m-%d"),
        "hora_inicial": hora_inicial,
        "hora_final": hora_final,
        "paciente": "paciente %s" % i,
        "procedimento": "procedimento %s" % i,
    }
    response = requests.post("http://localhost:8000/agendamento/", data=dados)
    # response = requests.post(
    #     "https://sistema-de-agendamento-lenz.herokuapp.com/agendamento/",
    #     data=dados)
    print(response.json())
