from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class MaterialClass(Base):
    __tablename__ = "material_classes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)  # e.g., "1"
    designation = Column(String)

    subclasses = relationship("SubClass", back_populates="material_class")


class SubClass(Base):
    __tablename__ = "subclasses"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)  # e.g., "00"
    designation = Column(String)
    material_class_id = Column(Integer, ForeignKey("material_classes.id"))

    material_class = relationship("MaterialClass", back_populates="subclasses")
    articles = relationship("Article", back_populates="subclass")


class Constructor(Base):
    __tablename__ = "constructors"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)  # e.g., "MT"
    designation = Column(String)

    series = relationship("Series", back_populates="constructor")


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)  # e.g., "01"
    designation = Column(String)
    constructor_id = Column(Integer, ForeignKey("constructors.id"))

    constructor = relationship("Constructor", back_populates="series")
    articles = relationship("Article", back_populates="series")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    item_code = Column(String, index=True)  # e.g., "0001"
    designation = Column(String)
    location = Column(String) # e.g. "Casier X"
    stock_quantity = Column(Integer, default=0)

    subclass_id = Column(Integer, ForeignKey("subclasses.id"))
    series_id = Column(Integer, ForeignKey("series.id"))

    subclass = relationship("SubClass", back_populates="articles")
    series = relationship("Series", back_populates="articles")

    @property
    def nomenclature(self):
        # 100MT010001
        # Class Code (1) + SubClass Code (00) + Constructor Code (MT) + Series Code (01) + Item Code (0001)
        if self.subclass and self.series:
            return f"{self.subclass.material_class.code}{self.subclass.code}{self.series.constructor.code}{self.series.code}{self.item_code}"
        return None
