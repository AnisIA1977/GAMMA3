from sqlalchemy.orm import Session
from . import models, schemas

# --- Material Class ---
def get_material_class(db: Session, class_id: int):
    return db.query(models.MaterialClass).filter(models.MaterialClass.id == class_id).first()

def get_material_classes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MaterialClass).offset(skip).limit(limit).all()

def create_material_class(db: Session, material_class: schemas.MaterialClassCreate):
    db_obj = models.MaterialClass(code=material_class.code, designation=material_class.designation)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# --- SubClass ---
def create_subclass(db: Session, subclass: schemas.SubClassCreate, class_id: int):
    db_obj = models.SubClass(**subclass.dict(), material_class_id=class_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# --- Constructor ---
def get_constructors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Constructor).offset(skip).limit(limit).all()

def create_constructor(db: Session, constructor: schemas.ConstructorCreate):
    db_obj = models.Constructor(code=constructor.code, designation=constructor.designation)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# --- Series ---
def create_series(db: Session, series: schemas.SeriesCreate, constructor_id: int):
    db_obj = models.Series(**series.dict(), constructor_id=constructor_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# --- Article ---
def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

def create_article(db: Session, article: schemas.ArticleCreate):
    db_obj = models.Article(**article.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_article_stock(db: Session, article_id: int, quantity: int):
    db_obj = db.query(models.Article).filter(models.Article.id == article_id).first()
    if db_obj:
        db_obj.stock_quantity = quantity
        db.commit()
        db.refresh(db_obj)
    return db_obj
