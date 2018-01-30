from rest_framework.test import APITestCase
from rest_framework import status
from app_age.tests.data_agendamento import reg1, reg2, reg_invalid_date, reg_not_unique, reg_blank, reg_list,\
    reg_hora_inicial_maior_hora_final

class AgendamentoAPI(APITestCase):

    def test_create_ok(self):
        response1 = self.client.post('/agendamento/', data=reg1['in'])
        response2 = self.client.post('/agendamento/', data=reg2['in'])

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        for item in reg1['out']:
            self.assertEqual(response1.data[item], reg1['out'][item])

        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        for item in reg2['out']:
            self.assertEqual(response2.data[item], reg2['out'][item])


    def test_create_invalid_date(self):
        response = self.client.post('/agendamento/', data=reg_invalid_date['in'])

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, reg_invalid_date['out'])


    def test_create_not_unique(self):
        response1 = self.client.post('/agendamento/', data=reg_not_unique['in'])
        response2 = self.client.post('/agendamento/', data=reg_not_unique['in'])

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.data, reg_not_unique['out'])


    def test_create_blank(self):
        response = self.client.post('/agendamento/', data=reg_blank['in'])

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, reg_blank['out'])


    def test_create_hora_inicial_maior_hora_final(self):
        response = self.client.post('/agendamento/', data=reg_hora_inicial_maior_hora_final['in'])

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, reg_hora_inicial_maior_hora_final['out'])


    def test_list_ok(self):
        response1 = self.client.get('/agendamento/')
        response_create1 = self.client.post('/agendamento/', data=reg2['in'])
        response_create2 = self.client.post('/agendamento/', data=reg1['in'])
        response2 = self.client.get('/agendamento/')

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.data, [])
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        for i, reg in enumerate(reg_list['out']):
            for item in reg:
                self.assertEqual(response2.data[i][item], reg_list['out'][i][item])


    def test_detail_ok(self):
        response_create1 = self.client.post('/agendamento/', data=reg1['in'])
        response_create2 = self.client.post('/agendamento/', data=reg2['in'])
        response1 = self.client.get('/agendamento/%s/' % response_create1.data['id'])
        response2 = self.client.get('/agendamento/%s/' % response_create2.data['id'])

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        for item in reg1['out']:
            self.assertEqual(response1.data[item], reg1['out'][item])
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        for item in reg2['out']:
            self.assertEqual(response2.data[item], reg2['out'][item])


    def test_detail_not_find(self):
        response1 = self.client.get('/agendamento/9999/')

        self.assertEqual(response1.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response1.data, {'detail': 'Not found.'})


    def test_delete_ok(self):
        response_create1 = self.client.post('/agendamento/', data=reg1['in'])
        response_create2 = self.client.post('/agendamento/', data=reg2['in'])
        response1 = self.client.delete('/agendamento/%s/' % response_create1.data['id'])
        response2 = self.client.delete('/agendamento/%s/' % response_create2.data['id'])

        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response1.data, None)
        self.assertEqual(response2.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response2.data, None)


    def test_delete_not_found(self):
        response1 = self.client.delete('/agendamento/9999/')

        self.assertEqual(response1.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response1.data, {'detail': 'Not found.'})


    def test_update_ok(self):
        response_create1 = self.client.post('/agendamento/', data=reg1['in'])
        response1 = self.client.put('/agendamento/%s/' % response_create1.data['id'], data=reg2['in'])

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        for item in reg1['out']:
            self.assertEqual(response1.data[item], reg2['out'][item])


    def test_update_not_unique(self):
        response_create1 = self.client.post('/agendamento/', data=reg1['in'])
        response_create2 = self.client.post('/agendamento/', data=reg2['in'])
        response1 = self.client.put('/agendamento/%s/' % response_create1.data['id'], data=reg2['in'])

        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response1.data, reg_not_unique['out'])




