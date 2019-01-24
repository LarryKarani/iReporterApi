import webargs
import json
import os

import cloudinary
import cloudinary.api
import cloudinary.uploader
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request, url_for, current_app

from werkzeug.utils import secure_filename
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

# UPLOAD_FOLDER = os.path.abspath("app/uploads")
# ALLOWED_EXTENSIONS = set(['mp4', 'png', 'jpg', 'jpeg'])


class Incidences(Resource, Incidents):
    @v2_incident.expect(incident_data)
    @v2_incident.doc(security='apikey')
    @jwt_required
    def post(self):

        # cloudinary config files

        cloudinary.config(
            cloud_name=os.getenv('cloud_name'),
            api_key=os.getenv("api_key"),
            api_secret=os.getenv("api_secret")

        )

        @staticmethod
        def allowed_file(filename):
            return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

        '''Create a new incidence'''
        if request.form:
            data = request.form
        else:
            data = json.loads(request.data)

        schema = IncidenceSchema()
        results = schema.load(data)

        # get errors if any
        errors = results.errors
        incidence_fields = ['createdBy',
                            'location', 'incidence_type', 'comment']
        for error in incidence_fields:
            if error in errors.keys():
                return{'message': 'Invalid or missing {}'.format(error)}, 400
        media_url = 'No image'
        if request.files:
            file = request.files['file']

            if not os.path.isdir(current_app.config['UPLOAD_FOLDER']):
                os.mkdir(current_app.config['UPLOAD_FOLDER'])

            filename = secure_filename(file.filename)

            filepath = os.path.join(
                current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            url = cloudinary.uploader.upload(filepath, public_id=filename)
            # url = cloudinary.utils.cloudinary_api_url(filename)
            media_url = url['secure_url']
        current_user = get_jwt_identity()
        new_instance = Incidents(
            current_user,
            data['incidence_type'],
            data['location'],
            data['comment'],
            media_url


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
                'type', 'location', 'status', 'comment', 'image']
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

        createdBy = incident[2]
        current_user = get_jwt_identity()
        if createdBy != current_user:
            return {"error":
                    "Not allowed to delete a comment you din't create"}, 405

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

        createdBy = target[2]
        current_user = get_jwt_identity()
        if createdBy != current_user:
            return {"error":
                    "Not allowed to edit a location you din't create"}, 403

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

        createdBy = target[2]
        current_user = get_jwt_identity()
        if createdBy != current_user:
            return {"error":
                    "Not allowed to edit a comment you din't create"}, 403
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


class UserIncidences(Resource, Incidents):
    @v2_incident.doc(security='apikey')
    @jwt_required
    def get(self):
        '''gets all incidences created by a specific user'''
        current_user = get_jwt_identity()
        incidents = self.get_all_incidents_created_by_a_user(current_user)
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
