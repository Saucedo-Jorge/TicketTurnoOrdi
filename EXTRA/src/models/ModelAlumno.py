from .entities.Alumno import Alumno

class ModelAlumno:

    @classmethod
    def get_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT CURP, CODMUNICIPIO, NOMBRE_S_ALUM, PATERNOALUM, MATERNOALUM, NIVELCURSA FROM alumnos"
            cursor.execute(sql)
            result = cursor.fetchall()
            alumnos = []
            for row in result:
                alumnos.append(Alumno(row[0], row[1], row[2], row[3], row[4], row[5]))
            return alumnos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add(self, db, alumno):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO alumnos (CURP, CODMUNICIPIO, NOMBRE_S_ALUM, PATERNOALUM, MATERNOALUM, NIVELCURSA) 
                     VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
                        alumno.curp, alumno.codmunicipio, alumno.nombre_s_alum, 
                        alumno.paternoalum, alumno.maternoalum, alumno.nivelcursa)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self, db, curp):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM alumnos WHERE CURP = '{}'".format(curp)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, alumno):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE alumnos SET CODMUNICIPIO = '{}', NOMBRE_S_ALUM = '{}', 
                     PATERNOALUM = '{}', MATERNOALUM = '{}', NIVELCURSA = '{}' 
                     WHERE CURP = '{}'""".format(
                        alumno.codmunicipio, alumno.nombre_s_alum, alumno.paternoalum, 
                        alumno.maternoalum, alumno.nivelcursa, alumno.curp)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
