from model.bd import Usuario
from model import bd
from sqlalchemy import func

def create(usuario_name, contraseña, admin=False, session=None):
    if session is None:
        session = bd.get_session()
    usuario = Usuario(Usuario=usuario_name, Contrasena=contraseña, Rol='Admin' if admin else 'Usuario')
    session.add(usuario)
    session.commit()
    return usuario

def read(usuario_name):
    session = bd.get_session()
    usuario = session.query(Usuario).filter(Usuario.Usuario == usuario_name).first()
    if usuario:
        return usuario
    else:
        return None

def list():
    session = bd.get_session()
    usuarios = session.query(Usuario).all()
    return usuarios

def update(usuario, contraseña=None):
    session = bd.get_session()
    usuario = session.query(Usuario).filter(Usuario.Usuario == usuario.Usuario).first()
    if contraseña is not None:
        usuario.Contrasena = contraseña
    session.commit()

def delete(usuario):
    session = bd.get_session()
    usuario = session.query(Usuario).filter(Usuario.Usuario == usuario.Usuario).first()
    session.delete(usuario)
    session.commit()

session = bd.get_session()
if session.query(func.count(Usuario.Usuario)).scalar() == 0:
    create('Admin', 'Admin', True)
    create('Usuario', 'Usuario123', False)