import subprocess
from openai import OpenAI

client = OpenAI()

# Get Kubernetes logs
logs = subprocess.check_output(
    ["kubectl", "logs", "deployment/log-generator"]
).decode("utf-8")

print("Collected Logs:\\n")
print(logs)

prompt = f"""
Analyze these Kubernetes application logs.

Identify:
- errors
- warnings
- possible issues
- short incident summary

Logs:
{logs}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

summary = response.choices[0].message.content

print("\\n===== AI INCIDENT SUMMARY =====\\n")
print(summary)