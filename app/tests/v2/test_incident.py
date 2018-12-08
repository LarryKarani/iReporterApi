import json

#local imports
from .base_test import BaseTestCase

class TestCreateIncidence(BaseTestCase):
    def setUp(self):
        #register a test user
        BaseTestCase.setUp(self)
        self.client.post('api/v2/auth/signup', data=json.dumps(self.sign_up_data),
        content_type='application/json')
        
        self.login_user = {'username':'thegeek',
                           'password':'werfg'}
        login_response = self.client.post('api/v2/auth/login', data=json.dumps(self.login_user),content_type='application/json')
        self.access_token = json.loads(login_response.data)['access_token']
        self.headers = {
            'Authorization': 'Bearer '+ self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    def tearDown(self):
        BaseTestCase.tearDown(self)

    def test_create_incidence(self):
        '''Test that a user can create an incidence of type red-flag or intervention'''
        response = self.client.post(
            'api/v2/interventions/', headers=self.headers, data=json.dumps(self.redflag_data)
        )
        data = json.loads(response.data)
        self.assertEqual(data['data'][0]['message'], 'Created incidence record')
        self.assertTrue(response.status_code == 200)


    def test_create_incidence_with_empty_type(self):
        response = self.client.post(
            'api/v2/interventions/', headers=self.headers, data=json.dumps(self.redflag_data_with_empty_type)
            )
        data = json.loads(response.data)
        self.assertEqual(data['message'], {'message': 'Fields cannot be blank'})
        self.assertTrue(response.status_code==400)

    def test_create_incidence_with_empty_location(self):
        response = self.client.post(
            'api/v2/interventions/', headers=self.headers, data=json.dumps(self.redflag_data_empty_location)
            )
        data = json.loads(response.data)
        self.assertEqual(data['message'], {'message': 'Fields cannot be blank'})
        self.assertTrue(response.status_code==400)
    
    def test_get_all_incedence(self):
        '''Test that a user can get all the incidences'''
        response = self.client.get(
             'api/v2/interventions/', headers=self.headers
        )
        self.assertTrue(response.status_code == 200)

    