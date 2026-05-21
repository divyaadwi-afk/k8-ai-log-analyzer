# K8s AI Log Analyzer

A Kubernetes-based log analysis project built using Flask, Docker, Minikube, and OpenAI.

This project simulates application logs inside Kubernetes pods and uses AI-assisted analysis to summarize incidents, detect issues, and identify possible operational problems from runtime logs.

---

## Features

- Flask application deployed on Kubernetes
- Dockerized application
- Kubernetes Deployment and Service
- Multiple pod replicas
- Real-time log generation
- Kubernetes log inspection using kubectl
- AI-assisted incident summarization using OpenAI
- Python-based automation workflow

---

## Architecture

```text
User Requests
      ↓
Flask Application
      ↓
Kubernetes Pods
      ↓
Application Logs
      ↓
Python Analyzer Script
      ↓
OpenAI Log Summary
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

Open in browser:

```text
http://localhost:5000
```

Generate simulated errors:

```text
http://localhost:5000/error
```

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
- sends logs for AI-based summarization
- identifies warnings and errors
- generates incident summaries

---

## Example AI Summary

```text
- Multiple database timeout errors detected
- High response latency observed
- Application operational but unstable
- Recommended investigation into backend dependencies
```

---

## Learning Goals

This project was built to learn:

- Kubernetes deployments
- Container orchestration
- Pod logging and debugging
- Kubernetes networking basics
- Infrastructure automation workflows
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