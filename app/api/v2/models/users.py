"""This module contains the user model that adds a new user to the db"""
import datetime
from werkzeug.security import generate_password_hash

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
        self.db_obj = Db()

    def __repr__(self):
        return {
            'username':self.username,
            'isAdmin':self.isAdmin,
            'email': self.email
        }

    def check_username(self, username):
        """checks if username already exists"""
        sql = "SELECT * FROM users WHERE users.username=\'%s\' "%(username)
        curr = Db().cur
        curr.execute(sql)
        output =curr.fetchone()
        return output

    def check_email(self, email):
        """checks if email is already in use"""
        sql = "SELECT * FROM users WHERE users.email=\'%s\' "%(email)
        curr = self.db_obj.cur
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
        conn = self.db_obj.con
        curr = conn.cursor()
        curr.execute(sql)
        print("addedd")
        conn.commit()
    
    def get_a_user(self, id):
        sql = f"SELECT * FROM users WHERE users.id={id}"
        curr = self.db_obj.cur
        curr.execute(sql)
        output = curr.fetchone()
        return output

