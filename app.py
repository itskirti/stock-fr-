import streamlit as st
import requests
import numpy as np

# Streamlit UI
st.title("Stock Price Prediction App 📈")
st.markdown("Predict the next day's closing price based on the latest stock data.")

# Input fields for user to enter stock features
st.sidebar.header("Enter today's stock details:")
open_price = st.sidebar.number_input("Open Price", min_value=0.0, format="%.2f")
high_price = st.sidebar.number_input("High Price", min_value=0.0, format="%.2f")
low_price = st.sidebar.number_input("Low Price", min_value=0.0, format="%.2f")
volume = st.sidebar.number_input("Volume", min_value=0.0, format="%.0f")
close_price = st.sidebar.number_input("Close Price", min_value=0.0, format="%.2f")

if st.sidebar.button("Predict"):  # Predict button
    user_features = [open_price, high_price, low_price, volume, close_price]
    api_url = "https://stock-backend-baxo.onrender.com/predict"  # Update if hosted externally

    try:
        response = requests.post(api_url, json={"features": user_features})
        if response.status_code == 200:
            prediction = response.json().get("predicted_close_price")
            st.success(f"Predicted Closing Price: ${prediction:.2f}")
        else:
            st.error("Error: " + response.json().get("error", "Unknown error"))
    except requests.exceptions.RequestException as e:
        st.error("Failed to connect to API. Make sure FastAPI is running.")
        st.error(str(e))

