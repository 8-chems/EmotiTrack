from pathlib import Path

import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["text_length"] = df["text"].str.len()
    df["word_count"] = df["text"].str.split().str.len()
    return df


if __name__ == "__main__":
    src = Path("data/processed/cleaned_data.csv")
    dst = Path("data/processed/feature_data.csv")
    dst.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(src)
    features = build_features(df)
    features.to_csv(dst, index=False)
    print(f"Feature data saved to {dst}")
