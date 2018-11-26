from unittest import TestCase

#local imports
from instance import create_app
from app.api.v1.models import db

class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.db = db
        self.client = self.app.test_client()

        self.redflag_data = {
             "createdBy": "Larry karani",
             "type" : "red-flag",
             "location": "123456, 23434",
             "Images": [],
             "videos":[],
             "comment":"String"
         }      
        self.redflag_data_with_empty_created={
             "createdBy": " ",
             "type" : "red-flag",
             "location": "123456, 23434",
             "Images": [],
             "videos":[],
             "comment":"String"
        }
        self.redflag_data_with_empty_type ={
             "createdBy": "Larry karani",
             "type" : " ",
             "location": "123456, 23434",
             "Images": [],
             "videos":[],
             "comment":"String"
        }

        self.redflag_data_empty_location = {
             "createdBy": "Larry karani",
             "type" : "red-flag",
             "location": " ",
             "Images": [],
             "videos":[],
             "comment":"String"
         }

        self.redflag_data_empty_location = {
             "createdBy": "Larry karani",
             "type" : "red-flag",
             "location": " ",
             "Images": [],
             "videos":[],
             "comment":"String"
         }



        self.redflag_data_invalid_location = {
             "createdBy": "Larry karani",
             "type" : "red-flag",
             "location": "long, lat",
             "Images": [],
             "videos":[],
             "comment":"String"
         }

      
       
    

        self.update_redflag_data = {
             "createdBy": "james Irungu",
             "type" : "intervention",
             "location": " ",
             "Images": [],
             "videos":[],
             "comment":"String"
         }
        

        self.redflag_data_invalid_type = {
             "createdBy": "Larry karani",
             "type" : "bundesliga",
             "location": "long, lat",
             "Images": [],
             "videos":[],
             "comment":"String"
         }


    def tearDown(self):
        """clean Db"""
        self.db.clear()
        self.client=None

