import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_frontpage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Enter Name" in response.data

def test_post(client):
    response = client.post('/echo_user_input', data={
        "user_input": "MyDemo", "pass_input":"test"})
    assert response.status_code == 200
    assert b"MyDemo" in response.data
    assert b"098f6bcd4621d373cade4e832627b4f6" in response.data