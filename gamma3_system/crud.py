from sqlalchemy.orm import Session
from . import models, schemas
import math

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
    db_obj = models.SubClass(**subclass.model_dump(), material_class_id=class_id)
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
    db_obj = models.Series(**series.model_dump(), constructor_id=constructor_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# --- Article ---
def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

def create_article(db: Session, article: schemas.ArticleCreate):
    data = article.model_dump()

    # --- Planning Logic (Phase 2) ---
    # Inputs: CMM (monthly_consumption), Lead Time (lead_time_days)
    # Rules:
    # 1. Sa = CMM * (Lead Time / 30)
    # 2. Ss = 1/3 * Sa

    cmm = data.get('monthly_consumption', 0)
    lead_time = data.get('lead_time_days', 0)

    # Auto-Calculate Sa if not manually overridden (or if 0)
    if data.get('alert_threshold', 0) == 0 and cmm > 0 and lead_time > 0:
        # Sa = CMM * (d / 30)
        # Round up to nearest integer for safety
        sa_calc = (cmm * lead_time) / 30.0
        data['alert_threshold'] = math.ceil(sa_calc)

    # Auto-Calculate Ss if not manually overridden (or if 0)
    sa = data.get('alert_threshold', 0)
    if data.get('security_threshold', 0) == 0 and sa > 0:
        # Ss = 1/3 * Sa
        data['security_threshold'] = math.ceil(sa / 3.0)

    db_obj = models.Article(**data)
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
