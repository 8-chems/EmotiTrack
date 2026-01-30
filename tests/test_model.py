import pandas as pd

from src.models.train import train_classifier
from src.models.predict import predict


def test_train_and_predict():
    df = pd.DataFrame(
        {
            "text": ["I love this", "I hate this"],
            "label": [1, 0],
        }
    )
    model, metrics = train_classifier(df)
    assert "accuracy" in metrics
    res = predict(model, ["I love this"])
    assert len(res) == 1
    assert "sentiment" in res[0]
