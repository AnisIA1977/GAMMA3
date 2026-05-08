import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from gamma3_system import crud, models, schemas
from gamma3_system.database import Base

from sqlalchemy import event
from sqlalchemy.engine import Engine

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

@event.listens_for(Engine, "connect")
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
        # Drop tables
        Base.metadata.drop_all(bind=engine)

def test_create_series_success(db_session):
    # 1. First, create a constructor
    constructor_in = schemas.ConstructorCreate(code="AB", designation="Constructor Alpha")
    constructor = crud.create_constructor(db=db_session, constructor=constructor_in)
    assert constructor.id is not None

    # 2. Create the series linking to the constructor
    series_in = schemas.SeriesCreate(code="01", designation="Series One")
    series = crud.create_series(db=db_session, series=series_in, constructor_id=constructor.id)

    # 3. Assertions
    assert series.id is not None
    assert series.code == "01"
    assert series.designation == "Series One"
    assert series.constructor_id == constructor.id

def test_create_series_invalid_constructor(db_session):
    # Create a series pointing to a non-existent constructor ID
    series_in = schemas.SeriesCreate(code="02", designation="Series Two")

    with pytest.raises(IntegrityError):
        # We expect this to fail due to foreign key constraint
        crud.create_series(db=db_session, series=series_in, constructor_id=999)
