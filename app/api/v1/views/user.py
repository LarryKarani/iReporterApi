import webargs
from flask_restplus import Resource, fields, Namespace


#local import
from app.api.v1.models.user_model import Users
from app.api.v1.validators.validate_user import UserSchema, LoginSchema

v1_user = Namespace('auth')

registration_data =v1_user.model('Regestration', {
    "firstname": fields.String(description='username'),
    "lastname": fields.String(description='username'),
    "othername": fields.String(description='username'),
    "password": fields.String(description='password'),
    "email": fields.String(description='email'),
    "phoneNumber": fields.String(description='phoneNumber'),
    "username": fields.String(description='username')})


Login_data = v1_user.model('Login', {
    'username': fields.String(description='username'),
    'password': fields.String(description='password')
})

class Register(Resource):
    @v1_user.expect(registration_data)
    def post(self):
        '''Register a new user'''
        data = v1_user.payload
        schema = UserSchema()
        schema_data = schema.load(data)

        errors = schema_data.errors
        error_types = ['firstname', 'lastname', 'othername', 'password', 'email','phoneNumber','username']

        for e in error_types:
            if e in errors.keys():
                return {'message': errors[e][0]}, 400
        
        new_user = Users()
       #check if user already exists

        user = new_user.get_username(data['username'])
        if user:
            return {'message': 'username already exists'}, 400

        mail = new_user.get_email(data['email'])
        if mail:
            return {'message': 'email already exists'}, 400

        new_user.db.append(data)
        return {'message': 'user successfuly  added',
                 'data': data
                }, 201

v1_user.add_resource(Register, '/register', strict_slashes=False)
    
