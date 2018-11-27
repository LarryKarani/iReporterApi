"""This module contains the incidence model"""
import datetime

db = []

class Incidence:
    def __init__(self):
        self.db = db

    def create_incidence(self,createdBy, incidence_type, location, comment):
        data = {}
        data['id'] = len(db)+1
        data['createdBy'] = createdBy
        data['status'] = 'draft'
        data['type']= incidence_type
        data['location'] = location
        data['createdOn']= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.db.append(data)

        return data

   
    def get_all_incidence(self):
        '''gets all the incidences created'''
        return self.db

   
    def get_an_incidence(self, id):
        '''get a specific incedence with the provided id'''
        output = [incidence for incidence in db if incidence['id']== id]
       
        return output
    
    def update(self, id, data):
        '''updates a specific incidence'''
        incidence = self.get_an_incidence(id)
        if len(incidence)==0:
            return {"message": "incidence does not exist"},400
        #check to see if the status has been changed
        if incidence[0]['status']!= 'draft':
            return {'message': 'This incidence cannot be updated its status is {}'.format(incidence['status'])}, 401

        incidence.update(data)

        return incidence

    def delete(self, id):
        '''delete a specific incidence'''
        incidence = self.get_an_incidence(id)
        
        if len(incidence)==0:
            return incidence

        self.db.remove(incidence[0])
        return incidence

    def change_status(self, id, status):
        '''allows admin to change the status of an inncidence'''

        incidence = self.get_an_incidence(id)
        if len(incidence)==0:
            return {"message": "incidence does not exist"},400

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
