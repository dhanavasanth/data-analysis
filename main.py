import streamlit as st

st.title("welcome to my app...!")

name = st.text_input('enter your name..!')

if name is not None and st.button("click"):
    st.write(name)
else:
    st.write("please enter a valid name...!")

print("hello welcome all to this session")
