from rest_framework.test import APITestCase
from rest_framework import status
from app_age.tests.data_agendamento import \
    reg1, reg2, reg3, date1, date2, \
    reg_invalid_date, reg_not_unique, reg_blank,\
    reg_list, reg_list2, reg_list_empty, \
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
        self.assertEqual(response1.data, reg_list_empty['out'])
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.data['count'], reg_list['out']['count'])
        self.assertEqual(response2.data['next'], reg_list['out']['next'])
        self.assertEqual(response2.data['previous'], reg_list['out']['previous'])
        for i, reg in enumerate(reg_list['out']['results']):
            for item in reg:
                self.assertEqual(response2.data['results'][i][item], reg_list['out']['results'][i][item])


    def test_list_with_filter(self):
        response_create1 = self.client.post('/agendamento/', data=reg1['in'])
        response_create2 = self.client.post('/agendamento/', data=reg2['in'])
        response_create3 = self.client.post('/agendamento/', data=reg3['in'])
        response1 = self.client.get('/agendamento/?min_data=%s&max_data=%s'
                                    % (date1.strftime("%Y-%m-%d"), date1.strftime("%Y-%m-%d")))
        response2 = self.client.get('/agendamento/?data=%s' % date2.strftime("%Y-%m-%d"))
        response3 = self.client.get('/agendamento/?paciente=Luis')

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response1.data['count'], reg_list['out']['count'])
        self.assertEqual(response1.data['next'], reg_list['out']['next'])
        self.assertEqual(response1.data['previous'], reg_list['out']['previous'])
        for i, reg in enumerate(reg_list['out']['results']):
            for item in reg:
                self.assertEqual(response1.data['results'][i][item], reg_list['out']['results'][i][item])

        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.data['count'], reg_list2['out']['count'])
        self.assertEqual(response2.data['next'], reg_list2['out']['next'])
        self.assertEqual(response2.data['previous'], reg_list2['out']['previous'])
        for i, reg in enumerate(reg_list2['out']['results']):
            for item in reg:
                self.assertEqual(response2.data['results'][i][item], reg_list2['out']['results'][i][item])

        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.data['count'], reg_list2['out']['count'])
        self.assertEqual(response3.data['next'], reg_list2['out']['next'])
        self.assertEqual(response3.data['previous'], reg_list2['out']['previous'])
        for i, reg in enumerate(reg_list2['out']['results']):
            for item in reg:
                self.assertEqual(response3.data['results'][i][item], reg_list2['out']['results'][i][item])


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




