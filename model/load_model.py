import joblib
import json
import os

def load_pipeline():
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    metadata_path = os.path.join(os.path.dirname(__file__), "metadata.json")

    pipeline = joblib.load(model_path)

    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    return pipeline, metadata

if __name__ == "__main__":
    pipeline, metadata = load_pipeline()
    print("Model loaded:", metadata["model_name"])
