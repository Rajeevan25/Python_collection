import streamlit as st
 
st.sidebar.title("allowing users to focus on the content in your app.")
st.sidebar.button("Enter")

container = st.container()
container.write("in the container")
st.title("out side the container")

