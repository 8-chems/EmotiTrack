import logging
import re
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("emotitrack.cleaning")


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(subset=["text", "label"])
    df["text"] = df["text"].apply(clean_text)
    df = df[df["text"].str.len() >= 3]
    df["label"] = df["label"].astype(int)
    df = df[df["label"].isin([0, 1])]
    logger.info("Cleaned data: %d rows", len(df))
    return df


if __name__ == "__main__":
    src = Path("data/raw/synthetic_data.csv")
    dst = Path("data/processed/cleaned_data.csv")
    dst.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(src)
    cleaned = clean_data(df)
    cleaned.to_csv(dst, index=False)
    print(f"Cleaned data saved to {dst}")
