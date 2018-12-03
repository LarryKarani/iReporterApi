'''This module incidence related inputs validation'''

import re
from marshmallow import Schema, fields,  validates, ValidationError


def validate_length(input):
    if input.strip()=='':
        raise ValidationError({'message':'fields cannot be blanck'})


class IncidenceSchema(Schema):
    '''Validates incidence data'''

    createdBy =    fields.String(required=True, validate=validate_length)
    location  = fields.String(required=True, validate=validate_length)
    comment   = fields.String(required=True,  validate=validate_length)
    incidence_type =fields.String(required=True, validate=validate_length)

    


