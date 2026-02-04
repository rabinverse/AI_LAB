import streamlit as st
import joblib

st.title("समाचार वर्गीकरण प्रणाली")

model = joblib.load("nepali_news_category_predictor.joblib")
st.markdown(
    """पूर्वानुमान गरिने समाचारका वर्गहरू : :orange['विचार', 'देश', 'खेलकुद', 'मनोरञ्जन', 'प्रवास', 'साहित्य',
       'सूचना प्रविधि', 'स्वास्थ्य', 'विश्व']"""
)
st.divider()
user_input = st.text_area("यहाँ समाचार लेख्नुहोस्:")
st.divider()
if st.button("पूर्वानुमान गर्नुहोस्"):
    output = model.predict([user_input])[0]
    st.success(f" यो समाचारको वर्ग :violet[\n{output}] हो")
