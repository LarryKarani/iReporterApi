import unittest
from app import create_app

from app.api.v2.models.users import Db


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.db_obj = Db()

        self.db_obj.drop_all_tables()
        self.db_obj.create_tables()

        self.client = self.app.test_client()
        # users
        self.sign_up_data = {
            "firstname": "larry",
            "lastname": "kubende",
            "othername": "karani",
            "email": "ka@gmail.com",
            "password": "werfg",
            "phoneNumber": "0702010376",
            "username": "thegeek"
        }

        self.invalid_phone = {
            "firstname": "larry",
            "lastname": "kubende",
            "othername": "karani",
            "email": "ka@gmail.com",
            "password": "werfg",
            "phoneNumber": "070201",
            "username": "thegeek"
        }

        self.invalid_firstname = {"firstname": " ",
                                  "lastname": "kubende",
                                  "othername": "karani",
                                  "email": "ka@gmail.com",
                                  "password": "werfg",
                                  "phoneNumber": "0702010376",
                                  "username": "thegeek"

                                  }

        self.login_data = {
            "password": "werfg",
            "username": "thegeek"

        }

        self.wrong_data = {
            "password": "wjames",
            "username": "thegeek"

        }

        self.wrong_password = {
            "password": "wetrr",
            "username": "thegeek"

        }

        self.empty_username = {
            "password": "werfg",
            "username": " "

        }

        self.empty_password = {
            "password": " ",
            "username": "thegeek"
        }

        # incident_data
        self.incident_data = {
            "createdBy": "thegeek",
            "incidence_type": "red-flag",
            "location": "90.0, 180.0",
            "comment": "String"
        }

        self.redflag_data = {
            "createdBy": "thegeek",
            "incidence_type": "red-flag",
            "location": "90.0, 180.0",
            "comment": "String"
        }

        self.redflag_data_invalid_incident_type = {
            "createdBy": "thegeek",
            "incidence_type": "red-uuu",
            "location": "90.0, 180.0",
            "comment": "String"
        }

        self.redflag_data_with_empty_created = {
            "createdBy": " ",
            "incidence_type": "red-flag",
            "location": "90.0, 180.0",
            "comment": "String"
        }
        self.redflag_data_with_empty_type = {
            "createdBy": "thegeek",
            "incidence_type": " ",
            "location": "90.0, 180.0",
            "comment": "String"
        }

        self.redflag_data_empty_location = {
            "createdBy": "thegeek",
            "incidence_type": "red-flag",
            "location": " ",
            "comment": "String"
        }
        self.redflag_data_empty_comment = {
            "createdBy": "thegeek",
            "incidence_type": "red-flag",
            "location": "90.0, 180.0",
            "comment": " "
        }
        self.redflag_data_invalid_location = {
            "createdBy": "thegeek",
            "incidence_type": "red-flag",
            "location": "long, lat",
            "comment": "String"
        }
        self.location_data = {
           "location": "90.0, 180.0",
        }
        self.comment_data = {
            "comment": "hey you"
        }

        self.update_redflag_status = {
            "status": "3333,5555"
        }

        self.invalid_location = {
            "location": "@#$%^&,@#$%^&"
        }
        self.invalid_comment = {
            "comment": "@#$%^&,@#$%^&"
        }
        self.status_data = {
            "status": "resolved"
        }

        self.invalid_status_data = {
            "status": "@#$%^&,@#$%^&"
        }

    def tearDown(self):
        self.db_obj.drop_all_tables()
        self.client = None


if __name__ == '__main__':
    unittest.main(verbosity=2)
