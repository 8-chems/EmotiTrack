from src.data.generate_synthetic_data import generate_synthetic_data


def test_generate_synthetic_data():
    df = generate_synthetic_data(100)
    assert len(df) == 100
    assert set(df.columns) == {"text", "label"}
    assert set(df["label"].unique()).issubset({0, 1})
