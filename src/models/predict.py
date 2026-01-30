from pathlib import Path
from typing import List, Dict

import joblib


def load_model(path: str = "models/sentiment_classifier.joblib"):
    return joblib.load(Path(path))


def predict(model, texts: List[str]) -> List[Dict]:
    proba = model.predict_proba(texts)
    preds = model.predict(texts)
    results = []
    for t, p, pr in zip(texts, preds, proba):
        results.append(
            {
                "text": t,
                "sentiment": "positive" if p == 1 else "negative",
                "confidence": float(max(pr)),
            }
        )
    return results
