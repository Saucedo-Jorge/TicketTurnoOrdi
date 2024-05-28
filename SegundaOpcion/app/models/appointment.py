from .db import db

class Appointment:
    def __init__(self, idappointments, user_id, date, time, description):
        self.idappointments = idappointments
        self.user_id = user_id
        self.date = date
        self.time = time
        self.description = description

    @staticmethod
    def create(user_id, date, time, description):
        cursor = db.cursor()
        cursor.execute("INSERT INTO appointments (user_id, date, time, description) VALUES (%s, %s, %s, %s)",
                       (user_id, date, time, description))
        db.commit()
        cursor.close()

    @staticmethod
    def get_by_user_id(user_id):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM appointments WHERE user_id = %s", (user_id,))
        appointments = cursor.fetchall()
        cursor.close()
        return appointments

    @staticmethod
    def delete(appointment_id):
        cursor = db.cursor()
        cursor.execute("DELETE FROM appointments WHERE idappointments = %s", (appointment_id,))
        db.commit()
        cursor.close()
