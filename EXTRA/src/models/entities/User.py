from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self,idusers, username, password, fullname="")->None:
        self.idusers = idusers
        self.username = username
        self.password = password
        self.fullname = fullname
        
    @classmethod
    def check_password(self,  password_hash, password):
        return check_password_hash(password_hash, password)
    