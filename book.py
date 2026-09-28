import streamlit as st

st.title("Add New Book Record")

t = st.text_input("Title")
a = st.text_input("Author")
p = st.number_input("Price", min_value=0.0, step=1.0)
pg = st.number_input("Pages", min_value=1, step=1)
l = st.text_input("Language")

btn = st.button("Add Book")

if btn:
    if t and a:
        st.success("Book added successfully!")
        st.write(f"**Title:** {t}")
        st.write(f"**Author:** {a}")
        st.write(f"**Price:** {p}")
        st.write(f"**Pages:** {pg}")
        st.write(f"**Language:** {l}")
    else:
        st.warning("Please enter Title and Author.")