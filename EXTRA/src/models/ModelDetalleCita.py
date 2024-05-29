from .entities.DetalleCita import DetalleCita

class ModelDetalleCita:

    @classmethod
    def get_all(self, db):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = "SELECT IDCITA, CURP, NUMTURNO,ASUNTOTRATAR FROM realiza"
            cursor.execute(sql)
            result = cursor.fetchall()
            detalles = []
            for row in result:
                detalles.append(DetalleCita(row[0], row[1]))
            return detalles
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add(self, db, detallecita):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = """INSERT INTO realiza (IDCITA, CURP, NUMTURNO,ASUNTOTRATAR) 
                     VALUES ('{}', '{}','{}', '{}')""".format(
                        detallecita.idcita, detallecita.curp, detallecita.numturno, detallecita.asuntotratar)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self, db, codmunicipio):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM municipio WHERE codmunicipio = '{}'".format(codmunicipio)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, municipio):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE municipio SET nombremunicipio = '{}' 
                     WHERE codmunicipio = '{}'""".format(
                        municipio.nombremunicipio, municipio.codmunicipio)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
