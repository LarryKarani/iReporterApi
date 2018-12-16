import json
from .base_test import BaseTestCase
from app.api.v2.models.users import User


class TestRegesterUser(BaseTestCase):
    def test_user_register(self):
        data = self.sign_up_data
        new_user = User(data['firstname'],
                        data['lastname'],
                        data['othername'],
                        data['email'],
                        data['phoneNumber'],
                        data['username'],
                        data['password']
                        )
        new_user.register_user()
        output = new_user.get_a_user(1)

        self.assertIn(data['firstname'], output)
