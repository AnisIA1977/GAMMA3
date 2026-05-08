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
