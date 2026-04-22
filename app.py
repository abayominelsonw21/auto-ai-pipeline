import streamlit as st
import joblib
import json
import pandas as pd

# 1. Load Artifacts (Optimized for Speed)
@st.cache_resource
def load_assets():
    model = joblib.load('universal_market_predictor.pkl')
    with open('make_model_mapping.json', 'r') as f:
        mapping = json.load(f)
    return model, mapping

model, make_model_mapping = load_assets()

# 2. Stealth Monochrome UI Styling
st.set_page_config(page_title="AutoMarket AI", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stButton>button { background-color: #ffffff; color: #000000; border-radius: 0px; font-weight: bold; width: 100%; }
    .stSelectbox, .stNumberInput { color: #ffffff; }
    h1, h2, h3 { color: #ffffff; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 AUTOMARKET AI")
st.subheader("Predictive Vehicle Valuation Microservice")
st.write("---")

# 3. Dynamic Inputs
col1, col2 = st.columns(2)

with col1:
    selected_make = st.selectbox("MAKE", options=sorted(make_model_mapping.keys()))

with col2:
    # Cascading dropdown logic
    available_models = sorted(make_model_mapping[selected_make])
    selected_model = st.selectbox("MODEL", options=available_models)
    available_bodies = sorted(make_model_mapping[selected_make][selected_model])
    body_style = st.selectbox("BODY STYLE", options=available_bodies)

mileage = st.number_input("MILEAGE", min_value=0, max_value=500000, value=45000)
vehicle_age = st.slider("VEHICLE AGE (YEARS)", 0, 30, 5)

st.write("---")

# 4. Prediction Execution
if st.button("RUN VALUATION ENGINE"):
    # Reconstruct input for XGBoost
    input_df = pd.DataFrame({
        'make': [selected_make],
        'model': [selected_model],
        'bodyStyle': [body_style],
        'mileage': [mileage],
        'vehicle_age': [vehicle_age]
    })
    
    # Cast to category as required by your trained model
    for col in ['make', 'model', 'bodyStyle']:
        input_df[col] = input_df[col].astype('category')
        
    prediction = model.predict(input_df)[0]
    
    st.markdown(f"### ESTIMATED VALUE: **${prediction:,.2f}**")