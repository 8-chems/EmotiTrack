"""
FastAPI application for EmotiTrack sentiment analysis.
"""

import logging
import os
from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

from src.api.middleware import log_requests_middleware

app.middleware("http")(log_requests_middleware)


# Logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("emotitrack.api")

app = FastAPI(
    title="EmotiTrack Sentiment Analysis API",
    description="Sentiment analysis API with monitoring and MLOps tooling.",
    version="1.0.0",
)

# Prometheus metrics
instrumentator = Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
)
instrumentator.instrument(app).expose(app, endpoint="/metrics")

MODEL_PATH = Path(os.getenv("MODEL_PATH", "models/sentiment_classifier.joblib"))
model = None


class SentimentRequest(BaseModel):
    text: str

    class Config:
        json_schema_extra = {"example": {"text": "I love this product!"}}


class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    confidence: float


def load_model():
    if not MODEL_PATH.exists():
        msg = f"Model file not found at {MODEL_PATH}. Train it with: python src/models/train.py"
        logger.error(msg)
        raise FileNotFoundError(msg)

    logger.info("Loading model from %s", MODEL_PATH)
    return joblib.load(MODEL_PATH)


@app.on_event("startup")
async def on_startup():
    global model
    model = load_model()
    logger.info("Model loaded successfully.")


@app.get("/", tags=["health"])
async def root():
    return {
        "message": "Welcome to EmotiTrack Sentiment Analysis API",
        "status": "healthy" if model is not None else "unhealthy",
        "version": "1.0.0",
    }


@app.get("/health", tags=["health"])
async def health():
    return {
        "status": "healthy" if model is not None else "unhealthy",
        "model_loaded": model is not None,
    }


@app.post("/predict", response_model=SentimentResponse, tags=["prediction"])
async def predict(request: SentimentRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Text must be a non-empty string.")

    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")

    try:
        proba = model.predict_proba([request.text])[0]
        pred = model.predict([request.text])[0]
        sentiment = "positive" if pred == 1 else "negative"
        confidence = float(max(proba))
        return SentimentResponse(text=request.text, sentiment=sentiment, confidence=confidence)
    except Exception as e:
        logger.exception("Prediction failed: %s", e)
        raise HTTPException(status_code=500, detail="Prediction failed.") from e


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("src.api.app:app", host="0.0.0.0", port=port, reload=True)
