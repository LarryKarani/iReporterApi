from flask_restplus import Resource, fields, Namespace
import werkzeug


#local import 
from app.api.v1.models.incidence_model import Incidence, db

v1_incedence = Namespace('Incedences')

incidence_data = v1_incedence.model('Incidence',{
                       'createdBy' :fields.String(description='name of the user creating the red-flag'), 
                       'type' :fields.String(description='name of the user creating the red-flag'),       
                       'location' :fields.String(description='name of the user creating the red-flag'),
                       'comment': fields.String(description='name of the user creating the red-flag')
})

class Incedence(Resource):
    '''Shows a list of all incedences and allow users to create a new incedence'''

    @v1_incedence.doc('list_incedence')
    def get(self):
        '''List all tasks'''

        return db, 200


    @v1_incedence.expect(incidence_data)
    def post(self):
        '''Create a new incidence'''

        data = v1_incedence.payload
        new_instance = Incidence(data['createdBy'],data['type'], data['location'],data['comment'])
        output = new_instance.create_incidence()
        return {
            "message": "incedence created",
            "data": output
        
        }

v1_incedence.add_resource(Incedence, '/incidence', strict_slashes=False)

        


    
      
