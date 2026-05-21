# K8s AI Log Analyzer

A Kubernetes-based incident analysis project built using Flask, Docker, Minikube, and OpenAI.

This project simulates a backend application running inside Kubernetes and generates realistic operational logs such as payment failures, database latency warnings, authentication activity, and application errors.

The generated logs are collected from Kubernetes pods and analyzed using Python and AI-assisted summarization workflows.

---

## Features

- Flask backend service deployed on Kubernetes
- Dockerized Python application
- Kubernetes Deployment and Service
- Multiple pod replicas
- Realistic operational log generation
- AI-assisted incident analysis
- Kubernetes log inspection using kubectl
- Python automation workflow

---

## Architecture

```text
User Requests
      ↓
Flask Backend Service
      ↓
Kubernetes Pods
      ↓
Application Logs
      ↓
Python Log Analyzer
      ↓
AI Incident Summary
```

---

## Tech Stack

- Kubernetes
- Minikube
- Docker
- Python
- Flask
- OpenAI API
- kubectl

---

## Project Structure

```text
k8s-ai-log-analyzer/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── analyzer/
│   └── analyze_logs.py
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

---

## Simulated Incidents

The application generates realistic backend operational logs including:

- User login activity
- Payment gateway slowdowns
- Payment service timeouts
- Database latency warnings
- Application crash simulations
- Health check events

Example logs:

```text
INFO: User login attempt: admin
WARNING: Payment gateway slow response
ERROR: Payment service timeout
WARNING: Database query latency high
ERROR: Application crash simulated
```

---

## Setup Instructions

### Start Minikube

```bash
minikube start
```

### Configure Docker Environment

```bash
eval $(minikube docker-env)
```

### Build Docker Image

```bash
cd app
docker build -t log-generator:v1 .
```

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

---

## Generate Logs

Port-forward the application:

```bash
kubectl port-forward service/log-generator-service 5000:80
```

Open endpoints in browser:

```text
http://localhost:5000/login
http://localhost:5000/payment
http://localhost:5000/database
http://localhost:5000/error
```

These endpoints generate operational logs inside Kubernetes pods.

---

## View Kubernetes Logs

```bash
kubectl logs deployment/log-generator
```

---

## Run AI Log Analyzer

```bash
python analyzer/analyze_logs.py
```

The analyzer:
- collects Kubernetes pod logs
- identifies operational issues
- summarizes incidents
- highlights warnings and failures

---

## Example Incident Summary

```text
- Payment service instability detected
- Database latency warnings observed
- Multiple application failures recorded
- Authentication activity appears normal
```

---

## Learning Goals

This project was built to learn:

- Kubernetes deployments
- Container orchestration
- Kubernetes logging workflows
- Pod debugging and observability
- Infrastructure automation
- AI-assisted operational analysis

---

## Future Improvements

- Grafana dashboards
- Prometheus monitoring
- Slack alerting
- Helm chart support
- CI/CD pipeline integration
- Automated remediation workflows

---

## Author

Built as a hands-on Kubernetes and platform engineering learning project.

