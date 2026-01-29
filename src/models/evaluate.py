import pandas as pd
from sklearn.metrics import classification_report

def evaluate_model(y_true: list, y_pred: list):
    report = classification_report(y_true, y_pred)
    print(report)

if __name__ == "__main__":
    # Load your validation data and predictions
    validation_data = pd.read_csv("data/validation_data.csv")  # Replace with actual validation data path
    y_true = validation_data['label'].tolist()  # Actual labels
    y_pred = []  # Replace with actual predictions

    evaluate_model(y_true, y_pred)
