import pytest
import mongomock
from app import app, mongo
from bson.objectid import ObjectId

@pytest.fixture
def client():
    app.config["TESTING"] = True
    
    # 1. Intercept live MongoDB connections and redirect to an in-memory mock client
    mock_client = mongomock.MongoClient()
    mongo.cx = mock_client
    mongo.db = mock_client['test_student_db']
    
    client = app.test_client()

    # 2. Setup: Clean existing workspace state and insert baseline seed dataset
    with app.app_context():
        mongo.db.students.delete_many({})
        mongo.db.students.insert_one({
            "_id": ObjectId("66fddff25f4b5f6a0a123456"),
            "name": "Test Student",
            "email": "test@student.com",
            "course": "Flask"
        })
        
    yield client

    # 3. Teardown: Clear workspace dataset (mock memory contexts drop automatically)
    with app.app_context():
        mongo.db.students.delete_many({})


def test_home_page(client):
    """Test if home page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Test Student" in response.data


def test_add_student(client):
    """Test adding a new student"""
    data = {"name": "New User", "email": "new@user.com", "course": "Python"}
    response = client.post('/add', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"New User" in response.data


def test_update_student(client):
    """Test updating a student"""
    student_id = "66fddff25f4b5f6a0a123456"
    data = {"name": "Updated Name", "email": "updated@student.com", "course": "Updated Course"}
    response = client.post(f'/update/{student_id}', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Updated Name" in response.data


def test_delete_student(client):
    """Test deleting a student"""
    with app.app_context():
        inserted = mongo.db.students.insert_one({
            "name": "Temp User",
            "email": "temp@user.com",
            "course": "Temp Course"
        })
        # FIX: Convert the BSON ObjectId into a plain string for the URL path
        student_id = str(inserted.inserted_id)

    response = client.get(f'/delete/{student_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Temp User" not in response.data
