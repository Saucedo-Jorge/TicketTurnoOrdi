from .db import db

class Appointment:
    def __init__(self, municipality, number, status='pending'):
        self.municipality = municipality
        self.number = number
        self.status = status

    @staticmethod
    def create(municipality):
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM appointments WHERE municipality = %s", (municipality,))
        count = cursor.fetchone()[0] + 1
        cursor.execute("INSERT INTO appointments (municipality, number, status) VALUES (%s, %s, %s)",
                       (municipality, count, 'pending'))
        db.commit()
        return count

    @staticmethod
    def update_status(appointment_id, status):
        cursor = db.cursor()
        cursor.execute("UPDATE appointments SET status = %s WHERE id = %s", (status, appointment_id))
        db.commit()

    @staticmethod
    def delete(appointment_id):
        cursor = db.cursor()
        cursor.execute("DELETE FROM appointments WHERE id = %s", (appointment_id,))
        db.commit()

    @staticmethod
    def get_all(status=None):
        cursor = db.cursor(dictionary=True)
        if status:
            cursor.execute("SELECT * FROM appointments WHERE status = %s", (status,))
        else:
            cursor.execute("SELECT * FROM appointments")
        return cursor.fetchall()
