import streamlit as st
import time


st.balloons()

st.subheader("Progress bar")
st.progress(10)             # st.progress(10) creates a progress bar that is 10% complete.

st.subheader("Wait for execution")
with st.spinner('Wait for it...'):  
      time.sleep(10)

      st.success("You did it !")
      st.error("Error")
      #st.warnig("Warning")
      st.info("It's easy to build a streamlit app")
      st.exception(RuntimeError("RuntimeError exception"))