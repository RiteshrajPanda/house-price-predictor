# app.py
import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the preprocessor and model
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title
st.title("🏠 Rental Price Prediction App")

# User input form
st.subheader("Enter Property Details")

# City input
city = st.selectbox("City", ['Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'])

# Area Type input
area_type = st.selectbox("Area Type", ['Carpet Area', 'Super Area', 'Built Area'])

# Furnishing status input
furnishing = st.selectbox("Furnishing Status", ['Furnished', 'Semi-Furnished', 'Unfurnished'])

# Numeric inputs
size = st.number_input("Size (sqft)", min_value=100, max_value=10000, value=1000)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, value=2)
bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
floor_level = st.number_input("Floor Level", min_value=-2, max_value=100, value=1)
total_floors = st.number_input("Total Floors", min_value=1, max_value=100, value=5)
posted_month = st.number_input("Posted Month", min_value=1, max_value=12, value=5)
posted_year = st.number_input("Posted Year", min_value=2000, max_value=2100, value=2025)

# Tenant preferences
tenant_bachelors = st.checkbox("Preferred for Bachelors?")
tenant_family = st.checkbox("Preferred for Family?")

# Predict button
if st.button("Predict Rent"):
    # Create input DataFrame
    input_dict = {
        'Size': [size],
        'BHK': [bhk],
        'Bathroom': [bathroom],
        'Floor_Level': [floor_level],
        'Total_Floors': [total_floors],
        'Posted_Month': [posted_month],
        'Posted_Year': [posted_year],
        'Tenant_Bachelors': [int(tenant_bachelors)],
        'Tenant_Family': [int(tenant_family)],
        'Area Type': [area_type],
        'City': [city],
        'Furnishing Status': [furnishing],
    }
    input_df = pd.DataFrame(input_dict)

    # Preprocess input
    processed_df = preprocessor.transform(input_df)

    # Predict
    prediction = model.predict(processed_df)[0]
    st.success(f"Estimated Monthly Rent: ₹{int(prediction):,}")
