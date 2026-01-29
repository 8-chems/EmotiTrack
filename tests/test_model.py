import pandas as pd
from src.models.train import train_classifier
from src.models.predict import predict

def test_train_classifier():
    data = pd.DataFrame({
        'text': ["I love this!", "I hate this!"],
        'label': [1, 0]
    })
    model = train_classifier(data)
    assert model is not None  # Ensure the model is trained


def test_predict():
    data = pd.DataFrame({
        'text': ["I love this!", "I hate this!"],
        'label': [1, 0]
    })
    model = train_classifier(data)
    sample_texts = ["I love this!", "I hate this!"]
    predictions = predict(model, sample_texts)
    assert len(predictions) == len(sample_texts)  # Should match the number of input texts
