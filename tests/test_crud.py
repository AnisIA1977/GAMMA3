import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from gamma3_system.database import Base
from gamma3_system import crud, schemas, models

# Use an in-memory SQLite database for testing CRUD
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
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

def test_create_material_class_success(db_session):
    # Setup test data
    class_in = schemas.MaterialClassCreate(code="1", designation="Matériel Mécanique")

    # Execute the function to test
    created_class = crud.create_material_class(db=db_session, material_class=class_in)

    # Verify the results
    assert created_class.id is not None
    assert created_class.code == "1"
    assert created_class.designation == "Matériel Mécanique"

    # Verify it was actually saved in the database
    db_obj = db_session.query(models.MaterialClass).filter(models.MaterialClass.id == created_class.id).first()
    assert db_obj is not None
    assert db_obj.code == "1"

def test_create_material_class_duplicate_code(db_session):
    # Setup first class
    class_in_1 = schemas.MaterialClassCreate(code="2", designation="Électricité")
    crud.create_material_class(db=db_session, material_class=class_in_1)

    # Try to create another class with the same code
    class_in_2 = schemas.MaterialClassCreate(code="2", designation="Duplicate Code")

    # Verify it raises an IntegrityError
    with pytest.raises(IntegrityError):
        crud.create_material_class(db=db_session, material_class=class_in_2)
