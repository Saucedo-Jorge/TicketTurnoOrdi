from model.bd import Municipio
from model import bd
from sqlalchemy import func

def create(nombre, session=None):
    if session is None:
        session = bd.get_session()
    municipio = Municipio(NombreMunicipio=nombre)
    session.add(municipio)
    session.commit()
    return municipio

def read(municipio_id):
    session = bd.get_session()
    municipio = session.query(Municipio).filter(Municipio.MunicipioID == municipio_id).first()
    if municipio:
        return municipio
    else:
        return None

def list():
    session = bd.get_session()
    municipios = session.query(Municipio).all()
    return municipios

def update(municipio, nombre=None):
    session = bd.get_session()
    municipio = session.query(Municipio).filter(Municipio.MunicipioID == municipio.MunicipioID).first()
    if nombre is not None:
        municipio.NombreMunicipio = nombre
    session.commit()

def delete(municipio):
    session = bd.get_session()
    municipio = session.query(Municipio).filter(Municipio.MunicipioID == municipio.MunicipioID).first()
    session.delete(municipio)
    session.commit()

session = bd.get_session()
if session.query(func.count(Municipio.MunicipioID)).scalar() == 0:
    create('Saltillo')
    create('Arteaga')
    create('Ramos Arispe')