from .db import db
import bcrypt
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def create(username, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
        db.commit()

    @staticmethod
    def authenticate(username, password):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data['password'].encode('utf-8')):
            return User(user_data['idusers'], user_data['username'], user_data['password'])
        return None

    @classmethod
    def get_user_by_username(cls, username):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return cls(user_data['idusers'], user_data['username'], user_data['password'])
        else:
            return None
