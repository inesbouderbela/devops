# 🚀 DevOps API Project

> A FastAPI-based REST API demonstrating complete DevOps practices including CI/CD, observability, security scanning, and Kubernetes deployment.

[![CI/CD](https://github.com/TON_USERNAME/devops/actions/workflows/main.yml/badge.svg)](https://github.com/TON_USERNAME/devops/actions)

## 📋 Table of Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [API Endpoints](#api-endpoints)
- [Development](#development)
- [Docker](#docker)
- [Kubernetes](#kubernetes)
- [CI/CD Pipeline](#cicd-pipeline)
- [Observability](#observability)
- [Security](#security)

## ✨ Features

- ✅ **FastAPI REST API** with health checks and metrics
- 📊 **Observability**: Prometheus metrics, JSON logs, OpenTelemetry tracing
- 🔒 **Security**: SAST (Bandit) + DAST (OWASP ZAP)
- 🐳 **Containerized** with Docker
- ☸️ **Kubernetes** deployment with automated CI/CD
- 🔄 **GitHub Actions** pipeline with automated testing

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker
- kubectl + kind (for Kubernetes)

### Local Development
```bash
# Clone repository
git clone https://github.com/TON_USERNAME/devops.git
cd devops

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload

# Test endpoints
curl http://localhost:8000/health
curl http://localhost:8000/hello?name=YourName
curl http://localhost:8000/metrics
```

## 📍 API Endpoints

| Endpoint | Method | Description | Example |
|----------|--------|-------------|---------|
| `/` | GET | Root endpoint | `curl http://localhost:8000/` |
| `/health` | GET | Health check | `curl http://localhost:8000/health` |
| `/hello` | GET | Personalized greeting | `curl http://localhost:8000/hello?name=Ines` |
| `/metrics` | GET | Prometheus metrics | `curl http://localhost:8000/metrics` |

### Example Responses

**Health Check:**
```json
{
  "status": "ok"
}
```

**Hello Endpoint:**
```json
{
  "message": "Hello, Ines!"
}
```

## 🛠️ Development

### Running Tests
```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app
```

### Project Structure
```
devops/
├── app/
│   └── main.py              # FastAPI application
├── tests/
│   └── test_api.py          # Unit tests
├── k8s/
│   ├── deployment.yaml      # Kubernetes deployment
│   └── service.yaml         # Kubernetes service
├── .github/
│   └── workflows/
│       └── main.yml         # CI/CD pipeline
├── Dockerfile               # Container definition
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🐳 Docker

### Build Image
```bash
docker build -t inesbouderbela3/devops-api:latest .
```

### Run Container
```bash
docker run -p 8000:8000 inesbouderbela3/devops-api:latest
```

### Push to Docker Hub
```bash
docker push inesbouderbela3/devops-api:latest
```

## ☸️ Kubernetes

### Deploy with Kind
```bash
# Create cluster
kind create cluster --name devops-cluster

# Load image
kind load docker-image inesbouderbela3/devops-api:latest --name devops-cluster

# Apply manifests
kubectl apply -f k8s/

# Verify deployment
kubectl get all

# Port forward to access
kubectl port-forward service/api-service 8000:80
```

### Access Service
```bash
curl http://localhost:8000/health
```

## 🔄 CI/CD Pipeline

The GitHub Actions pipeline automatically:

1. ✅ Runs unit tests
2. 🔍 Performs SAST scan (Bandit)
3. 🔍 Performs DAST scan (OWASP ZAP)
4. 🐳 Builds Docker image
5. 📤 Pushes to Docker Hub
6. ☸️ Deploys to Kubernetes
7. ✅ Verifies deployment

**Pipeline triggers:** Push to `main` or Pull Request

## 📊 Observability

### Metrics

Access Prometheus metrics at: `http://localhost:8000/metrics`

**Available Metrics:**
- `request_count` - Total HTTP requests by method and endpoint
- `request_latency_seconds` - Request duration histogram

### Logs

Structured JSON logs for all requests:
```json
{
  "time": "2024-12-23 10:30:45",
  "level": "INFO",
  "method": "GET",
  "path": "/health",
  "status": 200
}
```

### Tracing

OpenTelemetry instrumentation provides distributed tracing for all requests.

## 🔒 Security

### Static Analysis (SAST)
- **Tool:** Bandit
- **Runs:** Every push/PR
- **Reports:** Available in GitHub Actions artifacts

### Dynamic Analysis (DAST)
- **Tool:** OWASP ZAP Baseline Scan
- **Runs:** Every push/PR
- **Reports:** Available in GitHub Actions artifacts

### Security Results
- ✅ No critical vulnerabilities
- ⚠️ 3 low-priority warnings (missing security headers)

## 📝 Technology Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Python 3.11, FastAPI |
| **Metrics** | Prometheus Client |
| **Logging** | Python Logging (JSON) |
| **Tracing** | OpenTelemetry |
| **SAST** | Bandit |
| **DAST** | OWASP ZAP |
| **Container** | Docker |
| **Orchestration** | Kubernetes (Kind) |
| **CI/CD** | GitHub Actions |
| **Registry** | Docker Hub |

## 📄 License

MIT License

## 👤 Author

**Ines Bouderbela**

---

⭐ If you found this project helpful, please give it a star!