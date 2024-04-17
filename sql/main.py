from fastapi import Depends, FastAPI, Path, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
        
@app.get("/")
def index():
    return {
        'Aplicación': 'AlumnaSys',
        'Versión': '0.0.1'
    }    
    
@app.post("/tutores/", response_model=schemas.Tutor)
def create_tutor(tutor: schemas.CrearTutor, db: Session = Depends(get_db)):
    return crud.create_tutor(db=db, tutor=tutor)

@app.get("/tutores/{id}/", response_model=schemas.Tutor)
def read_tutor(id: int, db: Session = Depends(get_db)):
    return crud.get_tutor(db, id)

@app.get("/tutores/", response_model=list[schemas.Tutor])
def read_tutores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tutores = crud.get_tutores(db, skip=skip, limit=limit)
    return tutores

@app.put("/tutores/{id}/", response_model=schemas.Tutor)
def update_tutor(tutor: schemas.ModificarTutor, id: int = Path(..., alias="id"), db: Session = Depends(get_db)):
    return crud.update_tutor(db=db, tutor=tutor, id=id)

@app.delete("/tutores/{id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_tutor(id: int = Path(..., alias="id"), db: Session = Depends(get_db)):
    tutores = crud.delete_tutor(db=db, id=id)
    return tutores