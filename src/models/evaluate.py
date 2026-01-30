import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate(model_path: str, data_path: str):
    model = joblib.load(Path(model_path))
    df = pd.read_csv(data_path)
    y_true = df["label"]
    y_pred = model.predict(df["text"])

    acc = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)
    cm = confusion_matrix(y_true, y_pred).tolist()

    metrics = {"accuracy": float(acc), "confusion_matrix": cm, "report": report}
    Path("metrics").mkdir(exist_ok=True)
    with open("metrics/eval_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    return metrics


if __name__ == "__main__":
    evaluate("models/sentiment_classifier.joblib", "data/processed/feature_data.csv")
