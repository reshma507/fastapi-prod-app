from fastapi import FastAPI
import os
import redis

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI Production App Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
