
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("final_churn_model.pkl")

st.title("Customer Churn Prediction and Retention Analytics")

st.write("Enter customer details to predict churn.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Female", "Male"])
tenure = st.number_input("Tenure (Months)", min_value=0, value=12)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-Month", "One-Year", "Two-Year"]
)

plan = st.selectbox(
    "Plan Type",
    ["Basic", "Premium", "Standard"]
)

usage = st.number_input("Monthly Usage Hours", min_value=0.0, value=40.0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=500.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=5000.0)

payment = st.selectbox(
    "Payment Method",
    ["Cash", "Credit Card", "Debit Card", "Net Banking", "UPI"]
)

complaints = st.number_input("Complaints", min_value=0, value=0)
support = st.number_input("Support Tickets", min_value=0, value=0)

if st.button("Predict Churn"):

    customer = pd.DataFrame({
        "Age": [age],
        "Tenure_Months": [tenure],
        "MonthlyUsageHours": [usage],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "Complaints": [complaints],
        "SupportTickets": [support],
        "Gender_Male": [1 if gender == "Male" else 0],
        "ContractType_One-Year": [1 if contract == "One-Year" else 0],
        "ContractType_Two-Year": [1 if contract == "Two-Year" else 0],
        "PlanType_Premium": [1 if plan == "Premium" else 0],
        "PlanType_Standard": [1 if plan == "Standard" else 0],
        "PaymentMethod_Credit Card": [1 if payment == "Credit Card" else 0],
        "PaymentMethod_Debit Card": [1 if payment == "Debit Card" else 0],
        "PaymentMethod_Net Banking": [1 if payment == "Net Banking" else 0],
        "PaymentMethod_UPI": [1 if payment == "UPI" else 0]
    })

    prediction = model.predict(customer)

    if prediction[0] == 1:
        st.error("Customer is likely to CHURN")
        st.warning("Recommended Retention Action: Offer Discount")
    else:
        st.success("Customer is NOT likely to CHURN")
        st.info("Recommended Retention Action: No Action")
