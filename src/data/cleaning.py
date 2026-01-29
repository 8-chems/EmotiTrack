import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Example cleaning steps
    df.dropna(inplace=True)  # Remove missing values
    df['text'] = df['text'].str.strip()  # Strip whitespace
    return df

if __name__ == "__main__":
    data = pd.read_csv("data/raw/data.csv")
    cleaned_data = clean_data(data)
    cleaned_data.to_csv("data/processed/cleaned_data.csv", index=False)
