import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("delivery_time_model.joblib")

st.title("📦 Food Delivery Time Prediction")
st.write("Enter order details below to predict delivery time.")

# Input fields
age = st.number_input("Delivery Person Age", min_value=18, max_value=65, value=25)
rating = st.number_input("Delivery Person Rating", min_value=0.0, max_value=5.0, value=4.5, step=0.1)
distance = st.number_input("Distance (km)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)

weather = st.selectbox("Weather Conditions", ["Sunny", "Stormy", "Cloudy", "Fog", "Sandstorms", "Windy"])
traffic = st.selectbox("Road Traffic Density", ["Low", "Medium", "High", "Jam"])
order_type = st.selectbox("Type of Order", ["Snack", "Drinks", "Buffet", "Meal"])
festival = st.selectbox("Festival", ["Yes", "No"])
city = st.selectbox("City", ["Urban", "Semi-Urban", "Metropolitan"])
multiple_deliveries = st.number_input("Multiple Deliveries", min_value=0, max_value=5, value=0)

# Prepare input for prediction
input_df = pd.DataFrame({
    'Delivery_person_Age': [age],
    'Delivery_person_Ratings': [rating],
    'distance_km': [distance],
    'Weatherconditions': [weather],
    'Road_traffic_density': [traffic],
    'Type_of_order': [order_type],
    'Festival': [festival],
    'City': [city],
    'multiple_deliveries': [multiple_deliveries]
})

# Predict button
if st.button("Predict Delivery Time"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Delivery Time: {prediction:.2f} minutes")
