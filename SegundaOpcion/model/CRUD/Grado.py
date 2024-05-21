from model.bd import Grado
from model import bd
from sqlalchemy import func

def create(nombre, session=None):
    if session is None:
        session = bd.get_session()
    grado = Grado(NombreGrado=nombre)
    session.add(grado)
    session.commit()
    return grado

def read(grado_id):
    session = bd.get_session()
    grado = session.query(Grado).filter(Grado.GradoID == grado_id).first()
    if grado:
        return grado
    else:
        return None

def list():
    session = bd.get_session()
    grados = session.query(Grado).all()
    return grados

def update(grado, nombre=None):
    session = bd.get_session()
    grado = session.query(Grado).filter(Grado.GradoID == grado.GradoID).first()
    if nombre is not None:
        grado.NombreGrado = nombre
    session.commit()

def delete(grado):
    session = bd.get_session()
    grado = session.query(Grado).filter(Grado.GradoID == grado.GradoID).first()
    session.delete(grado)
    session.commit()

session = bd.get_session()
if session.query(func.count(Grado.GradoID)).scalar() == 0:
    create('1ero de secundaria')
    create('2do de secundaria')
    create('3ero de secundaria')