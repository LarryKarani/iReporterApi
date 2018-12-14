import webargs
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required

# local import
from app.api.v2.models.users import User
from app.api.v2.models.users import admin_required
from app.api.v2.models.incident import Incidents
from app.api.v2.validators.validate_incident import (IncidenceSchema,
                                                     UpdateLocationSchema,
                                                     UpdateCommentSchema,
                                                     UpdateStatusSchema)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}
v2_incident = Namespace(
    'interventions', authorizations=authorizations, security='apikey')

incident_data = v2_incident.model('Interventions', {
    'incidence_type': fields.String(
        description='name of the user creating the red-flag'),
    'location': fields.String(
        description='name of the user creating the red-flag'),
    'comment': fields.String(
        description='name of the user creating the red-flag')
})


class Incidences(Resource, Incidents):
    @v2_incident.expect(incident_data)
    @v2_incident.doc(security='apikey')
    @jwt_required
    def post(self):
        '''Create a new incidence'''
        data = v2_incident.payload
        schema = IncidenceSchema()
        results = schema.load(data)

        # get errors if any
        errors = results.errors
        incidence_fields = ['createdBy',
                            'location', 'incidence_type', 'comment']
        for error in incidence_fields:
            if error in errors.keys():
                return{'message': 'Invalid or missing {}'.format(error)}, 400

        current_user = get_jwt_identity()
        new_instance = Incidents(
            current_user,
            data['incidence_type'],
            data['location'],
            data['comment']
        )
        id = new_instance.create_an_incident()

        return {
            'status': 201,
            'data': [{
                'incident': data,
                'message':  'Created incidence record'
            }]
        }, 201

    @v2_incident.doc(security='apikey')
    @jwt_required
    def get(self):
        '''gets all incidences available in the db'''
        incidents = self.get_all_incidents()
        if len(incidents) == 0:
            return {'status': 200,
                    'message': 'No records available'}

        # convert the tuble to a list of dicts
        keys = ['id', 'createdon', 'createdby',
                'type', 'location', 'status', 'comment']
        output = []
        for values in incidents:
            output.append(dict(zip(keys, values)))

        return {
            "status": 200,
            "data": output
        }


@v2_incident.header("Authorization", "Access tokken", required=True)
class AnIncident(Resource, Incidents):
    '''get a single incident'''
    @v2_incident.doc(security='apikey')
    @jwt_required
    def get(self, incident_id):
        '''Returns details of a specific incidence'''

        keys = ['id', 'createdon', 'createdby',
                'type', 'location', 'status', 'comment']
        incident = self.get_an_incident(incident_id)
        if not incident:
            return {'message': 'Incident does not exist'}, 404

        output = dict(zip(keys, incident))
        return {
            'status': 200,
            'data': [output]
        }

    @v2_incident.doc(security='apikey')
    @jwt_required
    def delete(self, incident_id):
        '''deletes a specific incident'''
        incident = self.get_an_incident(incident_id)
        if not incident:
            return {
                'message': 'Incident with given id {} does not exist'
                .format(incident_id)}, 404
        self.delete_incident(incident_id)
        return {
            'status': 200,
            'id': incident[0],
            'message': 'record deleted successfully'
        }, 200


update_location = {"location": webargs.fields.Str(required=True)}
# documentation
update_location_args_model = v2_incident.model(
    "update_location_args", {"location": fields.String(required=True)})


@v2_incident.header("Authorization", "Access tokken", required=True)
class UpdateLocation(Resource, Incidents):
    @v2_incident.doc(body=update_location_args_model, security='apikey')
    @jwt_required
    def patch(self, incident_id):
        '''changes location of an incidence'''

        data = v2_incident.payload
        if not data:
            return {'message': 'Please input data'}, 400

        loc = data['location']

        if loc.strip() == '':
            return {'message': 'Please provide a valid location'}, 400
        schema = UpdateLocationSchema()
        results = schema.load(data)
        errors = results.errors
        update_location_field = ['location']
        for error in update_location_field:
            if error in errors.keys():
                return{'message': 'Invalid or missing {}'.format(error)}, 400

        target = self.get_an_incident(incident_id)
        if not target:
            return {'message': 'Incident does not exist'}, 404

        if target[5] != 'Draft':
            return {"message": "You cant change location for this intervention\
             its status is changed"}, 204

        else:
            self.update_location(incident_id, data['location'])
            target = self.get_an_incident(incident_id)
            keys = ['id', 'createdon', 'createdby',
                    'type', 'location', 'status', 'comment']
            output = dict(zip(keys, target))
            return {
                'status': 200,
                "data": [output],
                "id": target[0],
                "message": "Updated red-flag record’s location"
            }


update_comment = {"comment": webargs.fields.Str(required=True)}
update_comment_args_model = v2_incident.model(
    "update_comment_args", {"comment": fields.String(required=True)})


@v2_incident.header("Authorization", "Access tokken", required=True)
class UpdateComment(Resource, Incidents):
    @v2_incident.doc(body=update_comment_args_model, security='apikey')
    @jwt_required
    def patch(self, incident_id):
        '''allows a user to change the comment of an incident'''
        data = v2_incident.payload
        if not data:
            return {'message': 'Please input data'}, 400

        comment = data['comment']
        if comment.strip() == '':
            return {'message': 'please provide a valid comment'}, 400

        if not isinstance(comment, str):
            return {'message': 'Comment cannot be a number'}, 400

        schema = UpdateCommentSchema()
        results = schema.load(data)
        errors = results.errors
        update_location_field = ['comment']

        for error in update_location_field:
            if error in errors.keys():
                return{'message': 'Invalid or missing {}'.format(error)}, 400

        target = self.get_an_incident(incident_id)
        if not target:
            return {'message': 'Incident does not exist'}, 404

        status = target[5]
        if status != 'Draft':
            return {"message": "You cant change the comment for this\
            intervention its status is {}".format(status)}, 204

        self.update_comment(incident_id, comment)
        target = self.get_an_incident(incident_id)
        keys = ['id', 'createdon', 'createdby',
                'type', 'location', 'status', 'comment']
        output = dict(zip(keys, target))

        return {
            'status': 200,
            "data": [output],
            "id": target[0],
            "message": "Updated red-flag record’s comment"
        }, 200


update_status = {"status": webargs.fields.Str(required=True)}
update_status_args_model = v2_incident.model(
    "update_status_args", {"status": fields.String(required=True)})


@v2_incident.header("Authorization", "Access tokken", required=True)
class UpdateStatus(Resource, Incidents, User):

    @v2_incident.doc(body=update_status_args_model, security='apikey')
    @jwt_required
    @admin_required
    def patch(self, incident_id):
        '''allow admin to change the status of an incidence'''

        current_user = get_jwt_identity()
        user = User.check_username(current_user)

        data = v2_incident.payload
        schema = UpdateStatusSchema()
        results = schema.load(data)
        errors = results.errors
        update_status_field = ['status']

        for error in update_status_field:
            if error in errors.keys():
                return{'message': 'Invalid or missing {}'.format(error)}, 400

        target = self.get_an_incident(incident_id)
        if not target:
            return {'message': 'Incident does not exist'}, 404

        else:
            status = data['status']
            self.update_status(incident_id, status)
            target = self.get_an_incident(incident_id)
            keys = ['id', 'createdon', 'createdby',
                    'type', 'location', 'status', 'comment']
            output = dict(zip(keys, target))

            return {
                'status': 200,
                "data": [output],
                "id": target[0],
                "message": "Updated incidence record’s status"
            }, 200
