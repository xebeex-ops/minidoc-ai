from fastapi.testclient import TestClient
from minidoc.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() =={
        'message':'Welcome to MiniDoc AI'
    }

def test_health_endpoint():
    response = client.get('/health')

    assert response.status_code == 200
    assert response.json() == {
        'status':'ok'
    }  