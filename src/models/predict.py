import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib  # Import joblib for loading the model

def train_classifier(data: pd.DataFrame):
    model = make_pipeline(CountVectorizer(), LogisticRegression())
    model.fit(data['text'], data['label'])
    return model

def load_model():
    return joblib.load('models/sentiment_classifier.joblib')  # Load the model from the file

def predict(model, text: str) -> str:
    return model.predict([text])[0]

if __name__ == "__main__":
    model = load_model()  # Load the model
    sample_texts = ["I love this!", "I hate this!"]
    predictions = [predict(model, text) for text in sample_texts]
    print(predictions)
