from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    print("INFO: Home endpoint accessed", flush=True)
    return "K8s AI Log Analyzer Running"

@app.route("/login")
def login():
    users = ["admin", "guest", "test-user"]

    user = random.choice(users)

    print(f"INFO: User login attempt: {user}", flush=True)

    return "Login processed"

@app.route("/payment")
def payment():
    outcomes = [
        "INFO: Payment processed successfully",
        "WARNING: Payment gateway slow response",
        "ERROR: Payment service timeout"
    ]

    log = random.choice(outcomes)

    print(log, flush=True)

    return "Payment request completed"

@app.route("/database")
def database():
    print("WARNING: Database query latency high", flush=True)

    time.sleep(2)

    return "Database query executed"

@app.route("/health")
def health():
    print("INFO: Health check passed", flush=True)

    return "Healthy"

@app.route("/error")
def error():
    print("ERROR: Application crash simulated", flush=True)

    return "Error generated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)