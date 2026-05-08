from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from gamma3_system.main import app, get_db
from gamma3_system.database import Base
from gamma3_system import models

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    # Create tables
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    # Drop tables
    Base.metadata.drop_all(bind=engine)

def test_nomenclature_generation(client):
    """
    Verifies the specific example from the documentation:
    Class 1 (Meca) -> SubClass 00 (Diesel)
    Constructor MT (MTU) -> Series 01 (20V538)
    Item 0001 (Joint)
    Expected: 100MT010001
    """
    # 1. Create Class "1"
    res = client.post("/classes/", json={"code": "1", "designation": "Matériel Mécanique"})
    assert res.status_code == 200
    class_id = res.json()["id"]

    # 2. Create SubClass "00"
    res = client.post(f"/classes/{class_id}/subclasses/", json={"code": "00", "designation": "Moteurs Diesels"})
    assert res.status_code == 200
    subclass_id = res.json()["id"]

    # 3. Create Constructor "MT"
    res = client.post("/constructors/", json={"code": "MT", "designation": "MTU"})
    assert res.status_code == 200
    constructor_id = res.json()["id"]

    # 4. Create Series "01"
    res = client.post(f"/constructors/{constructor_id}/series/", json={"code": "01", "designation": "20 V 538"})
    assert res.status_code == 200
    series_id = res.json()["id"]

    # 5. Create Article "0001"
    article_data = {
        "item_code": "0001",
        "designation": "Joint",
        "location": "Casier X",
        "stock_quantity": 10,
        "subclass_id": subclass_id,
        "series_id": series_id
    }
    res = client.post("/articles/", json=article_data)
    assert res.status_code == 200
    data = res.json()

    # 6. Verify Nomenclature
    assert data["nomenclature"] == "100MT010001"
    print(f"\nTested Nomenclature: {data['nomenclature']} (Expected: 100MT010001)")

def test_article_listing(client):
    res = client.get("/articles/")
    assert res.status_code == 200
    assert len(res.json()) > 0

def test_update_article_stock(client):
    """
    Verifies the crud.update_article_stock function.
    Why it is necessary: The update_article_stock function in crud.py was previously untested.
    This test ensures that the stock quantity is correctly updated when valid IDs are provided,
    and that the system handles invalid IDs gracefully.
    Impact: Increases test coverage and reliability of the inventory management logic.
    """
    from gamma3_system import crud

    # 1. Setup - Create necessary parent entities to create an article
    res = client.post("/classes/", json={"code": "2", "designation": "Test Class"})
    class_id = res.json()["id"]

    res = client.post(f"/classes/{class_id}/subclasses/", json={"code": "99", "designation": "Test SubClass"})
    subclass_id = res.json()["id"]

    res = client.post("/constructors/", json={"code": "TT", "designation": "Test Constructor"})
    constructor_id = res.json()["id"]

    res = client.post(f"/constructors/{constructor_id}/series/", json={"code": "99", "designation": "Test Series"})
    series_id = res.json()["id"]

    # 2. Setup - Create the Article with initial stock 10
    article_data = {
        "item_code": "0002",
        "designation": "Test Item",
        "location": "Test Location",
        "stock_quantity": 10,
        "subclass_id": subclass_id,
        "series_id": series_id
    }
    res = client.post("/articles/", json=article_data)
    assert res.status_code == 200
    article_id = res.json()["id"]

    # 3. Execution & Verification - Happy Path
    db = TestingSessionLocal()
    try:
        # Update stock to 25
        updated_article = crud.update_article_stock(db, article_id=article_id, quantity=25)

        # Verify the returned object
        assert updated_article is not None
        assert updated_article.id == article_id
        assert updated_article.stock_quantity == 25

        # Verify it was actually saved to the database
        db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
        assert db_article.stock_quantity == 25

        # 4. Execution & Verification - Edge Case (Non-existent article)
        non_existent_id = 9999
        null_article = crud.update_article_stock(db, article_id=non_existent_id, quantity=50)
        assert null_article is None
    finally:
        db.close()
