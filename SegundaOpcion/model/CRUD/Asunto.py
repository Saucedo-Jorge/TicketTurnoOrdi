from model.bd import Asunto
from model import bd
from sqlalchemy import func

def create(tipo, session=None):
    if session is None:
        session = bd.get_session()
    asunto = Asunto(TipoAsunto=tipo)
    session.add(asunto)
    session.commit()
    return asunto

def read(asunto_id):
    session = bd.get_session()
    asunto = session.query(Asunto).filter(Asunto.AsuntoID == asunto_id).first()
    if asunto:
        return asunto
    else:
        return None

def list():
    session = bd.get_session()
    asuntos = session.query(Asunto).all()
    return asuntos

def update(asunto, tipo=None):
    session = bd.get_session()
    asunto = session.query(Asunto).filter(Asunto.AsuntoID == asunto.AsuntoID).first()
    if tipo is not None:
        asunto.TipoAsunto = tipo
    session.commit()

def delete(asunto):
    session = bd.get_session()
    asunto = session.query(Asunto).filter(Asunto.AsuntoID == asunto.AsuntoID).first()
    session.delete(asunto)
    session.commit()

session = bd.get_session()
if session.query(func.count(Asunto.AsuntoID)).scalar() == 0:
    create('Inscripción')
    create('Baja')
    create('Pago de Mantenimiento')