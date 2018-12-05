import webargs
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import create_access_token

#local import
from app.api.v1.models.user_model import Users
from app.api.v1.validators.validate_user import UserSchema, LoginSchema

v1_user = Namespace('auth')

registration_args_model=v1_user.model(
    'Regestration', {
    "firstname": fields.String(description='username'),
    "lastname": fields.String(description='username'),
    "othername": fields.String(description='username'),
    "password": fields.String(description='password'),
    "email": fields.String(description='email'),
    "phoneNumber": fields.String(description='phoneNumber'),
    "username": fields.String(description='username')})

user_login = v1_user.model('Login', {'username': fields.String('email@example.com'),
                                     'password': fields.String('test_pass')})

class Register(Resource):
    @v1_user.expect(registration_args_model)
    def post(self):
        '''register a new user'''
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

    def get(self):
        users = Users()
        return users.get_all_users()

class Login(Resource):
    @v1_user.expect(user_login )
    def post(self):
        'logs in a user'
        data = v1_user.payload
        schema = LoginSchema()
        schema_data = schema.load(data)
        errors = schema_data.errors
        error_types = ['username', 'password']

        for e in error_types:
            if e in errors.keys():
                return {'message': errors[e][0]}, 400

        new_instance= Users()
        current_user=new_instance.get_username(data['username'])
        
        if not current_user:
            return {'message': 'username does not exist'}, 400
               
        if not (current_user['password']== data['password']):
            return {'message': f'invalid username or password'}, 400

        access_token = create_access_token(identity=data['username'])

        return {'message': 'logged in as {}'.format(data['username']),
                'access_token': access_token}, 200
