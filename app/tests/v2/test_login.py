import json
from .base_test import BaseTestCase


class TestRegesterUser(BaseTestCase):
    def test_login(self):
        self.client.post('api/v1/auth/register', data=json.dumps(self.sign_up_data), content_type='application/json')
        response = self.client.post('api/v1/auth/login', data=json.dumps(self.login_data), content_type='application/json')
        self.assertEqual("logged in as thegeek", json.loads(response.data)['message'])
        self.assertTrue(response.status_code == 200)
    
    def test_unregestered_user_login(self):
        response = self.client.post('api/v1/auth/login', data=json.dumps(
            self.wrong_data), content_type='application/json')

        self.assertEqual("invalid username or password", json.loads(response.data)['message'])
        self.assertTrue(response.status_code == 400)
    def test_wrong_password_login(self):
        self.client.post('api/v1/auth/register', data=json.dumps(
            self.sign_up_data), content_type='application/json')
        response = self.client.post('api/v1/auth/login', data=json.dumps(
            self.wrong_password), content_type='application/json')
        print(json.loads(response.data)['message'])
        self.assertEqual("invalid username or password", json.loads(response.data)['message'])
        print(response.data)
        self.assertTrue(response.status_code == 400)

    def test_empty_username(self):
        self.client.post('api/v1/auth/register', data=json.dumps(
            self.sign_up_data), content_type='application/json')
        response = self.client.post('api/v1/auth/login', data=json.dumps(
            self.empty_username), content_type='application/json')
        self.assertEqual("fields cannot be blank", json.loads(response.data)['message']['message'])
        self.assertTrue(response.status_code == 400)
        
    def test_empty_password(self):
        self.client.post('api/v1/auth/register', data=json.dumps(
            self.sign_up_data), content_type='application/json')
        response = self.client.post('api/v1/auth/login', data=json.dumps(
            self.empty_password), content_type='application/json')
        self.assertEqual("fields cannot be blank", json.loads(response.data)['message']['message'])
        self.assertTrue(response.status_code == 400)
