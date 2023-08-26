import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write(""" At Omar's Coding Academy our mission is too create a world for programmers that is coder friendly and fun. 
All of us had to start somewhere when starting our journey into the programming world. It can be quite intimidating to
say the least. Where do I start? How do I start? all of these questions can be daunting especially for beginners. 
For those reasons here at Omar's Coding Academy we want all programmers regardless of skill level to feel welcomed in a 
community that is ready to support and aid all individuals looking to make a transition in to the tech world. 
Looking forward to you joining us!
""")

st.subheader("Our Fantastic Team")

col1, col2, col3 = st.columns(3)

db = pandas.read_csv("Company website project data.csv")

with col1:
    for index, row in db[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in db[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in db[8:12].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])







