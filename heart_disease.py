import streamlit as st
import pandas as pd
import joblib

model=joblib.load(r"C:\Users\l480\OneDrive\Desktop\ML Work\heart_disease.pkl")
expected_cols=joblib.load(r"C:\Users\l480\OneDrive\Desktop\ML Work\columns.pkl")
st.title("❤️ Heart Disease Prediction App")
st.markdown("Provide patient details:")
age = st.number_input("Age",18,100,40)
sex = st.selectbox("Sex", ['M','F'])
chest_pain = st.selectbox("Chest Pain Type",['ATA','NAP','TA','ASY'])
resting_bp = st.number_input("Resting Blood Pressure(mm Hg)",80,200,120)
cholesterol = st.number_input("Cholesterol(mg/dL)",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar >120mg/dL", [0, 1])
resting_ecg=st.selectbox("Resting ECG",["Normal","ST","LVH"])
max_hr = st.slider("Max Heart Rate",60,220,150)
exercise_angina = st.selectbox("Exercise Angina", ["Y","N"])
oldpeak = st.slider("Oldpeak (ST depression)",0.0,6.0,1.0)
St_slope=st.selectbox("ST Slope",['Up', 'Flat', 'Down'])

if st.button("Predict"):
    raw_input={
        'Age':age,
        'RestingBP':resting_bp,
        'Cholesterol':cholesterol,
        'FastingBS':fasting_bs,
        'MaxHR':max_hr,
        'OldPeak':oldpeak,
        'Sex_'+sex:1,
        'ChestPainType_'+chest_pain:1,
        'RestingECG_'+resting_ecg:1,
        'ExerciseAngina_'+exercise_angina:1,
        'ST_Slope_'+St_slope:1
    }
    input_df=pd.DataFrame([raw_input])
    for col in expected_cols:
        if col not in input_df.columns:
            input_df[col]=0
    input_df=input_df[expected_cols]
    prediction=model.predict(input_df)
    if prediction[0]==1:
        st.error("Risk of having heart disease")
    else:
        st.success("No risk of heart disease")