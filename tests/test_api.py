from fastapi.testclient import TestClient

from src.api.app import app

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "message" in resp.json()


def test_predict_ok(monkeypatch):
    # monkeypatch model to avoid loading real joblib
    from src.api import app as app_module

    class DummyModel:
        def predict(self, X):
            return [1]

        def predict_proba(self, X):
            return [[0.1, 0.9]]

    app_module.model = DummyModel()
    resp = client.post("/predict", json={"text": "I love this!"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["sentiment"] == "positive"
    assert body["confidence"] > 0.5


def test_predict_empty_text(monkeypatch):
    from src.api import app as app_module

    app_module.model = None  # to test validation first
    resp = client.post("/predict", json={"text": ""})
    assert resp.status_code == 400
