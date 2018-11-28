import datetime
db =[]

class Users():
    def __init__(self):
        self.db = db
        self.isAdmin = False
        self.registered = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



    def create_user(self, firstname, lastname, othername, email, phoneNumber, username):
        data = {}

        data['id'] = len(self.db)+1
        data['firstname'] = firstname
        data['lastname'] = lastname
        data['othername'] = othername
        data['email'] = email
        data['phoneNumber'] = phoneNumber
        data['username'] =  username
        data['registered'] = self.registered

    def get_user(self, id):
        output = [user for user in self.db if user['id']== id]
        if len(output) == 0:
            return False
        
        return output[0]

    def get_all_users(self):
        return  self.db

    def get_username(self, username):
        output = [user for user in self.db if user['username']== username]
        if len(output) == 0:
            return False
        return output[0]

    def get_email(self, email):
        output = [user for user in self.db if user['email']== email]
        if len(output) == 0:
            return False
        return output[0]





        




