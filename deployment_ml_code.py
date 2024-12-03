# -*- coding: utf-8 -*-
"""deployment ml code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cVIy2vuGiXnlGJMDN0-5H82D7fxG9nM5
"""

pip install streamlit_option_menu

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Load saved model
cholera_model = pickle.load(open('cholera_model.sav', 'rb'))

import streamlit as st
from streamlit_option_menu import option_menu

# Function to predict case status based on user inputs
def predict_case(diarrhoea, vomiting, dehydration, abdominal_pain, headache, age):
    # Dummy prediction logic for demonstration
    # Replace this with your actual model's prediction logic
    if diarrhoea and vomiting and dehydration:
        return "Positive"
    return "Negative"

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Disease Prediction',
                            ['Cholera Prediction'],
                            icons=['biohazard'],
                            menu_icon='cast',
                            default_index=0)

# Main content based on selection
if selected == 'Cholera Prediction':
    st.title('Cholera Prediction Model')
    st.write('Please input the following details to predict the case status.')

    # User inputs
    diarrhoea = st.checkbox('Diarrhoea')
    vomiting = st.checkbox('Vomiting')
    dehydration = st.checkbox('Dehydration')
    abdominal_pain = st.checkbox('Abdominal Pain/Cramps')
    headache = st.checkbox('Headache')
    age = st.number_input('Age', min_value=0, max_value=120)

    # Button to predict case status
    if st.button('Predict Case Status'):
        case_status = predict_case(diarrhoea, vomiting, dehydration, abdominal_pain, headache, age)
        st.success(f'Case Status: {case_status}')



