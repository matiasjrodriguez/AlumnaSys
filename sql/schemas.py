from pydantic import BaseModel

class BasePersona(BaseModel):
    apellido: str
    nombre: str
    fecha_nacimiento: str
    direccion: str
    localidad: str
    
class BaseTutor(BasePersona):
    tipo: str
    
class CrearTutor(BaseTutor):
    pass

class ModificarTutor(BaseTutor):
    pass
    
class EliminarTutor(BaseTutor):
    pass

class Tutor(BaseTutor):
    id: int
    
    class Config:
        orm_mode = True