import unittest
from instance import create_app

from app.api.v2.models.users import Db
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.db_obj = Db()
    
        self.db_obj.drop_all_tables()
        self.db_obj.create_tables()

        self.client = self.app.test_client()

        self.sign_up_data = {
            "firstname":"larry",
            "lastname":"kubende",
            "othername":"karani",
            "email":"ka@gmail.com",
            "password":"werfg",
            "phoneNumber":"0702010376",
            "username":"thegeek"
        }

        self.invalid_phone = {
            "firstname":"larry",
            "lastname":"kubende",
            "othername":"karani",
            "email":"ka@gmail.com",
            "password":"werfg",
            "phoneNumber":"070201",
            "username":"thegeek"
        }
        
        self.invalid_firstname = {
            "firstname":" ",
            "lastname":"kubende",
            "othername":"karani",
            "email":"ka@gmail.com",
            "password":"werfg",
            "phoneNumber":"0702010376",
            "username":"thegeek"
        }

        self.login_data = {
             "password":"werfg",
             "username":"thegeek"

        }

        self.wrong_data = {
            "password":"wjames",
             "username":"thegeek"

        }

        self.wrong_password = {
             "password":"wetrr",
             "username":"thegeek"

        }

        self.empty_username = {
             "password":"werfg",
             "username":" "

        }

        self.empty_password = {
            "password":" ",
             "username":"thegeek"
        }

        self.incident_data = {
             "createdBy": "Larry karani",
             "incidence_type" : "red-flag",
             "location": "123456,23434",
             "comment":"String"
         }      

    def tearDown(self):
        self.db_obj.drop_all_tables()
        self.client = None


if __name__ == '__main__':
    unittest.main(verbosity=2)