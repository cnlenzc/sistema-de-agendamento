import requests

# listar
response = requests.get("http://localhost:8000/agendamento/")
print('Lista de registros')
print('-' * 100)
for registro in response.json()['results']:
    print(registro)
print('-' * 100)
print('Total de %s registros listados na pagina'
      % len(response.json()['results']))
print('Total de %s registros' % response.json()['count'])
