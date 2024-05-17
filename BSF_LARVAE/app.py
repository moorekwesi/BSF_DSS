#import the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import base64
import joblib

st.set_page_config(page_title="BSF_LARVAE!!!",page_icon=":bar_chart",layout="wide")
# Load your pretrained model
model = joblib.load('./rf_model.pkl')

#Create two columns, one for the image and one for the title
header_col1, header_col2=st.columns([1,3])
#Display the logo 
with header_col1:
    st.image('icipe.png', width=200)
#display the title in the second column
with header_col2:
    st.title('Fertilizer Production Prediction App')

st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

# Sidebar
# Define custom CSS to create buttons with equal width

st.sidebar.title('Home')
home_button=st.sidebar.button('Home', key='home')
about_us_link = st.sidebar.button('About Us', key='about')
contact_us_link = st.sidebar.button('Contact Us',key='contact')

# Main content
if contact_us_link:
    st.write("<span style='color:#6F4E37;'>http://www.icipe.org/research/research-support-units/data-management-modelling-and-geo-information-dmmg-unit</span><br>"
        "<span style='color:#FAFAFA;'>+254 783675297 or WhatsApp: +905057833251.</span>", unsafe_allow_html=True)
elif about_us_link:
    st.write("<span style='color:#FAFAFA;'>As students at PAUSTI and researchers at icipe, we specialize in data management modeling and geo-information, employing mathematical tools, machine learning, artificial intelligence, and IoT technology to tackle real-world challenges. Our interdisciplinary approach enables us to analyze complex datasets, monitor environmental conditions, and develop innovative solutions. Through our collaborative efforts, we are committed to driving positive change and advancing scientific knowledge for the betterment of society.</span>", unsafe_allow_html=True)
else:
    st.write("<div style='text-align: center;'><span style='color:#FAFAFA'></span></div>", unsafe_allow_html=True)
#Streamlit UI
st.sidebar.header('User Inputs')
#change the color of sidebar
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #B2D3C2; /* Change this color to your desired color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

#define the user inputs
Relative_Humidity= st.sidebar.number_input('Enter Humidity (%)',min_value=28.0,max_value=50.0, value=28.0, step=0.1)
Air_Temperature= st.sidebar.number_input('Enter Air Temperature',min_value=25.0,max_value=55.0, value=25.0, step=0.1)
Moisture= st.sidebar.number_input('Enter Moisture Content(%)',min_value=26.0,max_value=150.0, value=30.0, step=0.1)
Sub_Temperature= st.sidebar.number_input('Enter Substrate Temperature',min_value=25.0,max_value=50.0, value=25.0, step=0.1)

#prediction button
if st.sidebar.button('Predict'):
    input_data=np.array([[Relative_Humidity,Air_Temperature,Moisture,Sub_Temperature]])
    prediction=model.predict(input_data)
    st.write('Nitrogen-Phosphorus-Potassium (mg/kg):',prediction)
#B2D3C2
#Footer
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #262730;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            margin: 0 10px;
        }
    </style>
    <div class="footer">
        <p>Trademark © icipe. All rights reserved.</p>
        <p>Follow us on <a href="https://twitter.com/malontema79189" target="_blank">Twitter</a>, 
        <a href="https://www.instagram.com/sonexcellencek/" target="_blank">Instagram</a>, and 
        <a href="https://www.linkedin.com/in/malontema-katchali-103326205" target="_blank">LinkedIn</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
