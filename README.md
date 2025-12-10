
---
<div align="center">
    
# **Customer Churn Prediction System**

### 🚀 **Machine Learning • FastAPI • Docker • Render • Streamlit UI**

This project is a **full production-level machine learning system** built to predict telecom customer churn.  
It follows real industry workflows: **data cleaning → modeling → MLOps → API deployment → UI frontend**.  

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-teal.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
</div>
The system includes:  


* ✅ A trained ML model (Logistic Regression)
* ✅ A FastAPI microservice wrapped in Docker
* ✅ Cloud deployment on Render
* ✅ A Streamlit user interface
* ✅ Complete validation, testing, and documentation
* ✅ Production practices: schema validation, column consistency checks, unit tests, versioning





---

# 📌 **Live Demo**

### 🎯 **Interactive Web UI (Streamlit)**

👉 *[https://customer-churn-predictor-service.streamlit.app](https://customer-churn-predictor-service.streamlit.app)*

### ⚙️ **Prediction API (FastAPI, Swagger UI)**

👉 **[https://customer-churn-predictor-6q1x.onrender.com/docs](https://customer-churn-predictor-6q1x.onrender.com/docs)**

---

# 📦 **Project Structure**

```
Customer-Churn-Predictor/
├── api/
│   ├── tests/
│   │   └── test_api.py
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── load_model.py
│   ├── main.py             # FastAPI entry point
│   ├── metadata.json
│   ├── model.pkl           # Model copy for the API
│   ├── model_version.txt
│   ├── requirements.txt
│   └── schemas.py
├── data/
│   ├── archive.zip         # Data zip file
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── model/
│   ├── load_model.py
│   ├── metadata.json
│   ├── model.pkl           # Trained model file
│   ├── model_version.txt
│   ├── requirements.txt
│   └── __init__.py
├── notebooks/
│   └── Customer Churn.ipynb
├── streamlit_app/
│   ├── app.py              # Streamlit application
│   ├── Churn.png
│   └── requirements.txt
└── tests/
    └── test_model.py
   

```

---

# 🎯 **Project Goals**

This project simulates a real business problem:

✔ Predict which customers are likely to churn  
✔ Expose the model as a production-ready API  
✔ Deploy to cloud infrastructure  
✔ Provide a user-friendly interface for stakeholders  
✔ Demonstrate MLOps concepts (validation, versioning, tests, Docker, CI/CD readiness)  

---

# 🔍 **Dataset**

Dataset: **Telco Customer Churn Dataset** (open-source, free)

Includes features such as:

* Gender
* Senior citizen status
* Partner / dependents
* Services subscribed
* Contract type
* Payment method
* Monthly & total charges
* And more…

Target:
`Churn` → Yes / No

---

# 🛠 **Tech Stack**

### **Machine Learning**

* Python
* Pandas
* Scikit-learn
* Imbalanced data handling (class weights)
* ROC curve, confusion matrix, thresholding

### **API / Backend**

* FastAPI
* Pydantic
* Uvicorn
* Model versioning
* Schema validation

### **Deployment**

* Docker (containerized API)
* Render (cloud hosting)
* Environment reproducibility

### **Frontend**

* Streamlit
* Error-resistant input validation
* Preset examples for quick testing
* Live API health indicator

---

# 🧠 **Model Details**

**Model Used:** Logistic Regression
**Pipeline Structure:**

* OneHotEncoder for categorical features
* StandardScaler for numeric features
* Logistic Regression classifier
* Class_weight="balanced" to handle imbalance

### Key Metrics:

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 73% |
| Precision | 81% |
| Recall    | 75% |
| F1-score  | 60% |
| ROC AUC   | 82.2% |

---

# 🧪 **Testing & Validation**

The project uses multiple validation layers:

### ✔ Unit Tests

Ensures:

* Model loads correctly
* Predictions return proper output shape
* Invalid schema inputs are rejected

### ✔ API Validation (Pydantic)

Prevents invalid categorical values reaching the model.

### ✔ Deployment Validation

Checklist:

* API reachable
* Swagger UI functional
* Docker image operational
* Streamlit frontend communicates successfully

---

# 🐳 **Run the API Locally with Docker**

```bash
cd api
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

Open Swagger UI:
➡ [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

# 💻 **Run the Streamlit App Locally**

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

---

# 🌐 **Cloud Deployment (Render)**

The API is deployed to Render using:

* Docker deployment
* Auto-build from repo
* Web service running Uvicorn
* Port 8000

The Streamlit app can also be deployed to:

* Streamlit Cloud (recommended)
* Render (alternative)

---

# 🧩 **Features of the Streamlit UI**

* Fully dynamic form with all inputs
* Dropdown lists for categorical values
* SeniorCitizen mapped from Yes/No → 1/0 automatically
* “Preset Example” selector for quick predictions
* API health indicator
* Descriptive error messages
* Predict churn with a single button click

---

# 📚 **Project Reports (10 Phases)**

All phases are documented in the Jupyter notebook:

1. Data Understanding
2. Preprocessing
3. Baseline Model
4. Evaluation
5. Hyperparameter Tuning
6. Model Packaging
7. API Development
8. Dockerization
9. Cloud Deployment
10. Streamlit UI Integration

Each phase includes:

* Motivation
* Code
* Outputs
* Analysis
* Final report section

---

# 📈 **Future Improvements**

* Add monitoring (drift detection, Prometheus, Grafana)
* Implement full CI/CD workflow (GitHub Actions)
* Add experiment tracking (MLflow)
* Improve Streamlit UI styling
* Expand model comparison (XGBoost, Random Forest)

---

# 🏁 **Conclusion**

This project demonstrates the **full lifecycle of a machine learning system**, from data exploration to cloud deployment, with real-world production techniques.
It is designed to be clear, reproducible, and intuitive for hiring managers and technical reviewers.

---
