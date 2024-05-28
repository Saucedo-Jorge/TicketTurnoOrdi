from .entities.Municipio import Municipio

class ModelMunicipio:

    @classmethod
    def get_all(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, nombre FROM municipio"
            cursor.execute(sql)
            result = cursor.fetchall()
            municipios = []
            for row in result:
                municipios.append(Municipio(row[0], row[1]))
            return municipios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add(self, db, municipio):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO municipio (nombre) 
                     VALUES ('{}')""".format(municipio.nombre)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM municipio WHERE id = {}".format(id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, municipio):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE municipio SET nombre = '{}' 
                     WHERE id = {}""".format(municipio.nombre, municipio.id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
