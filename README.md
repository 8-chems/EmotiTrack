# Sentiment Analysis API

This project implements a sentiment analysis API using FastAPI and Hugging Face Transformers.

## Features

- Automated data pipeline
- Experiment tracking with MLflow
- CI/CD automation with GitHub Actions
- Production-ready API with FastAPI
- Containerization with Docker
- Monitoring and alerting for data drift using Evidently
- Metrics monitoring with Prometheus and Grafana

## Installation

```bash
pip install -r requirements.txt
```

## Usage

To run the API, use:

```bash
uvicorn src/api/app:app --reload
```

### Monitoring with Evidently, Prometheus, and Grafana

1. **Run Prometheus**:
   ```bash
   prometheus --config.file=prometheus.yml
   ```

2. **Run Grafana** and add Prometheus as a data source.

3. **Access Metrics**: Visit `http://localhost:8000/metrics` to see the exposed metrics.

4. **Monitor Data Drift**: Use Evidently to monitor data drift and model performance.
