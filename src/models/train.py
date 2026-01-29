import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib  # Import joblib for saving the model

def train_classifier(train_data: pd.DataFrame):
    # Using logistic regression for a simple classifier
    model = make_pipeline(CountVectorizer(), LogisticRegression())
    model.fit(train_data['text'], train_data['label'])
    return model

if __name__ == "__main__":
    # Generate synthetic data
    from data.generate_synthetic_data import generate_synthetic_data
    data = generate_synthetic_data(100)  # Generate 100 samples
    model = train_classifier(data)
    
    # Save the model to a file
    joblib.dump(model, 'models/sentiment_classifier.joblib')  # Save the model

    train_data = pd.read_csv("data/processed/feature_data.csv")
    model = train_classifier(train_data)
    joblib.dump(model, 'models/sentiment_classifier.joblib')  # Save the model
