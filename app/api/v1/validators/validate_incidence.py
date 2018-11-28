'''This module incidence related inputs validation'''

import re
from marshmallow import Schema, fields,  validates, ValidationError


def validate_length(input):
    if input.strip()=='':
        raise ValidationError({'message':'fields cannot be blanck'})

    #remove special characters
    elif not re.match(r"^(?=.*[a-z])[a-zA-Z0-9_.-]{3,25}$", input):
        raise ValidationError("{} is not a valid input".format(input))

class IncidenceSchema(Schema):
    '''Validates incidence data'''

    createdBy =    fields.String(required=True, validate=validate_length)
    location  = fields.String(required=True, validate=validate_length)
    comment   = fields.String(required=True,  validate=validate_length)
    incidence_type =fields.String(required=True, validate=validate_length)

    


