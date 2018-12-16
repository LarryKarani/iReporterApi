import json
from .base_test import BaseTestCase
from app.api.v2.models.incident import Incidents
from app.api.v2.models.users import User


class TestRegesterUser(BaseTestCase):
    def test_create_icident(self):
        data = self.incident_data
        dat = self.sign_up_data
        new_user = User(dat['firstname'],
                        dat['lastname'],
                        dat['othername'],
                        dat['email'],
                        dat['phoneNumber'],
                        dat['username'],
                        dat['password']
                        )
        new_user.register_user()
        new_incident = Incidents(data['createdBy'],
                                 data['incidence_type'],
                                 data['location'],
                                 data['comment']
                                 )
        new_incident.create_an_incident()
        output = new_incident.get_an_incident(1)
        self.assertIn(data['createdBy'], output)

    def test_get_an_incident(self):
        data = self.incident_data
        dat = self.sign_up_data
        new_user = User(dat['firstname'],
                        dat['lastname'],
                        dat['othername'],
                        dat['email'],
                        dat['phoneNumber'],
                        dat['username'],
                        dat['password']
                        )
        new_user.register_user()
        new_incident = Incidents(data['createdBy'],
                                 data['incidence_type'],
                                 data['location'],
                                 data['comment']
                                 )
        new_incident.create_an_incident()
        output = new_incident.get_an_incident(1)[2]
        self.assertEqual(data['createdBy'], output)

    def test_get_all_incident(self):
        data = self.incident_data
        dat = self.sign_up_data
        new_user = User(dat['firstname'],
                        dat['lastname'],
                        dat['othername'],
                        dat['email'],
                        dat['phoneNumber'],
                        dat['username'],
                        dat['password']
                        )
        new_user.register_user()
        new_incident = Incidents(data['createdBy'],
                                 data['incidence_type'],
                                 data['location'],
                                 data['comment']
                                 )
        new_incident.create_an_incident()
        output = new_incident.get_an_incident(1)
        self.assertIn(data['createdBy'], output)
