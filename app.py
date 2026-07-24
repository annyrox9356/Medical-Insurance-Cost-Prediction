import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Web App UI
st.title("Medical Insurance Cost Predictor 🏥")
st.write("Yeh meri pehli Machine Learning Web App hai!")

st.header("Apni Details Daaliye:")

# Input fields
age = st.number_input("Enter your Age", min_value=18, max_value=100, value=25)
gender = st.selectbox("Select Gender", ["Male", "Female"])
bmi = st.number_input("Enter your BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Are you a Smoker?", ["Yes", "No"])
region = st.selectbox("Select Region", ["southwest", "southeast", "northwest", "northeast"])

# Prediction
if st.button("Predict Cost"):
    
    # Encode categorical variables
    sex_num = 1 if gender == "Male" else 0
    smoker_num = 1 if smoker == "Yes" else 0

    # One-Hot Encoding for region
    region_nw = 0
    region_se = 0
    region_sw = 0

    if region == "northwest":
        region_nw = 1
    elif region == "southeast":
        region_se = 1
    elif region == "southwest":
        region_sw = 1

    # Create input features in the same order as the training data
    # Order: [northwest, southeast, southwest, age, sex, bmi, children, smoker]
    input_features = np.array([[region_nw, region_se, region_sw, age, sex_num, bmi, children, smoker_num]])

    # Make prediction
    prediction = model.predict(input_features)

    # Display result
    st.success(f"Aapki estimated medical cost hai: ${prediction[0]:.2f}")
