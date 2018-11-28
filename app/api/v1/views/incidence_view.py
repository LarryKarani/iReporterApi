import webargs
from flask_restplus import Resource, fields, Namespace
import werkzeug


#local import 
from app.api.v1.models.incidence_model import Incidence, db

v1_incidence = Namespace('red-flags')
update_location = {"createdBy": webargs.fields.Str(required=True),
                   "type": webargs.fields.Str(required=True),
                   "location": webargs.fields.Str(required=True),
                   "comment": webargs.fields.Str(required=True),}
incidence_data = v1_incidence.model('Incidences',{
                       'createdBy' :fields.String(description='name of the user creating the red-flag'), 
                       'type' :fields.String(description='name of the user creating the red-flag'),       
                       'location' :fields.String(description='name of the user creating the red-flag'),
                       'comment': fields.String(description='name of the user creating the red-flag')
})

class Incidences(Resource):
    '''Shows a list of all incedences and allow users to create a new incedence'''

    def get(self):
        '''gets all incidences available in the db'''
        return db, 200


    @v1_incidence.expect(incidence_data)
    def post(self):
        '''Create a new incidence'''

        data = v1_incidence.payload
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
        output = new_instance.delete(red_id)

        if len(output)==0:
            return {'message': 'incidence with given id {} does not exist'.format(red_id)}, 400

        return {
             'status':200,
             'data' : output
              }

update_location = {"location": webargs.fields.Str(required=True)}
update_location_args_model = v1_incidence.model(
        "update_location_args", {"location": fields.String(required=True)})
class UpdateLocation(Resource):
    @v1_incidence.doc(body=update_location_args_model)
    def patch(self, red_id):
        '''changes location of an incidence'''
        data = v1_incidence.payload
        new_instance = Incidence()

        target = new_instance.location_patcher(red_id, data['location'])
        if target == 'Not allowed':
            return {"message": "you cant change location for this intervention its status is changed"}, 204

        if not target:
            return {'message': 'incidence does not exist'}

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
class UpdateComment(Resource):
    @v1_incidence.doc(body=update_comment_args_model)
    def patch(self, red_id):
        '''changes location of an incidence'''
        data = v1_incidence.payload
        new_instance = Incidence()

        target = new_instance.location_patcher(red_id, data['location'])
        if target == 'Not allowed':
            return {"message": "you cant change the comment for this intervention its status is changed"}, 204

        if not target:
            return {'message': 'incidence does not exist'}

        else:
            return {
                 'status':200, 
                 "data" : [target],
                 "id" : target['id'],
                 "message" : "Updated red-flag record’s comment"
             }









v1_incidence.add_resource(Incidences, '/' , strict_slashes=False)
v1_incidence.add_resource(AnIncidence, '/<int:red_id>', strict_slashes=False)
v1_incidence.add_resource(UpdateLocation, '/<int:red_id>/location', strict_slashes=False)
v1_incidence.add_resource(UpdateComment, '/<int:red_id>/comment', strict_slashes=False)
        


    
      
