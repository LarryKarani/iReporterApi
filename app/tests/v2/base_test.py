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
            "phoneNumber":"07020103",
            "username":"thegeek"
        }

    def tearDown(self):
        self.db_obj.drop_all_tables()
        self.client = None


if __name__ == '__main__':
    unittest.main(verbosity=2)