from .entities.DetalleCita import DetalleCita

class ModelDetalleCita:
    
    
    @staticmethod
    def get_data(db, datacita):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()            
            
            sql =  """select c.TELEFONOQR, c.CORREOQR, r.asuntotratar from realiza r join citas c 
                        ON r.IDCITA = c.IDCITA where r.NUMTURNO = '{}' AND r.CURP = '{}';""".format(datacita.curp, datacita.numturno)
            cursor.execute(sql)
            result = cursor.fetchone()
            print('este es print del model',result)
                
            return result
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_id(self, db, det):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = "select idcita from realiza where curp='{} AND NumTurn='{};".format(det.curp, det.numturno)
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            return result
        except Exception as ex:
            raise Exception(ex)



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
            connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(self, db, detallecita):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = "DELETE FROM realiza WHERE IDCITA = '{}'".format(detallecita.idcita,detallecita.curp )
            cursor.execute(sql)
            connection.commit()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def numturn(self, db, curp):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
                
            sql = """SELECT 
    m.NOMBREMUNICIPIO
FROM 
    alumnos a
JOIN 
    municipio m ON a.CODMUNICIPIO = m.CODMUNICIPIO
WHERE 
    a.CURP = '{}';""".format(curp)
            cursor.execute(sql)
            nommun = cursor.fetchone()
            muni = nommun[0]
            print(muni)
            
            sql = """SELECT 
    m.NOMBREMUNICIPIO,
    COUNT(r.IDCITA) AS NUM_CITAS
FROM 
    municipio m
JOIN 
    alumnos a ON m.CODMUNICIPIO = a.CODMUNICIPIO
JOIN 
    realiza r ON a.CURP = r.CURP
JOIN 
    citas c ON r.IDCITA = c.IDCITA
WHERE 
    m.NOMBREMUNICIPIO = '{}'
GROUP BY 
    m.NOMBREMUNICIPIO;""".format(muni)
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result[1])
            
            
            
            return (result[1]+1)
        
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, detallecita):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            sql = """UPDATE realiza SET ASUNTOTRATAR = '{}' 
                     WHERE IDCITA = '{}' AND curp = '{}' """.format(
                        detallecita.idcita, detallecita.curp)
            cursor.execute(sql)
            connection.commit()
        except Exception as ex:
            raise Exception(ex)
