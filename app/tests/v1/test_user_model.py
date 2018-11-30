"""This module contaiins unit tests for models used in application."""

from app.api.v1.models.incidence_model import Incidence
from app.api.v1.validators.validate_user import UserSchema
from app.api.v1.models.user_model import Users
from .base_test import BaseTestCase

class TestUser(BaseTestCase):
    def test_create_user(self):
        new_user = Users()
        new_user.create_user('larry','karani', 'kubende', 'karanilarry@gmail.com', '0701043047', 'larryTheGeek')
        
      
        self.assertTrue(new_user)

        user_created = new_user.get_email('karanilarry@gmail.com')

        self.assertTrue(user_created['username'], 'larryTheGeek')

    def test_get_user_by_id(self):
        new_user = Users()
        new_user.create_user('larry','karani', 'kubende', 'karanilarry@gmail.com', '0701043047', 'larryTheGeek')

        user_created = new_user.get_user(1)

        self.assertTrue(user_created['username']== 'larryTheGeek')
