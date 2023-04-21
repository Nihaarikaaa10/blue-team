import streamlit as st

st.set_page_config(page_title="Welcome to Streamlit!")
st.header("Enter your details:")
name = st.text_input("Enter your name:")
place = st.text_input("Enter your place:")

if st.button("Submit"):
    st.write("Hello, ",name,"from ",place)