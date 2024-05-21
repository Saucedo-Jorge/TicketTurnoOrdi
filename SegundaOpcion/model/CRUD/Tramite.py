from model.bd import Tramite
from model import bd
from sqlalchemy import func

def create(municipio_id, nombre_realizador, descripcion, estatus, alumno_curp, asunto_id, session=None):
    if session is None:
        session = bd.get_session()
    print(municipio_id, '\n\n\n\n\n')
    numero_turno = session.query(func.coalesce(func.max(Tramite.NumeroTurno), 0) + 1).filter(Tramite.Municipio == int(municipio_id)).scalar()
    tramite = Tramite(NumeroTurno=numero_turno, Municipio=municipio_id, NombreRealizador=nombre_realizador,
                      Descripcion=descripcion, Estatus=estatus, AlumnoCURP=alumno_curp, AsuntoID=asunto_id)
    session.add(tramite)
    session.commit()
    return tramite

def read(numero_turno, curp):
    session = bd.get_session()
    tramite = session.query(Tramite).filter(Tramite.NumeroTurno == numero_turno).filter(Tramite.AlumnoCURP == curp).first()
    return tramite

def read_municipio(numero_turno, municipio):
    session = bd.get_session()
    tramite = session.query(Tramite).filter(Tramite.NumeroTurno == numero_turno).filter(Tramite.Municipio == municipio).first()
    if tramite:
        return tramite
    else:
        return None

def list():
    session = bd.get_session()
    tramites = session.query(Tramite).all()
    return tramites

def update(tramite, municipio_id=None, nombre_realizador=None, descripcion=None, estatus=None, alumno_curp=None,
           asunto_id=None):
    session = bd.get_session()
    tramite = session.query(Tramite).filter(Tramite.NumeroTurno == tramite.NumeroTurno).first()
    if municipio_id is not None:
        tramite.Municipio = municipio_id
    if nombre_realizador is not None:
        tramite.NombreRealizador = nombre_realizador
    if descripcion is not None:
        tramite.Descripcion = descripcion
    if estatus is not None:
        tramite.Estatus = estatus
    if alumno_curp is not None:
        tramite.AlumnoCURP = alumno_curp
    if asunto_id is not None:
        tramite.AsuntoID = asunto_id
    session.commit()

def delete(tramite):
    session = bd.get_session()
    tramite = session.query(Tramite).filter(Tramite.NumeroTurno == tramite.NumeroTurno).first()
    session.delete(tramite)
    session.commit()