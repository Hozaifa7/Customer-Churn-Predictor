import pytest
import pandas as pd
from model.load_model import load_pipeline

@pytest.fixture(scope="module")
def model_pipeline():
    pipeline, metadata = load_pipeline()
    return pipeline

def test_model_loads(model_pipeline):
    assert model_pipeline is not None

def test_model_predicts(model_pipeline):
    sample_input = pd.DataFrame({
        "gender": ["Female"],
        "SeniorCitizen": [0],
        "Partner": ["Yes"],
        "Dependents": ["No"],
        "tenure": [12],
        "PhoneService": ["Yes"],
        "MultipleLines": ["No"],
        "InternetService": ["Fiber optic"],
        "OnlineSecurity": ["No"],
        "OnlineBackup": ["Yes"],
        "DeviceProtection": ["No"],
        "TechSupport": ["No"],
        "StreamingTV": ["Yes"],
        "StreamingMovies": ["No"],
        "Contract": ["Month-to-month"],
        "PaperlessBilling": ["Yes"],
        "PaymentMethod": ["Electronic check"],
        "MonthlyCharges": [70.35],
        "TotalCharges": [845.5]
    })
    preds = model_pipeline.predict(sample_input)
    probs = model_pipeline.predict_proba(sample_input)

    assert preds.shape[0] == 1
    assert probs.shape == (1, 2)  # two classes (no churn, churn)
    assert 0 <= probs[0, 1] <= 1
