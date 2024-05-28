from .entities.Cita import Cita

class ModelCita:

    @classmethod
    def get_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, fecha, descripcion FROM cita"
            cursor.execute(sql)
            result = cursor.fetchall()
            citas = []
            for row in result:
                citas.append(Cita(row[0], row[1], row[2]))
            return citas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add(self, db, cita):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO cita (fecha, descripcion) 
                     VALUES ('{}', '{}')""".format(cita.fecha, cita.descripcion)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM cita WHERE id = {}".format(id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, cita):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE cita SET fecha = '{}', descripcion = '{}' 
                     WHERE id = {}""".format(cita.fecha, cita.descripcion, cita.id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
