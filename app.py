import streamlit as st
import os
st.title("Discipline and movitated")
st.header("wallpaper")
name=st.text_input("enter your name")
age=st.number_input("enter your age",min_value=18,max_value=100,step=5)
st.write(f"name{name} your age is {age}")
gender=st.selectbox("select your gender",["Male","Female"])
subject=st.multiselect("select your choice",["Python","java","c++","mysql"])
login=st.button("login")

if login:
    st.success("submitted sucessfully")
    st.write(name)
    st.write(age)
    st.write(gender)
    st.write(subject)

st.divider()
st.image(r"C:\Users\USER\Desktop\download.jpg")
st.image(os.path.join(os.getcwd(),"static","shahid_hamid.jpeg"))
