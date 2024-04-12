from fastapi import Depends, FastAPI, Path, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
        
@app.post("/tutores/", response_model=schemas.Tutor)
def create_tutor(tutor: schemas.CrearTutor, db: Session = Depends(get_db)):
    return crud.create_tutor(db=db, tutor=tutor)