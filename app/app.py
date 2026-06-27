from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "EKS Kubernetes Status API is running",
        "project": "EKS Kubernetes Status API",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/status")
def status():
    return jsonify({
        "service": "eks-kubernetes-status-api",
        "status": "running",
        "version": "1.0.0",
        "platform": "Amazon EKS",
        "managed_by": "Kubernetes",
        "environment": os.getenv("APP_ENV", "dev")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)