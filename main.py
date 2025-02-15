import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Smart Calorie Burn Predictor",
                   layout="wide",
                   page_icon="🔥")

# Load the trained model
model_path = "/Users/pranshugarg/Desktop/calories_model.sav"
with open(model_path, "rb") as file:
    calorie_model = pickle.load(file)

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Calorie Burn Estimator',
                           ['Predict Calories Burned'],
                           menu_icon='fire',
                           icons=['activity'],
                           default_index=0)

# Calorie Prediction Page
if selected == 'Predict Calories Burned':

    # Page title
    st.title("🔥 Smart Calorie Burn Predictor")
    st.write("Estimate your calorie burn based on your body metrics and workout details.")

    # User input form
    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.selectbox('Gender', ['Male', 'Female'])
        Age = st.number_input('Age', min_value=10, max_value=100, step=1)
        Height = st.number_input('Height (cm)', min_value=100.0, max_value=250.0, step=0.1)

    with col2:
        Weight = st.number_input('Weight (kg)', min_value=30.0, max_value=200.0, step=0.1)
        Duration = st.number_input('Exercise Duration (min)', min_value=1, max_value=300, step=1)
        Heart_Rate = st.number_input('Heart Rate (bpm)', min_value=40, max_value=200, step=1)

    with col3:
        Body_Temp = st.number_input('Body Temperature (°C)', min_value=35.0, max_value=42.0, step=0.1)

    # Convert gender to numeric value
    Gender = 0 if Gender == 'Male' else 1

    # Prepare input for model
    user_input = [[Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]]

    # Prediction button
    if st.button("🔍 Predict Calories Burned"):
        prediction = calorie_model.predict(user_input)
        st.success(f'🔥 Estimated Calories Burned: **{prediction[0]:.2f} kcal**')
