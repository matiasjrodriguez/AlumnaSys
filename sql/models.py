from sqlalchemy import Column, Integer, String

from .database import Base

class Tutor(Base):
    __tablename__ = "tutores"
    
    id = Column(Integer, primary_key=True)
    apellido = Column(String, index=True)
    nombre = Column(String, index=True)
    fecha_nacimiento = Column(String, index=True)
    direccion = Column(String, index=True)
    localidad = Column(String, index=True)
    tipo = Column(String, index=True)