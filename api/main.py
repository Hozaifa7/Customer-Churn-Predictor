"""
main.py
-------
FastAPI application for Customer Churn Prediction.

To run the API server:
1. Ensure you are in the project's root directory:
   <Project Root Directory> (e.g., C:\...\Customer Churn Predictor\)
2. Execute the uvicorn command, specifying the full package path:

   uvicorn api.main:app --reload

This command runs the 'app' object inside the 'main' module of the 'api' package.
"""
from fastapi import FastAPI
from load_model import load_pipeline
from schemas import CustomerFeatures
import numpy as np
import pandas as pd

app = FastAPI(title="Customer Churn Prediction API")

model, metadata = load_pipeline()

@app.get("/")
def root():
    return {"message": "Churn Prediction API is running"}

@app.get("/version")
def version():
    return {"model_version": metadata["version"]}

@app.post("/predict")
def predict(features: CustomerFeatures):

    data = pd.DataFrame([features.model_dump()])

    proba = model.predict_proba(data)[0][1]
    prediction = int(proba >= 0.5)

    return {
        "prediction": prediction,
        "churn_probability": float(proba)
    }
