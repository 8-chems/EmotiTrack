import pandas as pd
import random

def generate_synthetic_data(num_samples: int) -> pd.DataFrame:
    texts = [
        "I love this product!",
        "This is the worst experience I've ever had.",
        "Absolutely fantastic!",
        "I'm not happy with the service.",
        "This is okay, not great.",
        "I would definitely recommend this.",
        "Terrible, would not buy again.",
        "Very satisfied with my purchase.",
        "It's just average.",
        "I hate it."
    ]
    labels = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0]  # 1 for positive, 0 for negative

    data = {
        "text": [random.choice(texts) for _ in range(num_samples)],
        "label": [random.choice(labels) for _ in range(num_samples)]
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    synthetic_data = generate_synthetic_data(100)  # Generate 100 samples
    synthetic_data.to_csv("data/raw/synthetic_data.csv", index=False)
