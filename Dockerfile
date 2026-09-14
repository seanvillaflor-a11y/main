from python:3.11-slim

WORKDIR /app
copy auditor.py
cmd ["python", "auditor.py"]