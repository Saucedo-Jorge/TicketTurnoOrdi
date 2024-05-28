from .entities.Alumno import Alumno

class ModelAlumno:

    @classmethod
    def get_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, nombre, apellido FROM alumno"
            cursor.execute(sql)
            result = cursor.fetchall()
            alumnos = []
            for row in result:
                alumnos.append(Alumno(row[0], row[1], row[2]))
            return alumnos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add(self, db, alumno):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO alumno (nombre, apellido) 
                     VALUES ('{}', '{}')""".format(alumno.nombre, alumno.apellido)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM alumno WHERE id = {}".format(id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, alumno):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE alumno SET nombre = '{}', apellido = '{}' 
                     WHERE id = {}""".format(alumno.nombre, alumno.apellido, alumno.id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
