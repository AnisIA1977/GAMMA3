from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from gamma3_system.main import app, get_db
from gamma3_system.database import Base

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
