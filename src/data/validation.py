import logging
from pathlib import Path
from typing import List, Tuple

import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("emotitrack.validation")


class DataValidator:
    def __init__(self, required: List[str] = None):
        self.required = required or ["text", "label"]
        self.errors: List[str] = []

    def validate_schema(self, df: pd.DataFrame) -> bool:
        missing = set(self.required) - set(df.columns)
        if missing:
            self.errors.append(f"Missing columns: {missing}")
            return False
        return True

    def validate_missing(self, df: pd.DataFrame) -> bool:
        if df[self.required].isnull().any().any():
            self.errors.append("Missing values in required columns.")
            return False
        return True

    def validate_labels(self, df: pd.DataFrame) -> bool:
        if not set(df["label"].unique()).issubset({0, 1}):
            self.errors.append("Label values must be 0 or 1.")
            return False
        return True

    def validate_all(self, df: pd.DataFrame) -> Tuple[bool, List[str]]:
        self.errors = []
        checks = [
            self.validate_schema(df),
            self.validate_missing(df),
            self.validate_labels(df),
        ]
        ok = all(checks)
        if not ok:
            logger.error("Validation failed: %s", self.errors)
        else:
            logger.info("Validation passed.")
        return ok, self.errors


def validate_data(df: pd.DataFrame) -> bool:
    v = DataValidator()
    ok, _ = v.validate_all(df)
    return ok


if __name__ == "__main__":
    p = Path("data/processed/cleaned_data.csv")
    df = pd.read_csv(p)
    ok, errs = DataValidator().validate_all(df)
    if not ok:
        raise SystemExit(1)
