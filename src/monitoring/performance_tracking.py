import pandas as pd
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric import RegressionPerformanceMetric

def log_performance(current_data: pd.DataFrame, baseline_data: pd.DataFrame):
    column_mapping = ColumnMapping(
        target="label",  # The target column for your model
        features=["text"]  # The feature column(s)
    )

    # Create a report
    report = Report(metrics=[RegressionPerformanceMetric()])
    report.run(current_data=current_data, reference_data=baseline_data, column_mapping=column_mapping)

    # Save the report to a file (optional)
    report.save("performance_report.html")

if __name__ == "__main__":
    current_data = pd.read_csv("data/processed/feature_data.csv")  # Current data
    baseline_data = pd.read_csv("data/baseline_data.csv")  # Baseline data for comparison
    log_performance(current_data, baseline_data)
