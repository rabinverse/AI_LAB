import streamlit as st
import joblib
import re

st.title("समाचार वर्गीकरण प्रणाली")

model = joblib.load("nepali_news_category_predictor.joblib")
st.markdown(
    """पूर्वानुमान गरिने समाचारका वर्गहरू : :orange['विचार', 'देश', 'खेलकुद', 'मनोरञ्जन', 'प्रवास', 'साहित्य',
       'सूचना प्रविधि', 'स्वास्थ्य', 'विश्व']"""
)
st.divider()
user_input = st.text_area("यहाँ समाचारको अनुच्छेद पेस्ट गर्नुहोस्:").strip()
st.divider()
if st.button("पूर्वानुमान गर्नुहोस्"):
    if re.search(r"[\u0900-\u097F]", user_input):
        output = model.predict([user_input])[0]
        st.success(f"यो समाचारको वर्ग :violet[{output}] हो")
    else:
        st.error("This supports Nepali news only")
