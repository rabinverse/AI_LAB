import streamlit as st
import joblib


input = st.text_input("Enter 13 dim numbers").strip()
if st.button("Predict"):
    model = joblib.load("heart_disease_pred.joblib")
    features = [float(x) for x in input.split(",")]
    result = model.predict([features])[0]
    st.success(f"output: {result}")
    st.success(
        f"{'The person has disease' if result else 'The person doesnt has disease'}"
    )
