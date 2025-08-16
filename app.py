# app.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Set page config
st.set_page_config(
    page_title="📦 Warehouse Sales Predictor",
    page_icon="📦",
    layout="centered"
)

# Load model and scaler
@st.cache_resource
def load_model():
    try:
        model = joblib.load('best_model_random_forest.pkl')
        scaler = joblib.load('scaler.pkl')
        st.success("✅ Model and scaler loaded successfully!")
        return model, scaler
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None, None

model, scaler = load_model()

# Title and description
st.title("📦 Warehouse Sales Predictor")
st.markdown("Enter retail details below to predict warehouse sales.")

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        retail_sales = st.number_input("Retail Sales ($)", min_value=0.0, step=10.0)
        year = st.number_input("Year", min_value=2000, max_value=2100, step=1)

    with col2:
        retail_transfers = st.number_input("Retail Transfers", min_value=0, step=1)
        month = st.number_input("Month (1–12)", min_value=1, max_value=12, step=1)

    submitted = st.form_submit_button("🔮 Predict Warehouse Sales")

# Make prediction
if submitted and model is not None:
    try:
        # Prepare input data
        num_cols = ['RETAIL SALES', 'RETAIL TRANSFERS', 'YEAR', 'MONTH']
        input_data = np.array([[retail_sales, retail_transfers, year, month]])

        # Scale numerical features
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)[0]

        # Display result
        st.success(f"Predicted Warehouse Sales: **${prediction:,.2f}**")

        # Optional: Show feature importance (if available)
        with st.expander("📊 Model Insight"):
            st.write("Random Forest was used for prediction.")
            st.write(f"Input: Retail Sales=${retail_sales}, Transfers={retail_transfers}, Time={year}-{month:02d}")

    except Exception as e:
        st.error(f"Prediction error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("💡 Built with [Streamlit](https://streamlit.io) | 🧠 Random Forest Model")