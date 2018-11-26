"""This module contains the incidence model"""
import datetime

db = []

class Incidence:

    def __init__(self, createdBy, incidence_type, location, images, videos, comment):
        self.db = db
        self.counter = 0
        self.createdBy = createdBy
        self.status = 'draft'
        self.incidence_type = incidence_type
        self.location = location
        self.images = images
        self.videos = videos
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_incidence(self):
        data = {}
        data['id'] = self.counter
        data['createdBy'] = self.createdBy
        data['status'] = self.status
        data['incedence_type']= self.incidence_type
        data['location'] = self.location
        data['images']= self.images
        data['videos'] = self.videos
        data['createdOn']= self.createdOn

        self.db.append(data)

        return data

   
    def get_all_incidence(self):
        '''gets all the incidences created'''
        return self.db

    def get_an_incidence(self, id):
        '''get a specific incedence with the provided id'''
        output = [incidence for incidence in self.db if incidence['id']== id]
        if len(output) == 0:
           return {"message":"incidence does not exist"}, 400

        return output
    
    def update(self, id, data):
        '''updates a specific incedence'''
        incidence = self.get_an_incidence(id)
        #check to see if the status has been changed
        if incidence[0]['status']!= 'draft':
            return {'message': 'This incidence cannot be updated its status is {}'.format(incidence['status'])}, 401

        incidence.update(data)

        return incidence

    def delete(self, id):
        '''delete a specific incidence'''
        incidence = self.get_an_incidence(id)[0]
        self.db.remove(incidence)
    
    def change_status(self, id, status):
        '''allows admin to change the status of an inncidence'''

        incidence = self.get_an_incidence(id)
        data = incidence[0]['status']= status

        incidence.update(data)
        return incidence

    def get_all_red_flags(self):
        '''returns all incidence of type red-flag'''

        output = [incidence for incidence in self.db if incidence['type']== 'red-flag']
        return output
    
    def get_all_interventions(self):
        '''returns all interventions'''

        output = [incidence for incidence in self.db if incidence['type']== 'interventions']
        return output
