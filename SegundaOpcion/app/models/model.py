from app import mysql

class UsuarioModel:
    def get_usuarios(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios")
        usuarios = cur.fetchall()
        cur.close()
        return usuarios
