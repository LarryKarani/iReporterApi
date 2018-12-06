"""This module contaiins unit tests for models used in application."""

from app.api.v1.models.incidence_model import Incidence
from .base_test import BaseTestCase

class TestUser(BaseTestCase):
    def test_create_user(self):
        new_incidence = Incidence()
        new_incidence.create_incidence('larry','redflag', '123,134', 'hey stop')
        self.assertTrue(new_incidence)
        incidence_created = new_incidence.get_an_incidence(6)
        self.assertTrue(incidence_created[0]['createdBy'], 'larry')

    def test_get_incidence_by_id(self):
        new_incidence = Incidence()
        new_incidence.create_incidence('larry','redflag', '123,134', 'hey stop')
        incidence_created = new_incidence.get_an_incidence(7)
        self.assertTrue(incidence_created[0]['createdBy'], 'larry')
        