import json
import logging
from datetime import datetime
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("emotitrack.train")


def train_classifier(df: pd.DataFrame):
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
    )

    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
            ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    logger.info("Training model on %d samples", len(X_train))
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    logger.info("Accuracy: %.4f", acc)
    logger.info("Classification report:\n%s", classification_report(y_test, y_pred))

    metrics = {
        "accuracy": float(acc),
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "timestamp": datetime.utcnow().isoformat(),
    }
    return pipeline, metrics


if __name__ == "__main__":
    feature_path = Path("data/processed/feature_data.csv")
    if not feature_path.exists():
        # Fallback: generate synthetic data
        from src.data.generate_synthetic_data import generate_synthetic_data

        df = generate_synthetic_data(1000)
    else:
        df = pd.read_csv(feature_path)

    model, metrics = train_classifier(df)

    Path("models").mkdir(exist_ok=True)
    model_path = Path("models/sentiment_classifier.joblib")
    joblib.dump(model, model_path)

    Path("metrics").mkdir(exist_ok=True)
    with open("metrics/training_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Model saved to {model_path}")
