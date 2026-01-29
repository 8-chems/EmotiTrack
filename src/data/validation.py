import pandas as pd

def validate_data(df: pd.DataFrame) -> bool:
    # Example validation checks
    if df.isnull().values.any():
        print("Data contains missing values.")
        return False
    if 'text' not in df.columns:
        print("Missing 'text' column.")
        return False
    return True

if __name__ == "__main__":
    data = pd.read_csv("data/processed/cleaned_data.csv")
    if validate_data(data):
        print("Data validation passed.")
    else:
        print("Data validation failed.")
