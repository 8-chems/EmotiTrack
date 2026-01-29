import pandas as pd
from src.data.generate_synthetic_data import generate_synthetic_data

def test_generate_synthetic_data():
    num_samples = 100
    data = generate_synthetic_data(num_samples)
    assert len(data) == num_samples
    assert 'text' in data.columns
    assert 'label' in data.columns
    assert all(data['label'].isin([0, 1]))  # Labels should be 0 or 1
