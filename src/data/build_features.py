import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    # Example feature engineering
    df['text_length'] = df['text'].apply(len)  # Add a feature for text length
    return df

if __name__ == "__main__":
    data = pd.read_csv("data/processed/cleaned_data.csv")
    feature_data = build_features(data)
    feature_data.to_csv("data/processed/feature_data.csv", index=False)
