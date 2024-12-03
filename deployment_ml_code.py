# -*- coding: utf-8 -*-
"""deployment ml code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cVIy2vuGiXnlGJMDN0-5H82D7fxG9nM5
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the model
try:
    cholera_model = pickle.load(open('cholera_model.sav', 'rb'))
    print(type(cholera_model))  # Print the type of the loaded model
except Exception as e:
    print(f"Error loading model: {e}")

# Check if the model has the predict method
if hasattr(cholera_model, 'predict'):
    print("The predict method exists.")
else:
    print("The predict method does not exist.")

# Function to predict case status based on user inputs
def predict_case(diarrhoea, vomiting, dehydration, abdominal_pain, headache, age):
    # Prepare input data for the model
    input_data = [[diarrhoea, vomiting, dehydration, abdominal_pain, headache, age]]
    
    # Use the model to make a prediction
    prediction = cholera_model.predict(input_data)

    # Return the case status as "Positive" or "Negative"
    if prediction[0] == 1:  # Assuming 1 means Positive
        return "Positive"
    else:
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



