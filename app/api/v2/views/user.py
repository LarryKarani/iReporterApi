import webargs
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.api.v2.views import blacklist
from flask_jwt_extended import jwt_required, get_raw_jwt
# local import
from app.api.v2.models.users import User
from app.api.v2.validators.validate_user import UserSchema, LoginSchema


v2_user = Namespace('auth')
registration_args_model = v2_user.model(
    'Regestration', {
        "firstname": fields.String(description='username'),
        "lastname": fields.String(description='username'),
        "othername": fields.String(description='username'),
        "password": fields.String(description='password'),
        "email": fields.String(description='email'),
        "phoneNumber": fields.String(description='phoneNumber'),
        "username": fields.String(description='username')})

user_login = v2_user.model('Login',
                           {'username': fields.String('email@example.com'),
                            'password': fields.String('test_pass')})


class Register(Resource):
    @v2_user.expect(registration_args_model)
    def post(self):
        '''register a new user'''
        data = v2_user.payload
        schema = UserSchema()
        schema_data = schema.load(data)

        errors = schema_data.errors
        error_types = ['firstname', 'lastname', 'othername',
                       'password', 'email', 'phoneNumber', 'username']

        for e in error_types:
            if e in errors.keys():
                return {'message': 'Invalid or missing {}'.format(e),
                        'status': 400}, 400

        new_user = User(
            data['firstname'],
            data['lastname'],
            data['othername'],
            data['email'],
            data['phoneNumber'],
            data['username'].lower(),
            data['password']
        )
        user = new_user.check_username(data['username'].lower())
        if user:
            return {'message': 'Username already exists',
                    'status': 400}, 400

        mail = new_user.check_email(data['email'])
        if mail:
            return {'message': 'Email already exists',
                    'status': 400}, 400

        new_user.register_user()
        del data['password']
        return {'message': 'User successfuly  added',
                'data': data,
                'status': 201}, 201


class Login(Resource, User):
    @v2_user.expect(user_login)
    def post(self):
        'logs in a user'
        data = v2_user.payload
        schema = LoginSchema()
        schema_data = schema.load(data)
        errors = schema_data.errors
        error_types = ['username', 'password']

        for e in error_types:
            if e in errors.keys():
                return {'message': 'Invalid or missing {}'.format(e),
                        'status': 400}, 400

        current_user = User.check_username(data['username'].lower())

        if not current_user:
            return {'message': 'Username does not exist',
                    'status': 400}, 400

        if not check_password_hash(current_user[9], data['password'].strip()):
            return {'message': f'Invalid username or password',
                    'status': 400}, 400

        access_token = create_access_token(identity=data['username'])
        is_admin = current_user[8]
        return {'message': 'Logged in as {}'.format(data['username']),
                'access_token': access_token,
                'status': 200,
                'is_admin': is_admin}, 200


class Logout(Resource):
    """logout users"""
    @v2_user.doc(security="apikey")
    @jwt_required
    def post(self):
        """Log out a given user by blacklisting user's token"""
        jti = get_raw_jwt()["jti"]
        blacklist.add(jti)
        return ({'message': "Successfully logged out",
                 'status': 200}), 200
