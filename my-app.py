
import streamlit as st


st.title('🎈 Image to Text Converter  ')
st.write("We present an online OCR (Optical Character Recognition) service to extract text from image. Upload photo to our image to text converter, click on submit and get your text file instantly.")

## Upload file ##
#st.sidebar.header('Upload file')
#uploaded_file = st.sidebar.file_uploader("Choose a file", type=['png', 'jpg'])
st.image("abc.png")
st.markdown("----")
option = st.selectbox('Upload option',['select','Browse the image','Open the camera']) 
uploaded_file = None
#if st.button('Upload the image'):
col1,col2 = st.columns(2)
with col1:
    if option == 'Browse the image' :
        uploaded_file = st.file_uploader('Upload a photo',type=['png', 'jpg'])
        
    elif option == 'Open the camera' :
        #if st.button('Take a photo'):
        uploaded_file = st.camera_input("Take a picture")
        if uploaded_file is not None:
          # To read image file buffer as bytes:
          bytes_data = uploaded_file.getvalue()
          # Check the type of bytes_data:
          # Should output: <class 'bytes'>
          #st.write(type(bytes_data))
with col2:
    if uploaded_file is not None:
        st.image(uploaded_file)
        st.subheader('Download the Text')
        st.button('Download')
st.markdown("----")