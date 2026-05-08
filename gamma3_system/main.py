from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="GAMMA3.0 System")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Material Classes & SubClasses ---
@app.post("/classes/", response_model=schemas.MaterialClass)
def create_material_class(material_class: schemas.MaterialClassCreate, db: Session = Depends(get_db)):
    return crud.create_material_class(db=db, material_class=material_class)

@app.get("/classes/", response_model=List[schemas.MaterialClassWithSubclasses])
def read_material_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_material_classes(db, skip=skip, limit=limit)

@app.post("/classes/{class_id}/subclasses/", response_model=schemas.SubClass)
def create_subclass(class_id: int, subclass: schemas.SubClassCreate, db: Session = Depends(get_db)):
    db_class = crud.get_material_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="Material Class not found")
    return crud.create_subclass(db=db, subclass=subclass, class_id=class_id)

# --- Constructors & Series ---
@app.post("/constructors/", response_model=schemas.Constructor)
def create_constructor(constructor: schemas.ConstructorCreate, db: Session = Depends(get_db)):
    return crud.create_constructor(db=db, constructor=constructor)

@app.get("/constructors/", response_model=List[schemas.ConstructorWithSeries])
def read_constructors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_constructors(db, skip=skip, limit=limit)

@app.post("/constructors/{constructor_id}/series/", response_model=schemas.Series)
def create_series(constructor_id: int, series: schemas.SeriesCreate, db: Session = Depends(get_db)):
    return crud.create_series(db=db, series=series, constructor_id=constructor_id)

# --- Articles ---
@app.post("/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)

@app.get("/articles/", response_model=List[schemas.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_articles(db, skip=skip, limit=limit)

# --- Static Files (Frontend) ---
app.mount("/", StaticFiles(directory="gamma3_system/static", html=True), name="static")
