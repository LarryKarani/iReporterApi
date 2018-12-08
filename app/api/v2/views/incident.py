import webargs
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required

#local import 
from app.api.v2.models.incident import Incidents
from app.api.v2.validators.validate_incident import IncidenceSchema

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}

v2_incident= Namespace('interventions', authorizations=authorizations, security='apikey')

incident_data = v2_incident.model('Interventions',{
                       'incidence_type' :fields.String(description='name of the user creating the red-flag'),       
                       'location' :fields.String(description='name of the user creating the red-flag'),
                       'comment': fields.String(description='name of the user creating the red-flag')
})


class Incidences(Resource, Incidents):
    @v2_incident.expect(incident_data)
    @v2_incident.doc(security='apikey')
    @jwt_required
    def post(self):
        '''Create a new incidence'''
        data = v2_incident.payload
        schema = IncidenceSchema()
        results=schema.load(data)

        #get error if any
        errors = results.errors
        incidence_fields = ['createdBy', 'location', 'incidence_type', 'comment']
        for error in incidence_fields:
            if error in errors.keys():
                return{'message': errors[error][0]}, 400
        
        current_user = get_jwt_identity()
        new_instance = Incidents( 
                                  current_user,
                                  data['incidence_type'],
                                  data['location'],
                                  data['comment']
                                )
        new_instance.create_an_incident()
        id = len(new_instance.get_all_incidents())
        return {
                'status' : 201, 
                'data' : [{
                           'id' : id,   
                           'message' :  'Created incidence record'
                           }]
               }
    @v2_incident.doc(security='apikey')
    @jwt_required
    def get(self):

        '''gets all incidences available in the db'''
        incidents = self.get_all_incidents()
        if len(incidents) == 0:
            return {'status':200,
                     'message': 'No records available'}
        
        #convert the tuble to a list of dicts
        keys = ['id', 'createdon', 'createdby', 'type','location', 'status', 'comment']
        output = []
        for values in incidents:
            output.append(dict(zip(keys, values)))

        return {
                "status": 200,
                "data":output
                }

    