import pandas as pd
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric import DataDriftMetric

def detect_drift(current_data: pd.DataFrame, baseline_data: pd.DataFrame) -> bool:
    column_mapping = ColumnMapping(
        target="label",  # The target column for your model
        features=["text"]  # The feature column(s)
    )

    # Create a report
    report = Report(metrics=[DataDriftMetric()])
    report.run(current_data=current_data, reference_data=baseline_data, column_mapping=column_mapping)
    
    # Check for drift
    drift_report = report.as_dict()
    drift_detected = drift_report['metrics'][0]['value']  # Adjust based on the report structure

    return drift_detected

if __name__ == "__main__":
    current_data = pd.read_csv("data/processed/feature_data.csv")  # Current data
    baseline_data = pd.read_csv("data/baseline_data.csv")  # Baseline data for comparison
    if detect_drift(current_data, baseline_data):
        print("Data drift detected!")
    else:
        print("No data drift detected.")
