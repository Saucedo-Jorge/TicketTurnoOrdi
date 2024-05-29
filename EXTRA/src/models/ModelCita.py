from .entities.Cita import Cita

class ModelCita:

    @classmethod
    def get_all(self, db):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = "SELECT IDCITA, QUIENR, TELEFONOQR, CORREOQR, STATUS FROM citas"
            cursor.execute(sql)
            result = cursor.fetchall()
            citas = []
            for row in result:
                citas.append(Cita(row[0], row[1], row[2], row[3], row[4]))
            return citas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_id(self, db):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = "select * from citas order by IDCITA desc limit 1;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add(self, db, cita):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            
            sql = """INSERT INTO citas ( QUIENR, TELEFONOQR, CORREOQR, STATUS) 
                     VALUES ( '{}', '{}', '{}', 'Pendiente' )""".format(
                         cita.quienr, cita.telefonoqr, cita.correoqr)
            cursor.execute(sql)
            connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self, db, idcita):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = "DELETE FROM citas WHERE IDCITA = '{}'".format(idcita)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, cita):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = """UPDATE citas SET QUIENR = '{}', TELEFONOQR = '{}', CORREOQR = '{}', STATUS = '{}' 
                     WHERE IDCITA = '{}'""".format(
                        cita.quienr, cita.telefonoqr, cita.correoqr, cita.status, cita.idcita)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
