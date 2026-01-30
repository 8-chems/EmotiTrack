import pandas as pd

from src.data.cleaning import clean_data
from src.data.validation import validate_data


def test_clean_and_validate():
    df = pd.DataFrame({"text": ["I love this", None], "label": [1, 0]})
    cleaned = clean_data(df)
    assert cleaned["text"].isnull().sum() == 0
    assert validate_data(cleaned)
