from .entities.User import User

class ModelUser:

    @classmethod
    def login(cls, db, user):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user 
                     WHERE username = %s"""
            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()
            if row is not None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(cls, db, id):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = "SELECT id, username, fullname FROM user WHERE id = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row is not None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
