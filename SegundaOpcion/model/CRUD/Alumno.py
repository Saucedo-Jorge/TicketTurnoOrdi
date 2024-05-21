from model.bd import Alumno
from model import bd
from sqlalchemy import func

def create(curp, nombre, paterno, materno, telefono, celular, correo, municipio_id, grado_id, session=None):
    if session is None:
        session = bd.get_session()
    alumno = Alumno(CURP=curp, Nombre=nombre, Paterno=paterno, Materno=materno, Telefono=telefono,
                    Celular=celular, Correo=correo, MunicipioID=municipio_id, GradoID=grado_id)
    session.add(alumno)
    session.commit()
    return alumno

def read(curp):
    session = bd.get_session()
    alumno = session.query(Alumno).filter(Alumno.CURP == curp).first()
    if alumno:
        return alumno
    else:
        return None

def list():
    session = bd.get_session()
    alumnos = session.query(Alumno).all()
    return alumnos

def update(alumno, nombre=None, paterno=None, materno=None, telefono=None, celular=None, correo=None,
           municipio_id=None, grado_id=None):
    session = bd.get_session()
    alumno = session.query(Alumno).filter(Alumno.CURP == alumno.CURP).first()
    if nombre is not None:
        alumno.Nombre = nombre
    if paterno is not None:
        alumno.Paterno = paterno
    if materno is not None:
        alumno.Materno = materno
    if telefono is not None:
        alumno.Telefono = telefono
    if celular is not None:
        alumno.Celular = celular
    if correo is not None:
        alumno.Correo = correo
    if municipio_id is not None:
        alumno.MunicipioID = municipio_id
    if grado_id is not None:
        alumno.GradoID = grado_id
    session.commit()

def delete(alumno):
    session = bd.get_session()
    alumno = session.query(Alumno).filter(Alumno.CURP == alumno.CURP).first()
    session.delete(alumno)
    session.commit()

session = bd.get_session()
if session.query(func.count(Alumno.CURP)).scalar() == 0:
    create('ABCD123456HIJKLMN0', 'Alumno', 'De', 'Prueba', '1234567890', '844234567', 'alumno@correo.com', 1, 1)