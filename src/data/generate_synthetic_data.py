import random
from pathlib import Path

import pandas as pd


def generate_synthetic_data(num_samples: int = 1000) -> pd.DataFrame:
    positive_texts = [
        "I absolutely love this!",
        "This is fantastic.",
        "Great experience overall.",
        "Highly recommended.",
        "Amazing product!",
    ]
    negative_texts = [
        "I hate this.",
        "This is terrible.",
        "Very bad experience.",
        "Would not recommend.",
        "Awful product.",
    ]
    neutral_texts = [
        "It's okay.",
        "Average experience.",
        "Nothing special.",
        "It's fine.",
        "Not good, not bad.",
    ]

    data = {"text": [], "label": []}

    pos_n = num_samples // 3
    neg_n = num_samples // 3
    neu_n = num_samples - pos_n - neg_n

    for _ in range(pos_n):
        data["text"].append(random.choice(positive_texts))
        data["label"].append(1)

    for _ in range(neg_n):
        data["text"].append(random.choice(negative_texts))
        data["label"].append(0)

    for _ in range(neu_n):
        t = random.choice(neutral_texts)
        # neutral randomly assigned
        data["text"].append(t)
        data["label"].append(random.choice([0, 1]))

    df = pd.DataFrame(data).sample(frac=1, random_state=42).reset_index(drop=True)
    return df


if __name__ == "__main__":
    out_dir = Path("data/raw")
    out_dir.mkdir(parents=True, exist_ok=True)
    df = generate_synthetic_data(1000)
    df.to_csv(out_dir / "synthetic_data.csv", index=False)
    print("Synthetic data saved to data/raw/synthetic_data.csv")
