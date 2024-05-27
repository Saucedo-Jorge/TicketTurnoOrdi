import mysql.connector
from config import Config

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = mysql.connector.connect(
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                host=Config.DB_HOST,
                database=Config.DB_NAME
            )
        return cls._instance

db = Database()