'''This module incidence related inputs validation'''

import re
from marshmallow import Schema, fields,  validates, ValidationError


def validate_length(input):
    if input.strip()=='':
        raise ValidationError({'message':'fields cannot be blank'})


class IncidenceSchema(Schema):

    '''Validates incidence data'''

    createdBy =    fields.String(required=True, validate=validate_length)
    location  = fields.String(required=True, validate=validate_length)
    comment   = fields.String(required=True,  validate=validate_length)
    incidence_type =fields.String(required=True, validate=validate_length)

    @validates('comment')
    def validate_length(self, comment):
        if comment.strip() == '':
            raise ValidationError('fields cannot be blank')
        elif not comment.isalpha():
            return {'message': "invalid comment"}
        