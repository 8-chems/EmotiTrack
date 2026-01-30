from pathlib import Path

import pandas as pd


def detect_drift(current: pd.DataFrame, baseline: pd.DataFrame, threshold: float = 0.1) -> bool:
    if "text_length" not in current.columns or "text_length" not in baseline.columns:
        return False
    c_mean = current["text_length"].mean()
    b_mean = baseline["text_length"].mean()
    return abs(c_mean - b_mean) > threshold


if __name__ == "__main__":
    current = pd.read_csv("data/processed/feature_data.csv")
    baseline = pd.read_csv("data/baseline_data.csv")
    if detect_drift(current, baseline):
        print("Data drift detected!")
    else:
        print("No data drift detected.")
