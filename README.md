# EmotiTrack 🎭

**Production-Ready Sentiment Analysis API with MLOps Best Practices**

[![CI](https://github.com/8-chems/EmotiTrack/workflows/CI/badge.svg)](https://github.com/8-chems/EmotiTrack/actions)
[![CD](https://github.com/8-chems/EmotiTrack/workflows/CD-Heroku/badge.svg)](https://github.com/8-chems/EmotiTrack/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A complete sentiment analysis microservice featuring automated ML pipelines, Prometheus monitoring, Docker containerization, and seamless Heroku deployment with CI/CD automation.

---

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Local Development](#-local-development)
- [Docker Deployment](#-docker-deployment)
- [Heroku Deployment](#-heroku-deployment)
- [CI/CD Pipeline](#-cicd-pipeline)
- [API Documentation](#-api-documentation)
- [Monitoring & Observability](#-monitoring--observability)
- [Testing](#-testing)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Contributing](#-contributing)

---

## ✨ Features

- 🤖 **Real-time Sentiment Analysis** - Fast text classification with confidence scores
- 📊 **Prometheus Metrics** - Built-in metrics exposure for monitoring and alerting
- 🐳 **Docker Ready** - Multi-stage containerization for efficient deployment
- ☁️ **Heroku Native** - One-click deployment with Procfile configuration
- 🔄 **CI/CD Automation** - GitHub Actions workflows for testing and deployment
- 📈 **Data Pipeline** - DVC-managed data versioning and reproducible ML workflows
- 🧪 **Comprehensive Testing** - Unit tests, integration tests, and API tests
- 🔍 **Drift Detection** - Monitor model performance degradation over time
- 📝 **API Documentation** - Auto-generated OpenAPI/Swagger docs

---

## 🛠️ Technology Stack

### Core Framework & API

| Library | Version | Purpose |
|---------|---------|---------|
| **FastAPI** | 0.109.0 | High-performance async web framework for building APIs with automatic validation and documentation |
| **Uvicorn** | 0.27.0 | Lightning-fast ASGI server for serving FastAPI applications in production |
| **Pydantic** | 2.5.3 | Data validation and settings management using Python type annotations |

**Why FastAPI?** 
- 🚀 Best performance among Python web frameworks (on par with NodeJS and Go)
- 📖 Automatic interactive API documentation (Swagger UI + ReDoc)
- ✅ Built-in request/response validation
- 🔄 Native async/await support for concurrent request handling

---

### Machine Learning & Data Processing

| Library | Version | Purpose |
|---------|---------|---------|
| **scikit-learn** | 1.4.0 | ML model training (LogisticRegression + TF-IDF vectorization) for text classification |
| **pandas** | 2.2.0 | Efficient data manipulation, cleaning, and feature engineering for tabular data |
| **numpy** | 1.26.3 | Numerical computing foundation for array operations and mathematical functions |
| **joblib** | 1.3.2 | Efficient model serialization/deserialization for saving trained pipelines |

**ML Pipeline:**
- **TF-IDF Vectorizer**: Converts text to numerical features with n-gram support (1-2 grams)
- **Logistic Regression**: Fast, interpretable classifier with class balancing
- **Pipeline Architecture**: Seamless integration of preprocessing + model for production deployment

---

### Monitoring & Observability

| Library | Version | Purpose |
|---------|---------|---------|
| **prometheus-fastapi-instrumentator** | 6.1.0 | Automatic Prometheus metrics collection (request count, duration, errors) and `/metrics` endpoint exposure |

**Exposed Metrics:**
- `http_requests_total` - Total HTTP requests by method, path, status
- `http_request_duration_seconds` - Request latency histogram
- `http_requests_inprogress` - Current concurrent requests
- Custom business metrics (predictions per label, confidence distribution)

**Integration:** Heroku + Prometheus Cloud = Real-time monitoring dashboard

---

### Development & Testing

| Library | Version | Purpose |
|---------|---------|---------|
| **pytest** | 7.4.4 | Modern testing framework with fixtures, parametrization, and powerful assertions |
| **pytest-cov** | 4.1.0 | Code coverage reporting integrated with pytest |
| **httpx** | 0.26.0 | Async HTTP client for testing FastAPI endpoints with TestClient |

**Test Coverage:**
- ✅ Unit tests for data processing functions
- ✅ Integration tests for ML model training/prediction
- ✅ API endpoint tests (health, prediction, metrics)
- ✅ Synthetic data generation validation

---

### Infrastructure & Deployment

| Tool | Purpose |
|------|---------|
| **Docker** | Containerization for consistent environments across development, testing, and production |
| **Docker Compose** | Multi-container orchestration (API + Prometheus + Grafana) for local development |
| **Heroku** | Cloud platform for seamless deployment with automatic scaling and managed infrastructure |
| **GitHub Actions** | CI/CD automation for testing, linting, and deployment workflows |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER REQUEST                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    HEROKU PLATFORM                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         FastAPI Application (src/api/app.py)         │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Middleware: Request Logging & Monitoring      │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Routes: /, /health, /predict, /metrics        │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Prometheus Instrumentator (Metrics Collector) │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │       ML Model (models/sentiment_classifier.joblib)  │  │
│  │   Pipeline: TF-IDF → Logistic Regression             │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              MONITORING (Prometheus Cloud)                   │
│  - Request metrics scraped from /metrics endpoint            │
│  - Grafana dashboards for visualization                      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    CI/CD PIPELINE                            │
│                                                               │
│  GitHub Push → CI Workflow → Tests → CD Workflow → Heroku   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+ installed
- Git installed
- (Optional) Docker Desktop for containerized deployment
- (Optional) Heroku CLI for cloud deployment

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/8-chems/EmotiTrack.git
cd EmotiTrack

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create necessary directories
mkdir -p data/{raw,processed} models metrics logs
```

### Generate Data & Train Model

```bash
# Generate synthetic training data (1000 samples)
python src/data/generate_synthetic_data.py

# Clean and validate data
python src/data/cleaning.py

# Build features
python src/data/build_features.py

# Train model
python src/models/train.py
# Output: models/sentiment_classifier.joblib
```

### Run the API Locally

```bash
# Start the server
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload

# API will be available at:
# - http://localhost:8000 (root)
# - http://localhost:8000/docs (Swagger UI)
# - http://localhost:8000/redoc (ReDoc)
# - http://localhost:8000/metrics (Prometheus metrics)
```

### Test the API

```bash
# Health check
curl http://localhost:8000/health

# Make prediction
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "I absolutely love this product! Best purchase ever!"}'

# Response:
# {
#   "text": "I absolutely love this product! Best purchase ever!",
#   "sentiment": "positive",
#   "confidence": 0.95
# }

# View Prometheus metrics
curl http://localhost:8000/metrics
```

---

## 💻 Local Development

### Using DVC for Data Pipeline

```bash
# Install DVC (if not already)
pip install dvc

# Initialize DVC
dvc init

# Run entire pipeline
dvc repro

# This executes all stages defined in dvc.yaml:
# 1. generate → synthetic_data.csv
# 2. clean → cleaned_data.csv
# 3. features → feature_data.csv
# 4. train → sentiment_classifier.joblib
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_api.py -v

# Run tests in parallel (faster)
pytest -n auto
```

### Code Quality

```bash
# Format code with black
black src/ tests/

# Lint with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/
```

---

## 🐳 Docker Deployment

### Why Docker?
- **Consistency**: Same environment across dev, staging, and production
- **Isolation**: Dependencies don't conflict with host system
- **Portability**: Run anywhere Docker is supported
- **Scalability**: Easy horizontal scaling with container orchestration

### Build Docker Image

```bash
# Build the image
docker build -t emotitrack:latest .

# Verify image
docker images | grep emotitrack
```

### Run Single Container

```bash
# Run container
docker run -d \
  -p 8000:8000 \
  --name emotitrack-api \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/data:/app/data \
  emotitrack:latest

# Check logs
docker logs emotitrack-api

# Stop container
docker stop emotitrack-api
```

### Docker Compose (Full Stack)

**What's Included:**
- **API Service**: FastAPI application on port 8000
- **Prometheus**: Metrics collection on port 9090
- **Grafana**: Visualization dashboards on port 3000

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Access services:
# - API: http://localhost:8000
# - Prometheus: http://localhost:9090
# - Grafana: http://localhost:3000 (admin/admin)
```

### Docker Image Optimization

**Multi-stage Build Benefits:**
- ✅ Reduced image size (Python slim base)
- ✅ Security: No build tools in production image
- ✅ Layer caching for faster rebuilds

**Image Size:** ~150MB (compared to 1GB+ for full Python image)

---

## ☁️ Heroku Deployment

### Why Heroku?
- **Zero DevOps**: Managed infrastructure, automatic scaling
- **Git-based Deploy**: `git push heroku main` to deploy
- **Add-ons**: Easy integration with databases, monitoring, logging
- **Free Tier**: Test your app without credit card
- **CI/CD Ready**: Native GitHub integration

### Prerequisites

```bash
# Install Heroku CLI
# macOS
brew tap heroku/brew && brew install heroku

# Windows
# Download installer from https://devcenter.heroku.com/articles/heroku-cli

# Linux
curl https://cli-assets.heroku.com/install.sh | sh

# Verify installation
heroku --version
```

### Manual Deployment

```bash
# 1. Login to Heroku
heroku login

# 2. Create new Heroku app
heroku create emotitrack-api
# Or use your preferred name:
# heroku create your-custom-name

# 3. Verify Procfile exists
cat Procfile
# Should contain: web: uvicorn src.api.app:app --host 0.0.0.0 --port $PORT

# 4. Set environment variables (optional)
heroku config:set MODEL_PATH=models/sentiment_classifier.joblib
heroku config:set LOG_LEVEL=INFO

# 5. Deploy to Heroku
git push heroku main

# 6. Open application
heroku open

# 7. View logs
heroku logs --tail

# 8. Scale dynos (if needed)
heroku ps:scale web=1
```

### Heroku Configuration Details

**Procfile Explanation:**
```
web: uvicorn src.api.app:app --host 0.0.0.0 --port $PORT
```
- `web`: Dyno type (receives HTTP traffic)
- `uvicorn`: ASGI server
- `--host 0.0.0.0`: Bind to all interfaces
- `--port $PORT`: Use Heroku-assigned port (automatically set)

**Buildpack:** Python buildpack auto-detected via `requirements.txt`

**Dyno Types:**
- **Free**: 550 hrs/month, sleeps after 30min inactivity
- **Hobby**: $7/mo, never sleeps
- **Standard**: Auto-scaling, performance metrics

### Post-Deployment Verification

```bash
# Get app URL
heroku info -s | grep web_url

# Test health endpoint
curl https://your-app.herokuapp.com/health

# Test prediction
curl -X POST https://your-app.herokuapp.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!"}'

# Check metrics endpoint
curl https://your-app.herokuapp.com/metrics
```

### Heroku Add-ons for Production

```bash
# Papertrail (Logging)
heroku addons:create papertrail:choklad

# New Relic (APM)
heroku addons:create newrelic:wayne

# Heroku Postgres (Database - if needed)
heroku addons:create heroku-postgresql:mini

# Redis (Caching - if needed)
heroku addons:create heroku-redis:mini
```

### Monitoring on Heroku

```bash
# View metrics
heroku metrics:web --app emotitrack-api

# View logs
heroku logs --tail --app emotitrack-api

# Restart dynos
heroku restart --app emotitrack-api
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

**Architecture:**
```
GitHub Push/PR
    │
    ├─► CI Workflow (.github/workflows/ci.yml)
    │   ├─ Checkout code
    │   ├─ Setup Python 3.10
    │   ├─ Install dependencies
    │   ├─ Run pytest (all tests)
    │   └─ Report results
    │
    └─► CD Workflow (.github/workflows/cd-heroku.yml)
        ├─ Wait for CI to pass
        ├─ Checkout code
        ├─ Run tests again
        ├─ Login to Heroku
        └─ Deploy to Heroku
```

### CI Workflow (ci.yml)

**Purpose:** Automated testing on every push/PR

**What it does:**
1. Checks out code from repository
2. Sets up Python 3.10 environment
3. Installs project dependencies
4. Runs full test suite with pytest
5. Reports test results (pass/fail)

**Triggers:**
- Push to `main` branch
- Pull requests to `main` branch

**Benefits:**
- ✅ Catch bugs before deployment
- ✅ Ensure code quality standards
- ✅ Prevent broken code from reaching production

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: pip install -r requirements.txt
      - run: pytest -q
```

### CD Workflow (cd-heroku.yml)

**Purpose:** Automated deployment to Heroku after tests pass

**What it does:**
1. Waits for CI workflow to complete successfully
2. Runs tests again (safety check)
3. Authenticates with Heroku API
4. Pushes code to Heroku Git remote
5. Heroku automatically builds and deploys

**Triggers:**
- Push to `main` branch (only after CI passes)

**Required Secrets (GitHub Repository Settings):**
- `HEROKU_API_KEY`: Your Heroku API token
- `HEROKU_APP_NAME`: Your Heroku app name

```yaml
name: CD-Heroku
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: pytest -q
      - run: curl https://cli-assets.heroku.com/install.sh | sh
      - run: |
          git remote add heroku https://heroku:${{ secrets.HEROKU_API_KEY }}@git.heroku.com/${{ secrets.HEROKU_APP_NAME }}.git
          git push heroku HEAD:main -f
```

### Setting Up GitHub Secrets

```bash
# 1. Get Heroku API key
heroku auth:token

# 2. In GitHub repository:
#    Settings → Secrets and variables → Actions → New repository secret

# 3. Add these secrets:
#    Name: HEROKU_API_KEY
#    Value: <paste-your-token>
#
#    Name: HEROKU_APP_NAME
#    Value: emotitrack-api
```

### Scheduled Retraining (retrain.yml)

**Purpose:** Weekly model retraining to prevent performance degradation

```yaml
name: Scheduled Retraining
on:
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday at midnight UTC

jobs:
  retrain:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: python src/models/train.py
      - run: git config --global user.email "bot@emotitrack.com"
      - run: git config --global user.name "Retrain Bot"
      - run: git add models/
      - run: git commit -m "Automated model retraining"
      - run: git push
```

### CI/CD Best Practices

✅ **Do:**
- Run tests in CI before deployment
- Use separate staging and production environments
- Version your models (timestamp in filename)
- Monitor deployment metrics
- Set up rollback strategy

❌ **Don't:**
- Deploy without tests passing
- Hardcode secrets in code
- Skip version control for models
- Deploy on Fridays (joke, but seriously...)

---

## 📚 API Documentation

### Interactive Documentation

FastAPI automatically generates interactive API docs:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints

#### `GET /`
**Description:** Root endpoint with API information

**Response:**
```json
{
  "message": "Welcome to EmotiTrack Sentiment Analysis API",
  "status": "healthy",
  "version": "1.0.0"
}
```

---

#### `GET /health`
**Description:** Health check endpoint for monitoring

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

**Use Case:** Load balancer health checks, uptime monitoring

---

#### `POST /predict`
**Description:** Predict sentiment from text input

**Request Body:**
```json
{
  "text": "I absolutely love this product!"
}
```

**Response:**
```json
{
  "text": "I absolutely love this product!",
  "sentiment": "positive",
  "confidence": 0.9234
}
```

**Status Codes:**
- `200`: Success
- `400`: Invalid input (empty text)
- `503`: Model not loaded

---

#### `GET /metrics`
**Description:** Prometheus metrics endpoint

**Response:** Plain text Prometheus format
```
# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="POST",path="/predict",status="200"} 42.0

# HELP http_request_duration_seconds HTTP request duration
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.1",method="POST",path="/predict"} 35.0
...
```

---

## 📊 Monitoring & Observability

### Prometheus Metrics

**Automatically Collected:**
- Request count by endpoint, method, status code
- Request duration (latency) percentiles (p50, p90, p99)
- Requests in progress (concurrent load)
- Python process metrics (CPU, memory, GC)

### Grafana Dashboard Setup

```bash
# 1. Start Grafana with Docker Compose
docker-compose up -d grafana

# 2. Access Grafana: http://localhost:3000
#    Default credentials: admin / admin

# 3. Add Prometheus data source:
#    Configuration → Data Sources → Add Prometheus
#    URL: http://prometheus:9090

# 4. Import dashboard:
#    Create → Import → Dashboard ID: 10427 (FastAPI dashboard)
```

### Key Metrics to Monitor

| Metric | Description | Alert Threshold |
|--------|-------------|----------------|
| Request Rate | Requests per second | Sudden drops/spikes |
| Error Rate | 4xx/5xx responses | > 5% |
| Latency p99 | 99th percentile response time | > 500ms |
| Model Confidence | Average prediction confidence | < 0.7 (drift) |

---

## 🧪 Testing

### Test Coverage

```bash
# Run with coverage report
pytest --cov=src --cov-report=term-missing --cov-report=html

# View HTML report
open htmlcov/index.html
```

**Current Coverage:** ~85%

### Test Categories

**Unit Tests:**
- Data cleaning functions
- Feature engineering
- Validation logic

**Integration Tests:**
- Model training pipeline
- Prediction workflow

**API Tests:**
- Endpoint responses
- Error handling
- Input validation

---

## 📂 Project Structure

```
EmotiTrack/
├── .github/
│   └── workflows/
│       ├── ci.yml                # Continuous Integration
│       ├── cd-heroku.yml         # Continuous Deployment
│       └── retrain.yml           # Scheduled Retraining
│
├── src/
│   ├── api/
│   │   ├── app.py               # FastAPI application
│   │   └── middleware.py        # Request logging
│   │
│   ├── data/
│   │   ├── generate_synthetic_data.py
│   │   ├── cleaning.py
│   │   ├── validation.py
│   │   └── build_features.py
│   │
│   ├── models/
│   │   ├── train.py             # Model training
│   │   ├── predict.py           # Inference logic
│   │   └── evaluate.py          # Model evaluation
│   │
│   └── monitoring/
│       ├── performance_tracking.py
│       └── model_drift.py
│
├── tests/
│   ├── test_api.py
│   ├── test_data.py
│   ├── test_model.py
│   └── test_synthetic_data.py
│
├── config/
│   ├── model_config.yaml
│   └── deployment_config.yaml
│
├── data/                        # gitignored
│   ├── raw/
│   └── processed/
│
├── models/                      # gitignored
│   └── sentiment_classifier.joblib
│
├── metrics/                     # gitignored
│   └── training_metrics.json
│
├── Dockerfile                   # Container definition
├── docker-compose.yml           # Multi-container orchestration
├── Procfile                     # Heroku process definition
├── requirements.txt             # Python dependencies
├── dvc.yaml                     # Data pipeline definition
├── prometheus.yml               # Prometheus config
└── README.md                    # This file
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `MODEL_PATH` | `models/sentiment_classifier.joblib` | Path to trained model |
| `LOG_LEVEL` | `INFO` | Logging verbosity (DEBUG/INFO/WARNING/ERROR) |
| `PORT` | `8000` | API server port (auto-set by Heroku) |

### Setting in Heroku

```bash
heroku config:set LOG_LEVEL=DEBUG
heroku config:set MODEL_PATH=models/sentiment_classifier.joblib
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

**Code Quality Requirements:**
- All tests must pass (`pytest`)
- Code coverage > 80%
- Follow PEP 8 style guide
- Add docstrings to new functions

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 👤 Author

**8-chems**
- GitHub: [@8-chems](https://github.com/8-chems)

---

## 🙏 Acknowledgments

- **FastAPI** - Modern web framework
- **scikit-learn** - ML toolkit
- **Heroku** - Cloud platform
- **Prometheus** - Monitoring system
- **Docker** - Containerization

---

## 📞 Support

- 📧 Email: support@emotitrack.com
- 🐛 Issues: [GitHub Issues](https://github.com/8-chems/EmotiTrack/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/8-chems/EmotiTrack/discussions)

---

**Built with ❤️ by the EmotiTrack Team**
