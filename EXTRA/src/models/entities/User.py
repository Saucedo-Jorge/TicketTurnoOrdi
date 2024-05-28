from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self, username, password, fullname="")->None:
        self.username = username
        self.password = password
        self.fullname = fullname
        
    @classmethod
    def check_password(self, password, password_hash):
        return check_password_hash(password_hash, password)
    
print("es:",generate_password_hash('123456'))