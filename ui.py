# ui.py
import streamlit as st
from app import predict_rent  # import the function from app.py

st.set_page_config(page_title="Rental Price Predictor")

st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #F2F0EF;
        color: #245F73;
    }

    /* Header */
    h1 {
        color: #733E24;
    }

    /* Paragraphs and labels */
    p, label, .stSelectbox, .stNumberInput, .stCheckbox {
        color: #245F73 !important;
    }

    /* Input backgrounds */
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"],
    .stCheckbox {
        background-color: white;
        color: #245F73;
        border: 1px solid #BBBDBC;
        border-radius: 6px;
    }

    /* Button styling */
    .stButton > button {
        background-color: #FFFFFF;  /* Black background */
        color: #000000;  /* Warm brown text */
        border: none;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #733E24;  /* Warm brown background on hover */
        color: #000000;  /* Black text on hover */
    }
    .stButton {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Metric styling */
    div[data-testid="stMetric"] {
        background-color: #245F73;
        color: white;
        padding: 1em;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Title & subtitle
st.markdown("<h1 style='text-align: center; color: #733E24;'>Rental Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #245F73;'>Enter the property details below to estimate monthly rent.</p>", unsafe_allow_html=True)


# Layout in two columns
col1, col2 = st.columns(2)

with col1:
    city = st.selectbox("City", ['Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'])
    area_type = st.selectbox("Area Type", ['Carpet Area', 'Super Area', 'Built Area'])
    furnishing = st.selectbox("Furnishing Status", ['Furnished', 'Semi-Furnished', 'Unfurnished'])
    posted_month = st.number_input("Posted Month", min_value=1, max_value=12, value=5)
    posted_year = st.number_input("Posted Year", min_value=2000, max_value=2100, value=2025)
    tenant_bachelors = st.checkbox("Preferred for Bachelors?")
    
    
    
with col2:
    size = st.number_input("Size (sqft)", min_value=100, max_value=10000, value=1000)
    bhk = st.number_input("Number of BHK", min_value=1, max_value=10, value=2)
    bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
    floor_level = st.number_input("Floor Level", min_value=-2, max_value=100, value=1)
    total_floors = st.number_input("Total Floors", min_value=1, max_value=100, value=5)
    tenant_family = st.checkbox("Preferred for Family?")

# Collect input
input_data = {
    'Size': size,
    'BHK': bhk,
    'Bathroom': bathroom,
    'Floor_Level': floor_level,
    'Total_Floors': total_floors,
    'Posted_Month': posted_month,
    'Posted_Year': posted_year,
    'Tenant_Bachelors': int(tenant_bachelors),
    'Tenant_Family': int(tenant_family),
    'Area Type': area_type,
    'City': city,
    'Furnishing Status': furnishing
}

# Predict on button click
if st.button("Predict Rent"):
    predicted_rent = predict_rent(input_data)
    st.metric(label="Estimated Monthly Rent", value=f"₹ {predicted_rent:,}")
