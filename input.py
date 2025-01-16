import streamlit as st

st.subheader("Hello ,Do you want to fill the form ?")
st.checkbox('yes')
st.checkbox('no')

st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your Language',['Tamil','Sinhala'])
st.multiselect('choose your Province',['North Central Province','Uva Province' , 'Northern Province' ,'South Province' , 'Central Province', 'North Western Province','Sabaragamuwa Province' , 'Eastern Province' ,  'Western Province' ])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.button('Submit')
