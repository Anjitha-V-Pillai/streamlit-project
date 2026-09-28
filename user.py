import streamlit as st

st.title("User Information Form")

# Form input fields
name = st.text_input("Name")
age = st.number_input("Age", min_value=0)
place = st.text_input("place")

gender = st.radio("Gender", ["Male", "Female", "Other"])

qualifications = st.selectbox("Qualifications", ["bca", "bba", "btech"])

# Submit button
if st.button("submit"):
    if name and place:
        st.success("Form submitted successfully!")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Place:** {place}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Qualification:** {qualifications}")
    else:
        st.warning("Please fill in all required fields.")