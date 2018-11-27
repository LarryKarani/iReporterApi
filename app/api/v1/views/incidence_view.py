from flask_restplus import Resource, fields, Namespace
import werkzeug


#local import 
from app.api.v1.models.incidence_model import Incidence, db

v1_incedence = Namespace('red-flags')

incidence_data = v1_incedence.model('Incidence',{
                       'createdBy' :fields.String(description='name of the user creating the red-flag'), 
                       'type' :fields.String(description='name of the user creating the red-flag'),       
                       'location' :fields.String(description='name of the user creating the red-flag'),
                       'comment': fields.String(description='name of the user creating the red-flag')
})

class Incidences(Resource):
    '''Shows a list of all incedences and allow users to create a new incedence'''

    def get(self):
        '''List all incidence'''

        return db, 200


    @v1_incedence.expect(incidence_data)
    def post(self):
        '''Create a new incidence'''

        data = v1_incedence.payload
        new_instance = Incidence()
        output = new_instance.create_incidence(data['createdBy'],data['type'], data['location'],data['comment'])
        return {
                'status' : 201, 
                'data' : [{
                           'id' : output['id'],   
                           'message' :  'Created red-flag record'
                           }]
               }

class AnIncidence(Resource):
    '''gets a single incidence, updates an incidence, change the status of an incidence'''
  
    def get(self, red_id):
        '''Returns details of a specific incidence'''
        new_instance = Incidence()
        response=new_instance.get_an_incidence(red_id)
        if len(response)==0:
            return {'message': 'incidence does not exist'}, 400

        return {
                  'status': 200, 
                  'data' : response
               }

    def delete(self, red_id):
        '''deletes a specific incidence'''
        new_instance = Incidence()
        response = new_instance.delete(red_id)

        if len(response)==0:
            return {'message': 'incidence does not exist'}, 400

        return {
             'status':200,
             'data' : response
              }
       



v1_incedence.add_resource(Incidences, '/' , strict_slashes=False)
v1_incedence.add_resource(AnIncidence, '/<int:red_id>', strict_slashes=False)

        


    
      
