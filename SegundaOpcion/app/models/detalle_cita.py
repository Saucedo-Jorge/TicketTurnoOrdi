from .db import db

class DetalleCita:
    def __init__(self, cita_id, descripcion):
        self.cita_id = cita_id
        self.descripcion = descripcion

    @staticmethod
    def create(cita_id, descripcion):
        cursor = db.cursor()
        cursor.execute("INSERT INTO DetalleCita (cita_id, descripcion) VALUES (%s, %s)", (cita_id, descripcion))
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_cita_id(cita_id):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM DetalleCita WHERE cita_id = %s", (cita_id,))
        return cursor.fetchall()
