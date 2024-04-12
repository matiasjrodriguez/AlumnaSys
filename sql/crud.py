from sqlalchemy.orm import Session

from . import models, schemas

def get_tutor(db: Session, id: int):
    return db.query(models.Tutor).filter(models.Tutor.id == id).first()

def get_tutores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tutor).offset(skip).limit(limit).all()

def create_tutor(db: Session, tutor: schemas.CrearTutor):
    db_tutor = models.Tutor(
        apellido = tutor.apellido,
        nombre = tutor.nombre,
        fecha_nacimiento = tutor.fecha_nacimiento,
        direccion = tutor.direccion,
        localidad = tutor.localidad,
        tipo = tutor.tipo
    )
    db.add(db_tutor)
    db.commit()
    db.refresh(db_tutor)
    return db_tutor

def update_tutor(db: Session, tutor: schemas.ModificarTutor, id: int):
    db_tutor = get_tutor(db, id)
    if not db_tutor:
        raise ValueError("Tutor no encontrado")
    
    db_tutor.apellido = tutor.apellido
    db_tutor.nombre = tutor.nombre
    db_tutor.fecha_nacimiento = tutor.fecha_nacimiento
    db_tutor.direccion = tutor.direccion
    db_tutor.localidad = tutor.localidad
    db_tutor.tipo = tutor.tipo
    db.commit()
    db.refresh(db_tutor)
    return db_tutor

def delete_tutor(db: Session, id: int):
    db_tutor = db.query(models.Tutor).filter(models.Tutor.id == id).first()
    if not db_tutor:
        raise ValueError("Tutor no encontrado")
    db.delete(db_tutor)
    db.commit()
    return "Tutor eliminado"
