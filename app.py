import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# Load trained model
model = joblib.load("final_tuned_random_forest.pkl")

# Title
st.title("📊 Customer Churn Prediction")
st.caption(
    "Predict whether a customer is likely to churn based on their usage and account information."
)

st.divider()

# Customer information
st.subheader("👤 Customer Information")

# Input fields
call_failure = st.number_input(
    "Call Failure", min_value=0, value=5
)

complaints = st.number_input(
    "Complaints", min_value=0, value=0
)

subscription_length = st.number_input(
    "Subscription Length", min_value=0, value=12
)

charge_amount = st.number_input(
    "Charge Amount", min_value=0, value=20
)

seconds_of_use = st.number_input(
    "Seconds of Use", min_value=0, value=5000
)

frequency_of_use = st.number_input(
    "Frequency of use", min_value=0, value=50
)

frequency_of_sms = st.number_input(
    "Frequency of SMS", min_value=0, value=20
)

distinct_called_numbers = st.number_input(
    "Distinct Called Numbers", min_value=0, value=10
)

age_group = st.number_input(
    "Age Group", min_value=1, value=3
)

tariff_plan = st.number_input(
    "Tariff Plan", min_value=1, value=1
)

status = st.number_input(
    "Status", min_value=1, value=1
)

age = st.number_input(
    "Age", min_value=1, value=30
)

customer_value = st.number_input(
    "Customer Value", min_value=0.0, value=100.0
)

st.divider()

# Prediction
if st.button("🔮 Predict Churn", use_container_width=True):

    input_data = [[
        call_failure,
        complaints,
        subscription_length,
        charge_amount,
        seconds_of_use,
        frequency_of_use,
        frequency_of_sms,
        distinct_called_numbers,
        age_group,
        tariff_plan,
        status,
        age,
        customer_value
    ]]

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is unlikely to churn.")