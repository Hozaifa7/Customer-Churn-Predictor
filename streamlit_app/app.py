import streamlit as st
import requests


API_URL = "https://customer-churn-predictor-6q1x.onrender.com/predict"
# ----------------------------
# PAGE CONFIGURATION
st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
# Centered image at the top
image_file = "churn.png"
# Create three columns: the center one is where the image goes
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Place the image in the center column
    st.image(image_file)
# ----------------------------
# TITLE AND DESCRIPTION
st.title("📊 Customer Churn Prediction App")
st.write("Fill in the customer details or choose a preset example then press the button below to predict the churn probability.")
st.write("You can find details about each input field by hovering over the question mark at the top right of each box.")
# ----------------------------
# API HEALTH CHECK
HEALTH_URL = "https://customer-churn-predictor-6q1x.onrender.com"

def check_health():
    try:
        response = requests.get(HEALTH_URL, timeout=5)
        if response.status_code == 200:
            return "healthy"
        else:
            return "unhealthy"
    except:
        return "unreachable"

status = check_health()

if status == "healthy":
    st.success("🟢 API Status: Healthy")
else:
    st.error("🔴 API Status: Not Reachable")

# ----------------------------
# PRESET EXAMPLES
# ----------------------------

presets = {
    "🔹 Example 1 – Likely to Stay": {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "Yes",
        "tenure": 36,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "Yes",
        "TechSupport": "Yes",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "One year",
        "PaperlessBilling": "No",
        "PaymentMethod": "Credit card (automatic)",
        "MonthlyCharges": 68.6,
        "TotalCharges": 2495.2
    },
    "🔸 Example 2 – Likely to Churn": {
        "gender": "Male",
        "SeniorCitizen": 1,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 5,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 89.5,
        "TotalCharges": 450.2
    }
}
preset_name = st.selectbox("Choose an example preset", presets.keys())
preset = presets[preset_name]

st.write("---")

# ----------------------------
# INPUT FORM
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"], index=["Male", "Female"].index(preset["gender"]), 
                          help="Whether the customer is a male or a female.")

    senior_yes_no = st.selectbox(
        "Senior Citizen", ["Yes", "No"],
        index=0 if preset["SeniorCitizen"] == 1 else 1,
    help = "Whether the customer is a senior citizen or not.")
    SeniorCitizen = 1 if senior_yes_no == "Yes" else 0

    Partner = st.selectbox("Partner", ["Yes", "No"], index=["Yes", "No"].index(preset["Partner"]),
                           help="Whether the customer has a partner or not.")
    Dependents = st.selectbox("Dependents", ["Yes", "No"], index=["Yes", "No"].index(preset["Dependents"]),
                              help="Whether the customer has dependents or not.")
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=preset["tenure"],
                             help="Number of months the customer has stayed with the company.")

    PhoneService = st.selectbox("Phone Service", ["Yes", "No"], index=["Yes", "No"].index(preset["PhoneService"]),
                                help="Whether the customer has phone service or not.")
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No"], index=["Yes", "No"].index(preset["MultipleLines"]),
                                 help="Whether the customer has multiple lines or not.")

    InternetService = st.selectbox(
        "Internet Service", ["DSL", "Fiber optic", "No"],
        index=["DSL", "Fiber optic", "No"].index(preset["InternetService"]),
        help="Customer's internet service provider."
    )

with col2:
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"], index=["Yes", "No"].index(preset["OnlineSecurity"]),
                                  help="Whether the customer has online security or not.")
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"], index=["Yes", "No"].index(preset["OnlineBackup"]),
                                help="Whether the customer has online backup or not.")
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No"], index=["Yes", "No"].index(preset["DeviceProtection"]),
                                    help="Whether the customer has device protection or not.")
    TechSupport = st.selectbox("Tech Support", ["Yes", "No"], index=["Yes", "No"].index(preset["TechSupport"]),
                               help="Whether the customer has tech support or not.")
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No"], index=["Yes", "No"].index(preset["StreamingTV"]),
                               help="Whether the customer has streaming TV or not.")
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"], index=["Yes", "No"].index(preset["StreamingMovies"]),
                                   help="Whether the customer has streaming movies or not.")
    Contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"],
        index=["Month-to-month", "One year", "Two year"].index(preset["Contract"]),
        help="The contract term of the customer.")
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"], index=["Yes", "No"].index(preset["PaperlessBilling"]),
                                    help="Whether the customer has paperless billing or not.")
    
st.write("\n")
st.write("\n")

PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check", "Mailed check",
            "Bank transfer (automatic)", "Credit card (automatic)"
        ],
        index=[
            "Electronic check", "Mailed check",
            "Bank transfer (automatic)", "Credit card (automatic)"
        ].index(preset["PaymentMethod"]), help="The customer's payment method."
    )
MonthlyCharges = st.number_input("Monthly Charges", min_value=18.3, value=float(preset["MonthlyCharges"]), help="The amount charged to the customer monthly.")
TotalCharges = st.number_input("Total Charges", min_value=18.8, value=float(preset["TotalCharges"]), help="The total amount charged to the customer.")

st.write("---")

# ----------------------------
# PREDICTION REQUEST
# ----------------------------

if st.button("Predict Churn", type="primary"):
    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }
    
    
    try:
        response = requests.post(API_URL, json=payload, timeout=15)

        if response.status_code == 200:
            result = response.json()

            churn = result.get("churn_prediction")
            churn_prob = result.get("churn_probability")

            st.success(f"Churn Probability: **{churn_prob:.2%}**")

            # Risk interpretation
            if churn_prob >= 0.7:
                st.error("High churn risk ⚠️")
            elif churn_prob >= 0.4:
                st.warning("Medium churn risk ⚠")
            else:
                st.success("Low churn risk ✔")

        else:
            # Attempt to parse FastAPI error response
            try:
                error_details = response.json()
                st.error(f"API Error: {error_details.get('detail', 'Unknown error')}")
            except:
                # If response is HTML or some non-JSON content
                st.error("Server returned an unexpected error. Please refresh the page and check the API status at the top.")


    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the server. Please check your connection or try again later.")

    except requests.exceptions.Timeout:
        st.error("The request timed out. The server might be under heavy load.")

    except Exception as e:
        st.error(f"Unexpected error: {e}")
