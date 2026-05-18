from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class MaterialClass(Base):
    __tablename__ = "material_classes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    designation = Column(String)

    subclasses = relationship("SubClass", back_populates="material_class")


class SubClass(Base):
    __tablename__ = "subclasses"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    designation = Column(String)
    material_class_id = Column(Integer, ForeignKey("material_classes.id"))

    material_class = relationship("MaterialClass", back_populates="subclasses")
    articles = relationship("Article", back_populates="subclass")


class Constructor(Base):
    __tablename__ = "constructors"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    designation = Column(String)

    series = relationship("Series", back_populates="constructor")


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    designation = Column(String)
    constructor_id = Column(Integer, ForeignKey("constructors.id"))

    constructor = relationship("Constructor", back_populates="series")
    articles = relationship("Article", back_populates="series")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)

    # Identification
    item_code = Column(String, index=True)
    designation = Column(String)

    subclass_id = Column(Integer, ForeignKey("subclasses.id"))
    series_id = Column(Integer, ForeignKey("series.id"))

    subclass = relationship("SubClass", back_populates="articles")
    series = relationship("Series", back_populates="articles")

    # Gestion
    unit_of_measure = Column(String, default="U")
    supply_mode = Column(String, default="ACHAT")
    unit_price = Column(Float, default=0.0)

    # Stockage & Planification
    location = Column(String)
    stock_quantity = Column(Integer, default=0)

    # Planning Inputs
    lead_time_days = Column(Integer, default=0) # Délai d'approvisionnement (d)
    monthly_consumption = Column(Float, default=0.0) # Consommation Moyenne Mensuelle (CMM)

    # Thresholds (Calculated)
    alert_threshold = Column(Integer, default=0) # Sa = CMM * (d/30)
    security_threshold = Column(Integer, default=0) # Ss = Sa / 3
    minimum_threshold = Column(Integer, default=0) # Smin

    @property
    def nomenclature(self):
        if self.subclass and self.series:
            return f"{self.subclass.material_class.code}{self.subclass.code}{self.series.constructor.code}{self.series.code}{self.item_code}"
        return None
