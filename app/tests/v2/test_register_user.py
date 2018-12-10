import json
from .base_test import BaseTestCase

class TestRegister(BaseTestCase):
    def test_user_register(self):
        response = self.client.post('api/v2/auth/signup', data=json.dumps(self.sign_up_data), content_type='application/json')
        self.assertTrue(response.status_code==201)

    def test_missing_data_register(self):
        invalid_data = {
            'firstname':'larryTheGeek',
            'lastname':'kubende'
        }
        response = self.client.post('api/v2/auth/signup', data=json.dumps(invalid_data), content_type='application/json')
        self.assertTrue(response.status_code == 400)

    def test_user_register_existing_users(self):
        #signup a new user
        response = self.client.post('api/v2/auth/signup', data=json.dumps(self.sign_up_data), content_type='application/json')
        self.assertTrue(response.status_code == 201)
        #signup existing user
        response = self.client.post('api/v2/auth/signup', data=json.dumps(self.sign_up_data), content_type='application/json')
        self.assertTrue(response.status_code == 400)

    def test_register_user_invalid_phone(self):
        response = self.client.post('api/v2/auth/signup', data=json.dumps(self.invalid_phone), content_type='application/json')
        self.assertTrue(response.status_code==400)
        self.assertTrue('phone number should be 10 characters  long' == json.loads(response.data)['message'])

    def test_register_user_empty_firstname(self):
        response = self.client.post('api/v2/auth/signup', data=json.dumps(self.invalid_firstname), content_type='application/json')
        self.assertTrue(response.status_code==400)
        self.assertIn('fields cannot be blank' , json.loads(response.data)['message']['message'])
