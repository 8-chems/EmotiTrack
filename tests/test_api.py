import pytest
from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sentiment Analysis API"}


def test_predict():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
