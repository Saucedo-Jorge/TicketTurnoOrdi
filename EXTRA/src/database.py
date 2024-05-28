from flask_mysqldb import MySQL

class Database:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.mysql = MySQL()
            if app is not None:
                cls._instance.mysql.init_app(app)
        return cls._instance

    def get_connection(self):
        return self.mysql.connection
