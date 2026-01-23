from pydantic import BaseModel
from typing import List, Optional

# --- Base Schemas ---

class MaterialClassBase(BaseModel):
    code: str
    designation: str

class SubClassBase(BaseModel):
    code: str
    designation: str

class ConstructorBase(BaseModel):
    code: str
    designation: str

class SeriesBase(BaseModel):
    code: str
    designation: str

# --- Create Schemas ---

class MaterialClassCreate(MaterialClassBase):
    pass

class SubClassCreate(SubClassBase):
    pass

class ConstructorCreate(ConstructorBase):
    pass

class SeriesCreate(SeriesBase):
    pass

# --- Response Schemas (Simple/Nested) ---

class MaterialClass(MaterialClassBase):
    id: int
    class Config:
        from_attributes = True

class SubClass(SubClassBase):
    id: int
    material_class_id: int
    material_class: MaterialClass
    class Config:
        from_attributes = True

class Constructor(ConstructorBase):
    id: int
    class Config:
        from_attributes = True

class Series(SeriesBase):
    id: int
    constructor_id: int
    constructor: Constructor
    class Config:
        from_attributes = True

# --- Hierarchical Response Schemas (for listing trees) ---

class SubClassForTree(SubClassBase):
    id: int
    material_class_id: int
    class Config:
        from_attributes = True

class MaterialClassWithSubclasses(MaterialClass):
    subclasses: List[SubClassForTree] = []

class SeriesForTree(SeriesBase):
    id: int
    constructor_id: int
    class Config:
        from_attributes = True

class ConstructorWithSeries(Constructor):
    series: List[SeriesForTree] = []

# --- Article Schemas ---

class ArticleBase(BaseModel):
    item_code: str
    designation: str
    location: Optional[str] = None
    stock_quantity: int = 0

    # FSA Fields
    unit_of_measure: str = "U"
    supply_mode: str = "ACHAT"
    unit_price: float = 0.0

    # Planning Inputs
    lead_time_days: int = 0
    monthly_consumption: float = 0.0 # CMM

    # Thresholds (Calculated or Override)
    alert_threshold: int = 0
    security_threshold: int = 0
    minimum_threshold: int = 0

class ArticleCreate(ArticleBase):
    subclass_id: int
    series_id: int

class Article(ArticleBase):
    id: int
    subclass: SubClass
    series: Series
    nomenclature: str

    class Config:
        from_attributes = True
