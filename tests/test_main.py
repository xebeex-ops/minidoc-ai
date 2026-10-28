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

def test_ask_endpoint():
    response = client.post(''
    '/ask',
    json={'question':'What is this document about?'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'received_question':'What is this document about?'
    }

def test_ask_endpoint_requires_question():
    response = client.post('/ask', json={})

    assert response.status_code == 422

def test_ask_endpoint_rejects_empty_question():
    response = client.post('/ask', json={'question': ''})
    
    assert response.status_code == 422

def test_ask_endpoint_rejects_whitespace_question():
    response = client.post('/ask', json={'question':' '})

    assert response.status_code == 422