'''This module incidence related inputs validation'''
import re
from marshmallow import Schema, fields,  validates, ValidationError

def validate_length(input):
    if input.strip()=='':
        raise ValidationError({'message':'Fields cannot be blank'})

class IncidenceSchema(Schema):
    '''Validates incidence data'''

    location  = fields.String(required=True, validate=validate_length)
    comment   = fields.String(required=True,  validate=validate_length)
    incidence_type =fields.String(required=True, validate=validate_length)

    @validates('comment')
    def validate_comment(self, comment):
        
        r = re.compile("^[A-Za-z0-9.,:;!?'$()\s]+$")
        if comment.strip() == '':
            raise ValidationError('Fields cannot be blank')
        elif not r.match(comment):
            raise ValidationError("{} is not a valid comment".format(comment))

    @validates('location')
    def validate_location(self, location):
        r = re.compile("^[0-9]+(,[0-9]+)*$")
        if location.strip() == '':
            raise ValidationError('Fields cannot be blank')
        elif not r.match(location):
            raise ValidationError("{} is not a valid location".format(location))

class UpdateCommentSchema(Schema):
    '''validates update incident data'''
    comment = fields.String(required=True, validate=validate_length)

    @validates('comment')
    def validate_location(self, comment):
        r = re.compile("^[a-zA-Z ]*$")
        if comment.strip() == '':
            raise ValidationError('Fields cannot be blank')
        elif not r.match(comment):
            raise ValidationError("{} is not a valid comment".format(comment))

class UpdateLocationSchema(Schema):
    '''validates update incident data'''
    location = fields.String(required=True, validate=validate_length)

    @validates('location')
    def validate_location(self, location):
        r = re.compile("^[0-9]+(,[0-9]+)*$")
        if location.strip() == '':
            raise ValidationError('Fields cannot be blank')
        elif not r.match(location):
            raise ValidationError("{} is not a valid location".format(location))

class UpdateStatusSchema(Schema):
    '''validates update incident data'''
    status = fields.String(required=True, validate=validate_length)
    @validates('status')
    def validate_location(self, status):
        status_option = ['resolved', 'under investigation', 'draft']
        r = re.compile("^[a-zA-Z ]*$")
        if status.strip() == '':
            raise ValidationError('Fields cannot be blank')
        elif not r.match(status):
            raise ValidationError("{} is not a valid status".format(status))
        elif status.lower() not in status_option:
            raise ValidationError("{} status can only be 'under investigation', 'draft' or resolved".format(status))
