import streamlit as st
import pandas as pd
import joblib

# PAGE CONFIG

st.set_page_config(
    page_title="Electric Vehicle Range Predictor",
    page_icon="⚡",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* Background image */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1605559424843-9e4f3e5a98a6");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Add dark overlay for readability */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.45); /* adjust transparency here */
        z-index: 0;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
    }

    /* Title styling */
    h1 {
        color: #00e6ac;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 2.2em;
    }

    /* Text and widgets */
    .stNumberInput label {
        color: white !important;
    }

    .stButton>button {
        background-color: #00e6ac;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }

    .stSuccess {
        background-color: rgba(0, 230, 172, 0.1);
        border-left: 4px solid #00e6ac;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# SIDEBAR CONTENT

st.sidebar.write(
    "Experience the future of driving — where range meets performance and elegance."
)

# LOAD MODEL
model = joblib.load('ev_range_predictor.pkl')

# MAIN TITLE

st.title("⚡ Electric Vehicle Range Prediction Dashboard")
st.write("Enter vehicle specifications below to predict the estimated range (in km).")

# INPUT FIELDS

col1, col2, col3 = st.columns(3)

with col1:
    battery_capacity = st.number_input("🔋 Battery Capacity (kWh)", min_value=10.0, max_value=200.0)
    efficiency = st.number_input("⚡ Efficiency (Wh/km)", min_value=100.0, max_value=400.0)

with col2:
    top_speed = st.number_input("🚗 Top Speed (km/h)", min_value=50.0, max_value=400.0)
    acceleration = st.number_input("⏱️ 0–100 km/h Acceleration (s)", min_value=2.0, max_value=15.0)

with col3:
    charging_power = st.number_input("🔌 Fast Charging Power (kW)", min_value=20.0, max_value=400.0)
    torque = st.number_input("🌀 Torque (Nm)", min_value=50.0, max_value=1500.0)


# PREDICTION

if st.button("🚀 Predict Range"):
    input_data = pd.DataFrame(
        [[battery_capacity, top_speed, efficiency, acceleration, charging_power, torque]],
        columns=[
            'battery_capacity_kWh', 'top_speed_kmh', 'efficiency_wh_per_km',
            'acceleration_0_100_s', 'fast_charging_power_kw_dc', 'torque_nm'
        ]
    )

    prediction = model.predict(input_data)[0]
    st.success(f"✅ **Estimated Range:** {prediction:.2f} km")
    st.balloons()
