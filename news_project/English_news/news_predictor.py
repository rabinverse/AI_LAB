import streamlit as st
import joblib


model = joblib.load("english_news_category_predictor.joblib")

user_input = st.text_area("Enter the news to predict its category").strip()

if st.button("predict"):
    output = model.predict([user_input])[0]
    st.success(f"🙏\n{output}")
