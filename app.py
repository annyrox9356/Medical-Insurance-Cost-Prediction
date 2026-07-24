import streamlit as st
import pickle
import numpy as np

# 1. Model load karna
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# 2. Web App ka UI
st.title("Medical Insurance Cost Predictor 🏥")
st.write("Yeh meri pehli Machine Learning Web App hai!")

st.header("Apni Details Daaliye:")

# 6 Inputs (Original dataset ke hisaab se)
age = st.number_input("Enter your Age", min_value=18, max_value=100, value=25)
gender = st.selectbox("Select Gender", ["Male", "Female"])
bmi = st.number_input("Enter your BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Are you a Smoker?", ["Yes", "No"])
region = st.selectbox("Select Region", ["southwest", "southeast", "northwest", "northeast"])

# 3. Prediction Logic
if st.button("Predict Cost"):
    
    # Encoding: Gender (Male=1, Female=0)
    sex_num = 1 if gender == "Male" else 0
    
    # Encoding: Smoker (Yes=1, No=0)
    smoker_num = 1 if smoker == "Yes" else 0
    
    # Encoding: Region (One-Hot Encoding format)
    # Default sabko 0 rakhte hain
    region_nw = 0
    region_se = 0
    region_sw = 0
    
    # Jo region select hoga, usko 1 kar denge
    if region == "northwest":
        region_nw = 1
    elif region == "southeast":
        region_se = 1
    elif region == "southwest":
        region_sw = 1
    # Agar northeast select hua, toh teeno 0 rahenge (kyunki notebook mein drop='first' use hua tha)

    # 8 features ka array banayenge, EXACT usi order mein jisme model train hua tha
    # Order: [northwest, southeast, southwest, age, sex, bmi, children, smoker]
    input_features = np.array([[region_nw, region_se, region_sw, age, sex_num, bmi, children, smoker_num]])
    
    # Prediction calculate karna
    prediction = model.predict(input_features)
    
    # Result print karna
    st.success(f"Aapki estimated medical cost hai: ${prediction[0]:.2f}")