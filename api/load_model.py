import joblib
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
METADATA_PATH = os.path.join(BASE_DIR, "metadata.json")

def load_pipeline():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    if not os.path.exists(METADATA_PATH):
        raise FileNotFoundError(f"Metadata file not found at: {METADATA_PATH}")

    with open(METADATA_PATH, "r") as f:
        metadata = json.load(f)

    return model, metadata
