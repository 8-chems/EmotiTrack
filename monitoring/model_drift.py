import pandas as pd

def detect_drift(current_data: pd.DataFrame, baseline_data: pd.DataFrame) -> bool:
    # Example drift detection logic
    current_mean = current_data['text_length'].mean()
    baseline_mean = baseline_data['text_length'].mean()
    drift_detected = abs(current_mean - baseline_mean) > 0.1  # Adjust threshold as needed
    return drift_detected

if __name__ == "__main__":
    current_data = pd.read_csv("data/processed/feature_data.csv")  # Current data
    baseline_data = pd.read_csv("data/baseline_data.csv")  # Baseline data for comparison
    if detect_drift(current_data, baseline_data):
        print("Data drift detected!")
    else:
        print("No data drift detected.")
