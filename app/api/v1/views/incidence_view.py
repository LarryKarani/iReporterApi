import webargs
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required

#local import 
from app.api.v1.models.incidence_model import Incidence, db
from app.api.v1.validators.validate_incidence import IncidenceSchema

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}

v1_incidence = Namespace('red-flags', authorizations=authorizations, security='apikey')

incidence_data = v1_incidence.model('Incidences',{
                       'createdBy' :fields.String(description='name of the user creating the red-flag'), 
                       'incidence_type' :fields.String(description='name of the user creating the red-flag'),       
                       'location' :fields.String(description='name of the user creating the red-flag'),
                       'comment': fields.String(description='name of the user creating the red-flag')
})

@v1_incidence.header("Authorization", "Access tokken", required=True)
class Incidences(Resource):
    '''Shows a list of all incedences and allow users to create a new incedence'''
    @v1_incidence.doc(security='apikey')
    @jwt_required
    def get(self):
        '''gets all incidences available in the db'''
        if len(db) == 0:
            return {'status':200,
                     'message': 'no records available'}
        return db, 200

    
    @v1_incidence.expect(incidence_data)
    @v1_incidence.doc(security='apikey')
    @jwt_required
    def post(self):
        '''Create a new incidence'''

        data = v1_incidence.payload
        schema = IncidenceSchema()

        results=schema.load(data)

        #get error if any
        errors = results.errors
        incidence_fields = ['createdBy', 'location', 'incidence_type', 'comment']
        for error in incidence_fields:
            if error in errors.keys():
                return{'message': errors[error][0]}, 400

        new_instance = Incidence()
        output = new_instance.create_incidence(data['createdBy'],data['incidence_type'], data['location'],data['comment'])
        return {
                'status' : 201, 
                'data' : [{
                           'id' : output['id'],   
                           'message' :  'Created incidence record'
                           }]
               }

@v1_incidence.header("Authorization", "Access tokken", required=True)
class AnIncidence(Resource):
    '''gets a single incidence, updates an incidence, change the status of an incidence'''

    @v1_incidence.doc(security='apikey')
    @jwt_required
    def get(self, red_id):
        '''Returns details of a specific incidence'''
        new_instance = Incidence()
        response=new_instance.get_an_incidence(red_id)    
        if len(response)==0:
            return {'message': 'Incident does not exist'}, 400

        return {
                  'status': 200, 
                  'data' : response
               }
    @v1_incidence.doc(security='apikey')
    @jwt_required
    def delete(self, red_id):
        '''deletes a specific incident'''
        new_instance = Incidence()
        output = new_instance.delete(red_id)

        if len(output)==0:
            return {'message': 'Incident with given id {} does not exist'.format(red_id)}, 400

        return {
             'status':200,
             'id' : output[0]['id'],
             'message': 'record deleted successfully'
              }

update_location = {"location": webargs.fields.Str(required=True)}

#documentation
update_location_args_model = v1_incidence.model(
        "update_location_args", {"location": fields.String(required=True)})

@v1_incidence.header("Authorization", "Access tokken", required=True)
class UpdateLocation(Resource):
    @v1_incidence.doc(body=update_location_args_model, security='apikey')
    @jwt_required
    def patch(self, red_id):
        '''changes location of an incidence'''

        data = v1_incidence.payload
        if not data:
            return {'message':'Please input data'}, 400

        loc = data['location']
        
        if loc.strip() =='':
            return {'message': 'Please provide a valid location'}, 400
        if not isinstance(loc, str):
            return {'message': 'location cannot be a number'}, 400
        new_instance = Incidence()
        target = new_instance.location_patcher(red_id, data['location'])
        if target == 'Not allowed':
            return {"message": "You cant change location for this intervention its status is changed"}, 204

        if not target:
            return {'message': 'Incident does not exist'}, 404

        else:
            return {
                 'status':200, 
                 "data" : [target],
                 "id" : target['id'],
                 "message" : "Updated red-flag record’s location"
             }

update_comment = {"comment": webargs.fields.Str(required=True)}
update_comment_args_model = v1_incidence.model(
        "update_comment_args", {"comment": fields.String(required=True)})

@v1_incidence.header("Authorization", "Access tokken", required=True)
class UpdateComment(Resource):
    @v1_incidence.doc(body=update_comment_args_model, security='apikey')
    @jwt_required
    def patch(self, red_id):
        '''allows a user to change the location of an incidence'''
        data = v1_incidence.payload
        if not data:
            return {'message':'Please input data'}, 400

        comment = data['comment']
        if comment.strip() == '':
            return {'message': 'please provide a valid comment'}, 400

        if not isinstance(comment, str):
            return {'message': 'Comment cannot be a number'}, 400

        new_instance = Incidence()
        target = new_instance.comment_patcher(red_id, comment)
        if target == 'Not allowed':
            return {"message": "You cant change the comment for this intervention its status is changed"}, 204

        if not target:
            return {'message': 'Incident does not exist'}

        else:
            return {
                 'status':200, 
                 "data" : [target],
                 "id" : target['id'],
                 "message" : "Updated red-flag record’s comment"
             }

update_status = {"status": webargs.fields.Str(required=True)}
update_status_args_model = v1_incidence.model(
        "update_status_args", {"status": fields.String(required=True)})

@v1_incidence.header("Authorization", "Access tokken", required=True)
class UpdateStatus(Resource):
    @v1_incidence.doc(body=update_status_args_model, security='apikey')
    @jwt_required
    def patch(self, red_id):
        '''allow admin to change the status of an incidence'''
        data = v1_incidence.payload
        if not data:
            return {'message':'Please input data'}, 400
        status = data['status']

        if status.strip() == '':
            return {'message': 'Please provide a valid status'}, 400

        if not isinstance(status, str):
            return {'message': 'Comment cannot be a number'}, 400
            
        statuses = ['draft', 'under-review', 'accepted', 'rejected']
        if status not in statuses:
            return {'message', 'Invalid status'}, 400

        new_instance = Incidence()
        target = new_instance.change_status(red_id, status)

        if target == 'Not allowed':
            return {"message": "You cant change the comment for this intervention its status is changed"}, 204

        if not target:
            return {'message': 'Incident does not exist'},404

        else:
            return {
                 'status':200, 
                 "data" : [target],
                 "id" : target['id'],
                 "message" : "Updated incidence record’s status"
             }
             