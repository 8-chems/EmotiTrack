from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Load the model

def load_model():
    data = pd.read_csv("data/raw/synthetic_data.csv")
    model = make_pipeline(CountVectorizer(), LogisticRegression())
    model.fit(data['text'], data['label'])
    return model

app = FastAPI()
Instrumentator().instrument(app).expose(app)
model = load_model()

class SentimentRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict(request: SentimentRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    prediction = model.predict([request.text])
    sentiment = 'positive' if prediction[0] == 1 else 'negative'
    return {"sentiment": sentiment}

@app.get("/")
async def root():
    return {"message": "Welcome to the Sentiment Analysis API"}
