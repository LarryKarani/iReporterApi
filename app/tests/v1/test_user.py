import json
from .base_test import BaseTestCase

class TestRegister(BaseTestCase):
    def test_user_register(self):
        response = self.client.post('api/v1/auth/register', data=json.dumps(self.user_data), content_type='application/json')
        self.assertTrue(response.status_code==201)

    def test_missing_data_register(self):
        invalid_data = {
            'firstname':'larryTheGeek',
            'lastname':'kubende'

        }

        response = self.client.post('api/v1/auth/register', data=json.dumps(invalid_data), content_type='application/json')
        self.assertTrue(response.status_code == 400)


    def test_user_register_existing_users(self):
        #signup a new user
        response = self.client.post('api/v1/auth/register', data=json.dumps(self.user_data), content_type='application/json')
        self.assertTrue(response.status_code == 201)

        #signup existing user
        response = self.client.post('api/v1/auth/register', data=json.dumps(self.user_data), content_type='application/json')
        self.assertTrue(response.status_code == 400)