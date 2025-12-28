import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Page Configuration

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="centered"
)


# Load Model Assets

model = joblib.load("models/churn_xgboost_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")

# Sidebar

st.sidebar.title("📌 About")
st.sidebar.markdown()

st.sidebar.markdown("---")
st.sidebar.write("🔍 Enter customer details")
st.sidebar.write("📊 Get churn probability")
st.sidebar.write("🎯 Take retention action")

# Main Title

st.title("📉 Customer Churn Prediction System")
st.markdown()

st.divider()

# -------------------------------
# Customer Inputs
# -------------------------------
st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly_charges = st.slider("Monthly Charges", 20, 120, 70)

with col2:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )
    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

st.subheader("💳 Billing Details")

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

st.info(
    "ℹ️ Tip: Customers with **short tenure** and **high monthly charges** "
    "have a higher probability of churn."
)

st.divider()


# Feature Engineering

avg_monthly = total_charges / (tenure + 1)

# Create input dictionary with all features = 0
input_dict = {feature: 0 for feature in feature_names}

# Assign numerical features
input_dict["tenure"] = tenure
input_dict["MonthlyCharges"] = monthly_charges
input_dict["TotalCharges"] = total_charges
input_dict["AvgMonthlyCharges"] = avg_monthly

# Contract encoding
if contract == "One year":
    input_dict["Contract_One year"] = 1
elif contract == "Two year":
    input_dict["Contract_Two year"] = 1

# Payment method encoding
if payment_method == "Electronic check":
    input_dict["PaymentMethod_Electronic check"] = 1
elif payment_method == "Mailed check":
    input_dict["PaymentMethod_Mailed check"] = 1
elif payment_method == "Bank transfer (automatic)":
    input_dict["PaymentMethod_Bank transfer (automatic)"] = 1
elif payment_method == "Credit card (automatic)":
    input_dict["PaymentMethod_Credit card (automatic)"] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Scale input
input_scaled = scaler.transform(input_df)


# Prediction Button

predict_button = st.button("🔍 Predict Churn Risk", use_container_width=True)

# Prediction Output
if predict_button:
    probability = model.predict_proba(input_scaled)[0][1]

    if probability >= 0.7:
        risk_level = "🔴 High Risk"
        color = "red"
    elif probability >= 0.4:
        risk_level = "🟠 Medium Risk"
        color = "orange"
    else:
        risk_level = "🟢 Low Risk"
        color = "green"

    st.subheader("📊 Prediction Result")

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )

    st.markdown(
        f"""
        <h3 style="color:{color};">
            Risk Level: {risk_level}
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown()
