from flask import Flask
import random

app = Flask(__name__)

logs = [
    "INFO: Request received",
    "WARNING: High response time",
    "ERROR: Database timeout",
    "INFO: Health check passed"
]

@app.route("/")
def home():
    log = random.choice(logs)
    print(log, flush=True)
    return "K8s AI Log Analyzer Running"

@app.route("/error")
def error():
    print("ERROR: Simulated application failure", flush=True)
    return "Error generated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)