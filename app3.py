import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
with open("housePrice.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

st.write("Fill in the house details below to predict the price in ₹.")

# Input fields
location = st.selectbox("Location", ["HSR Layout", "Koramangala", "Whitefield", "Marathahalli"])  # Use your dataset's unique values
condition = st.selectbox("Condition", ["Good", "Average", "Poor"])
size = st.number_input("Size (sqft)", min_value=300.0, max_value=10000.0, step=10.0, value=1200.0)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1, value=2)
bathrooms = st.number_input("Number of Bathrooms", min_value=1.0, max_value=10.0, step=0.5, value=2.0)
year_built = st.number_input("Year Built", min_value=1950, max_value=2025, step=1, value=2000)
garage = st.selectbox("Garage Available?", [1, 0])

# Prediction
if st.button("Predict House Price"):
    # Create input DataFrame
    input_data = pd.DataFrame([[location, condition, size, bedrooms, bathrooms, year_built, garage]],
                              columns=["Location", "Condition", "Size (sqft)", "Bedrooms", "Bathrooms", "YearBuilt", "Garage"])
    try:
        result = model.predict(input_data)
        st.success(f"🏷️ Predicted House Price: ₹ {int(result[0]):,}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")