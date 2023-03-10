from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'OK'}


def test_create_task():
    response = client.post("/tasks", json={"title": "test", "description": "test", 'date': '2021-01-01'})
    assert response.status_code == 200
    assert type(response.json()['id']) is int


def test_read_tasks():
    client.post("/tasks", json={"title": "test", "description": "test", 'date': '2021-01-01'})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_delete_task():
    response = client.post("/tasks", json={"title": "test", "description": "test", 'date': '2021-01-01'})
    task_id = response.json()['id']
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert str(response.json()['id']) == str(task_id)
    response = client.get("/tasks")
    assert len(response.json()) == 2
