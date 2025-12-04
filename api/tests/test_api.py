"""
test_api.py
-----------
Pytest suite for testing the Customer Churn Prediction API endpoints.

To run these tests:
1. Ensure you are in the project's root directory:
   <Project Root Directory> (e.g., C:\...\Customer Churn Predictor\)
2. Execute pytest using the Python module runner, which correctly sets the
   package path for imports:

   python -m pytest api/tests/

The tests use the absolute package import 'from api.main import app'
to access the FastAPI application object.
"""
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_predict():
    sample = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "No",
        "DeviceProtection": "Yes",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.5,
        "TotalCharges": 800.4
    }

    response = client.post("/predict", json=sample)

    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "churn_probability" in response.json()
