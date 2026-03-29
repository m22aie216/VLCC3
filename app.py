from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    # Optional: inspect alert payload
    print("Received alert:", data)

    # Trigger GCP VM creation
    subprocess.run([
        "gcloud", "compute", "instances", "create", "scaled-vm",
        "--zone=us-central1-a",
        "--machine-type=e2-medium",
        "--image-family=debian-11",
        "--image-project=debian-cloud"
    ])
    return "Scaling triggered", 200

if __name__ == '__main__':
    app.run(port=5000)

