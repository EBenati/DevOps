from fastapi.testclient import TestClient
from src.main import *

client = TestClient(app)

def test_root_status_endpoint(): # testa se o endpoint / está ok
    response = client.get("/")
    assert response.status_code == 200

def test_root_msg(): # testa se a mensagem enviado é "Hello: world"
    response = client.get("/")
    assert response.json() == {"Hello": "World"}

def test_teste1_status_endpoint(): # testa se o endpoint /teste1 está ok
    response = client.get("/teste1")
    assert response.status_code == 200

def test_teste1_caminho(): # testa se o endpoint /test1 está corretamente escrito
    response = client.get("/teste1")
    data = response.json()
    assert data["teste1"] is True

def test_teste1_numero_aleatorio(): # testa se o num aleatório é menor ou igual 20000
    response = client.get("/teste1")
    data = response.json()
    assert 0 <= data["num_aleatorio"] <= 20000
