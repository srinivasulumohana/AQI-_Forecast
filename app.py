# =========================================================
# FINAL AQI FORECAST DASHBOARD
# =========================================================

import streamlit as st
import pandas as pd
import joblib
import os
from PIL import Image

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(

    page_title="AQI Forecast Dashboard",

    layout="wide"

)

# =========================================================
# TITLE
# =========================================================

st.title("🌫️ AQI Forecast Dashboard")

st.write(
    "Machine Learning Based Air Quality Prediction System"
)

# =========================================================
# LOAD MODEL
# =========================================================

MODEL_PATH = "models/best_aqi_model.pkl"

if not os.path.exists(MODEL_PATH):

    st.error(
        "Model not found! Run advanced_aqi_forecast.py first."
    )

    st.stop()

model = joblib.load(MODEL_PATH)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(

    "Select Page",

    [

        "Prediction",

        "Visualizations"

    ]

)

# =========================================================
# PREDICTION PAGE
# =========================================================

if page == "Prediction":

    st.header("AQI Prediction System")

    pm25 = st.number_input(
        "PM2.5",
        value=50.0
    )

    pm10 = st.number_input(
        "PM10",
        value=80.0
    )

    co = st.number_input(
        "CO",
        value=1.0
    )

    no2 = st.number_input(
        "NO2",
        value=30.0
    )

    so2 = st.number_input(
        "SO2",
        value=20.0
    )

    o3 = st.number_input(
        "O3",
        value=40.0
    )

    temperature = st.number_input(
        "Temperature",
        value=30.0
    )

    humidity = st.number_input(
        "Humidity",
        value=60.0
    )

    wind_speed = st.number_input(
        "Wind Speed",
        value=5.0
    )

    pressure = st.number_input(
        "Pressure",
        value=1013.0
    )

    cloud_cover = st.number_input(
        "Cloud Cover",
        value=50.0
    )

    if st.button("Predict AQI"):

        input_data = pd.DataFrame([{

            "PM2_5_ugm3": pm25,
            "PM10_ugm3": pm10,
            "CO_ugm3": co,
            "NO2_ugm3": no2,
            "SO2_ugm3": so2,
            "O3_ugm3": o3,
            "Temp_2m_C": temperature,
            "Humidity_Percent": humidity,
            "Wind_Speed_10m_kmh": wind_speed,
            "Pressure_MSL_hPa": pressure,
            "Cloud_Cover_Percent": cloud_cover

        }])

        prediction = model.predict(input_data)[0]

        st.success(
            f"Predicted AQI: {round(prediction, 2)}"
        )

        # AQI CATEGORY

        if prediction <= 50:

            st.success("Air Quality: GOOD")

        elif prediction <= 100:

            st.info("Air Quality: SATISFACTORY")

        elif prediction <= 200:

            st.warning("Air Quality: MODERATE")

        elif prediction <= 300:

            st.warning("Air Quality: POOR")

        else:

            st.error("Air Quality: VERY POOR / SEVERE")

# =========================================================
# VISUALIZATION PAGE
# =========================================================

if page == "Visualizations":

    st.header("Advanced AQI Visualizations")

    visualization_files = [

        "model_comparison.png",

        "heatmap.png",

        "aqi_distribution.png",

        "feature_importance.png",

        "prediction_vs_actual.png"

    ]

    for file in visualization_files:

        path = os.path.join(
            "visualizations",
            file
        )

        if os.path.exists(path):

            image = Image.open(path)

            st.image(

                image,

                caption=file,

                use_container_width=True

            )

# =========================================================
# FOOTER
# =========================================================

st.write("---")

st.write(
    "Developed using Python, Machine Learning & Streamlit"
)
