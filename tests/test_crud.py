import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from gamma3_system.database import Base
from gamma3_system import crud, schemas

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    # Create tables
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Drop tables after each test to ensure a clean state
        Base.metadata.drop_all(bind=engine)

def test_create_subclass_success(db_session):
    # Setup: Create a MaterialClass first
    class_in = schemas.MaterialClassCreate(code="1", designation="Matériel Mécanique")
    material_class = crud.create_material_class(db=db_session, material_class=class_in)

    # Action: Create the SubClass
    subclass_in = schemas.SubClassCreate(code="00", designation="Moteurs Diesels")
    subclass = crud.create_subclass(db=db_session, subclass=subclass_in, class_id=material_class.id)

    # Assertions
    assert subclass.id is not None
    assert subclass.code == "00"
    assert subclass.designation == "Moteurs Diesels"
    assert subclass.material_class_id == material_class.id

def test_create_subclass_invalid_class_id(db_session):
    # Action: Try to create a SubClass with a non-existent class_id
    subclass_in = schemas.SubClassCreate(code="01", designation="Invalid")

    with pytest.raises(IntegrityError):
        crud.create_subclass(db=db_session, subclass=subclass_in, class_id=999)

def test_update_article_stock(db_session):
    # Setup: Create full hierarchy
    class_in = schemas.MaterialClassCreate(code="1", designation="Matériel Mécanique")
    material_class = crud.create_material_class(db=db_session, material_class=class_in)

    subclass_in = schemas.SubClassCreate(code="00", designation="Moteurs Diesels")
    subclass = crud.create_subclass(db=db_session, subclass=subclass_in, class_id=material_class.id)

    constructor_in = schemas.ConstructorCreate(code="MT", designation="MTU")
    constructor = crud.create_constructor(db=db_session, constructor=constructor_in)

    series_in = schemas.SeriesCreate(code="01", designation="20 V 538")
    series = crud.create_series(db=db_session, series=series_in, constructor_id=constructor.id)

    article_in = schemas.ArticleCreate(
        item_code="0001",
        designation="Joint",
        subclass_id=subclass.id,
        series_id=series.id,
        stock_quantity=10
    )
    article = crud.create_article(db=db_session, article=article_in)

    # Action: Update stock
    updated_article = crud.update_article_stock(db=db_session, article_id=article.id, quantity=50)

    # Assertions
    assert updated_article is not None
    assert updated_article.id == article.id
    assert updated_article.stock_quantity == 50

    # Verify in DB (new session to be sure it's committed)
    db_article = db_session.query(crud.models.Article).filter(crud.models.Article.id == article.id).first()
    assert db_article.stock_quantity == 50

def test_update_article_stock_non_existent(db_session):
    # Action: Try to update stock for a non-existent article
    result = crud.update_article_stock(db=db_session, article_id=999, quantity=50)

    # Assertions
    assert result is None
