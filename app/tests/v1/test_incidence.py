import json

#local imports
from .base_test import BaseTestCase

class TestCreateIncidence(BaseTestCase):
    def setUp(self):
        #register a test user
        BaseTestCase.setUp(self)

        self.client.post('api/v1/auth/register', data=json.dumps(self.test_user),
        content_type='application/json')

        
        self.login_user = {'username':'larrythegeek',
                           'password':'6398litein'}

    
        login_response = self.client.post('api/v1/auth/login', data=json.dumps(self.login_user),content_type='application/json')

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
            'api/v1/red-flags/', headers=self.headers, data=json.dumps(self.redflag_data)
        )
        self.assertTrue(response.status_code == 200)

    def test_get_all_incedence(self):
        '''Test that a user can get all the incidences'''
        response = self.client.get(
             'api/v1/red-flags/', headers=self.headers
        )
        self.assertTrue(response.status_code == 200)

    def test_get_an_incidence(self):
        '''Test user can get a specific incidence given its id'''

        self.client.post(
            'api/v1/red-flags/', headers=self.headers, data=json.dumps(self.redflag_data)
        )

        response = self.client.get(
             'api/v1/red-flags/1', headers=self.headers
        )
        self.assertTrue(response.status_code == 200)

    
    def test_update_location(self):

        self.client.post(
            'api/v1/red-flags/', headers=self.headers, data=json.dumps(self.redflag_data)
        )

        response = self.client.patch(
             'api/v1/red-flags/1/location', headers=self.headers, data=json.dumps(self.location_data)
        )

        self.assertTrue(response.status_code == 200)

    def test_update_comment(self):

        self.client.post(
            'api/v1/red-flags/', headers=self.headers, data=json.dumps(self.redflag_data)
        )

        response = self.client.patch(
             'api/v1/red-flags/1/comment', headers=self.headers, data=json.dumps(self.comment_data)
        )

        self.assertTrue(response.status_code == 200)

    def test_delete_incidence(self):
        self.client.post(
            'api/v1/red-flags/', headers=self.headers, data=json.dumps(self.redflag_data)
        )

        response = self.client.delete(
             'api/v1/red-flags/1', headers=self.headers)

        self.assertTrue(response.status_code == 200)
        






