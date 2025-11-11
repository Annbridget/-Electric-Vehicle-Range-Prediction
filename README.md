⚡ # Electric Vehicle Range Prediction App 🚗🔋
 # Overview

The Electric Vehicle Range Prediction App is an interactive Streamlit web application that uses machine learning to predict the estimated driving range of electric vehicles (EVs).
By analyzing vehicle specifications such as battery capacity, weight, motor power, and efficiency, the app provides a real-time estimate of how far an EV can travel on a single charge.

# Project Objective

The goal of this project is to build a machine learning model that accurately predicts the range (in kilometers or miles) of electric vehicles based on technical parameters.
It is designed to help:
 Manufacturers evaluate prototype designs
 Researchers explore performance trends
 Consumers compare EV options

 # Machine Learning Model

Model Used: Linear Regression
Framework: Scikit-learn
Target Variable: Electric Vehicle Range
Input Features: 'battery_capacity_kWh', 'top_speed_kmh', 'efficiency_wh_per_km', 
            'acceleration_0_100_s', 'fast_charging_power_kw_dc', 'torque_nm'

The model was trained on cleaned EV dataset samples, serialized using joblib, and integrated into a Streamlit app for real-time prediction.

# Future Improvements
Add more advanced models (e.g., Random Forest, XGBoost)
Incorporate weather or terrain effects
Build an API for EV manufacturers to connect directly
Create a mobile-friendly interface

## Streamlit Link
https://annbridget--electric-vehicle-range-pre-ev-prediction-app-vddrdu.streamlit.app/
