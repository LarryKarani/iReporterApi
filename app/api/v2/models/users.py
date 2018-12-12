"""This module contains the user model that adds a new user to the db"""
import datetime
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import generate_password_hash
from functools import wraps

#local imports
from .db import Db


class User():
    def __init__(self, firstname, lastname , othername, email, phoneNumber, username, password, isAdmin=False):
        self.registered = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.isAdmin = isAdmin
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = generate_password_hash(password.strip())
       

    def __repr__(self):
        return {
            'username':self.username,
            'isAdmin':self.isAdmin,
            'email': self.email
        }
    @classmethod
    def check_username(cls, username):
        """checks if username already exists"""
        sql = "SELECT * FROM users WHERE users.username=\'%s\' "%(username)
        curr = Db().cur
        curr.execute(sql)
        output =curr.fetchone()
        return output
    @classmethod
    def check_email(cls, email):
        """checks if email is already in use"""
        sql = "SELECT * FROM users WHERE users.email=\'%s\' "%(email)
        curr = Db().cur
        curr.execute(sql)
        output = curr.fetchone()
        return output

    def register_user(self):
        """Registers a new user into the database"""
        sql = "INSERT INTO users (firstname,\
                                  lastname,\
                                  othername,\
                                  email,\
                                  phoneNumber,\
                                  username,\
                                  registered,\
                                  isAdmin,\
                                  password)\
                            VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"%(
                                self.firstname,
                                self.lastname,
                                self.othername,
                                self.email,
                                self.phoneNumber,
                                self.username,
                                self.registered,
                                self.isAdmin,
                                self.password  
                            )
        conn = Db().con
        curr = conn.cursor()
        curr.execute(sql)
        print("addedd")
        conn.commit()
    
    @staticmethod
    def get_a_user(id):
        sql = f"SELECT * FROM users WHERE users.id={id}"
        curr = Db().cur
        curr.execute(sql)
        output = curr.fetchone()
        return output
    @classmethod
    def promote_user(cls,username):
        sql="UPDATE users SET isAdmin=True WHERE users.username=%s"
        conn = Db().con
        curr = conn.cursor()
        curr.execute(sql,(username,))
        conn.commit()
    @classmethod
    def create_admin(cls):
        try:
            admin = User('ben','larry','kkk','kara@g.com','0701043047', 'kkk','lll')
            admin.register_user()
            admin.promote_user('kkk')
        except:
            return 'user already exists'

  
def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user = User.check_username(get_jwt_identity())
        if user[8] != True:
            return {'message': 'Only admim can change status'}, 401
        return f(*args, **kwargs)
    return wrapper
