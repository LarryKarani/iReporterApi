'''This module handles the validation of all data relating to the user'''

import re
from marshmallow import Schema, fields,  validates, ValidationError

def validate_length(input):
    if input.strip()=='':
        raise ValidationError({'message':'fields cannot be blanck'})



class UserSchema(Schema):
    firstname = fields.String(required=True, validate=validate_length)
    lastname = fields.String(required=True, validate=validate_length)
    othername = fields.String(required=True, validate=validate_length)
    email = fields.Email(required=True)
    phoneNumber = fields.String(required=True, validate=validate_length)
    username = fields.String(required=True, validate=validate_length)

    @validates('phoneNumber')
    def validate_phonenumber(self, phoneNumber):
        if len(phoneNumber)<10:
            raise ValidationError('phone number should be 10 characters  long')
    