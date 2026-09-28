import streamlit as st

st.title("Multiplication")
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

if st.button("Multiply"):
    st.success(f"Result: {num1 * num2}")