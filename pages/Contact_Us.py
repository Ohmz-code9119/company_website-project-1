import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("Company website project topics.csv")

st.header("Contact Us")

with st.form(key="send emails"):
    user_email = st.text_input("Your email address")
    topic_selection = st.selectbox("Choose a topic", df["topic"])
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: Questions from company website 

From: {user_email}
Topic: {topic_selection}
{raw_message} 
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
