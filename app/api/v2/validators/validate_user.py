'''This module handles the validation of all data relating to the user'''
import re
from marshmallow import Schema, fields,  validates, ValidationError


def validate_length(value):
    r = re.compile("^[A-Za-z0-9.,:;!?()\s]+$")
    if value.strip() == '' or len(value) < 2:
        raise ValidationError({'message': 'fields cannot be blank'})
    elif not r.match(value):
        raise ValidationError('invalid {}'.format(value))


class UserSchema(Schema):
    '''schema for validating signup data'''
    firstname = fields.String(required=True, validate=validate_length)
    lastname = fields.String(required=True, validate=validate_length)
    othername = fields.String(required=True, validate=validate_length)
    email = fields.Email(required=True)
    phoneNumber = fields.String(required=True, validate=validate_length)
    username = fields.String(required=True, validate=validate_length)
    password = fields.String(required=True, validate=validate_length)

    @validates('phoneNumber')
    def validate_phonenumber(self, phoneNumber):
        if len(phoneNumber) < 10:
            raise ValidationError('phone number should be 10 characters  long')
        elif not re.match('^[0-9]+$', phoneNumber):
            raise ValidationError('phone number should only contain digits')

    @validates('password')
    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError('password should be 8\
            or more characters long')


class LoginSchema(Schema):
    '''schema for validating login data'''
    username = fields.String(required=True, validate=validate_length)
    password = fields.String(required=True, validate=validate_length)
