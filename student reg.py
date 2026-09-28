import streamlit as st

st.title("Student Registration Form")

name = st.text_input("Name")
age = st.number_input("Age")
dob = st.date_input("DOB")
email = st.text_input("Email")
gender = st.radio("Gender", ["Male", "Female"])
courses = st.selectbox("Courses", ["python", "java", "dotnet", "testing"])

if st.button("Register"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"DOB: {dob}")
    st.write(f"Email: {email}")
    st.write(f"Gender: {gender}")
    st.write(f"Courses: {courses}")