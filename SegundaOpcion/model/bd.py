from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

#pip install sqlalchemy

# Crear el motor de la base de datos SQLite
engine = create_engine('sqlite:///ticketturno.db', echo=False)  # 'echo=True' muestra las consultas generadas

# Declaramos una clase base para nuestras definiciones de tabla
Base = declarative_base()

# Definir las clases que representan las tablas en la base de datos

class Usuario(Base):
    __tablename__ = 'usuario'

    Usuario = Column(String(50), primary_key=True)
    Contrasena = Column(String(50), nullable=False)
    Rol = Column(Enum('Admin', 'Usuario'), nullable=False)

class Grado(Base):
    __tablename__ = 'grado'

    GradoID = Column(Integer, primary_key=True, autoincrement=True)
    NombreGrado = Column(String(30), nullable=False)

class Asunto(Base):
    __tablename__ = 'asunto'

    AsuntoID = Column(Integer, primary_key=True, autoincrement=True)
    TipoAsunto = Column(String(50), nullable=False)

class Municipio(Base):
    __tablename__ = 'municipio'

    MunicipioID = Column(Integer, primary_key=True, autoincrement=True)
    NombreMunicipio = Column(String(100), nullable=False)

class Alumno(Base):
    __tablename__ = 'alumno'

    CURP = Column(String(18), primary_key=True)
    Nombre = Column(String(50), nullable=False)
    Paterno = Column(String(50), nullable=False)
    Materno = Column(String(50), nullable=False)
    Telefono = Column(String(15), nullable=False)
    Celular = Column(String(15), nullable=False)
    Correo = Column(String(100), nullable=False)
    MunicipioID = Column(Integer, ForeignKey('municipio.MunicipioID'), nullable=False)
    GradoID = Column(Integer, ForeignKey('grado.GradoID'), nullable=False)
    municipio = relationship("Municipio")
    grado = relationship("Grado")

class Tramite(Base):
    __tablename__ = 'tramite'

    NumeroTurno = Column(Integer, primary_key=True, autoincrement=False)
    Municipio = Column(Integer, ForeignKey('municipio.MunicipioID'), primary_key=True, nullable=False)
    NombreRealizador = Column(String(100), nullable=False)
    Descripcion = Column(String(200), nullable=False)
    Estatus = Column(Enum('Resuelto', 'Pendiente'), nullable=False)
    AlumnoCURP = Column(String(18), ForeignKey('alumno.CURP'), nullable=False)
    AsuntoID = Column(Integer, ForeignKey('asunto.AsuntoID'), nullable=False)
    alumno = relationship("Alumno")
    asunto = relationship("Asunto")
    municipio = relationship("Municipio")

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

session = None

def get_session():
    global session
    if session is None:
        Session = sessionmaker(bind=engine)
        session = Session()
    return session