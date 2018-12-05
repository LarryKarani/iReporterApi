"""This module contains the incidence model"""
import datetime

db = []

class Incidence:
    counter = 1
    def __init__(self):
        self.db = db
        self.id = Incidence.counter

    def create_incidence(self,createdBy, incidence_type, location, comment):
        data = {}
        data['id'] = self.id
        data['createdBy'] = createdBy
        data['status'] = 'draft'
        data['type']= incidence_type
        data['location'] = location
        data['createdOn']= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.db.append(data)
        Incidence.counter += 1

        return data

   
    def get_all_incidence(self):
        '''gets all the incidences created'''
        return self.db

   
    def get_an_incidence(self, id):
        '''get a specific incedence with the provided id'''
        output = [incidence for incidence in db if incidence['id']== id]
       
        return output
    
    def location_patcher(self, red_id, value):
        """change value only if its still a draft"""
        incidence= self.get_an_incidence(red_id)
        if len(incidence)!= 0:
            if incidence[0]['status'] == 'draft':
                incidence[0]['location'] = value

                return incidence[0]

            else:
                 return 'Not allowed'

        return False

    def comment_patcher(self, red_id, value):
        """change value only if its still a draft"""
        incidence= self.get_an_incidence(red_id)
        if len(incidence)!= 0:
            if incidence[0]['status'] == 'draft':
                incidence[0]['comment'] = value

                return incidence[0]

            else:
                 return 'Not allowed'

        return False



        


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
            return False

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
    