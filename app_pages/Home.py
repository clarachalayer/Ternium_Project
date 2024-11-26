import streamlit as st
import pandas as pd
import joblib
from sklearn.svm import SVC

def main():
    st.image("images/logo.png", width=100)
    st.header("Bienvenido a la página principal")
    st.write("Este es el contenido de la página Home.")

    st.header("Bienvenido.")
    st.write("Este es el contenido de la página Home.")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(data)

        # Define the required variables
        variables = [
            "Coil Thickness",
            "Deceleration",
            "Transfer Bar Thickness",
            "FM Final Speed",
            "STD Cycle Time",
            "Slab Thickness",
            "STD Rolling Time",
            "Slab Weight",
            "SSP Pacing Time",
            "1st Accel",
            "2nd Accel Time",
            "FCE Pacing Time",
            "Pacing CountDown Time",
            "SSP Width Tail Error",
            "Commander Slab Speed",
            "FDT",
            "FCE Waiting Time",
            "FM Thread Speed",
            "Transfer Bar Lenght",
            "SSP Width Head Error",
            "R1 Rolling Time",
            "PC Width",
            "PC Thickness",
            "Residence time in furnace Actual",
            "Discharge Temperature Actual Calculated",
            "Slab Width"
        ]

        # Check if all required features are in the uploaded file
        if all(feature in data.columns for feature in variables):
            # Extract features
            input_features = data[variables]

            # Load the pre-trained model
            model = joblib.load("svc_model.pkl")

            # Make predictions
            data['Prediction'] = model.predict(input_features)

            # Display results
            st.write("Predictions:")
            st.write(data[['Prediction']])
        else:
            st.error("Please ensure the file contains the required columns.")
            
        # Pie de página
    st.markdown(
        """
        <style>
        /* Footer fijo en la parte inferior */
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #000000;
            color: white;
            text-align: right;
            padding: 10px;
            font-size: 14px;
        }
        /* Ajuste del padding inferior para que no se superponga el contenido con el footer */
        .main > div {
            padding-bottom: 50px;
        }
        </style>
        <div class="footer">
            Seiketsu Consulting &copy; 2023
        </div>
        """,
        unsafe_allow_html=True
    )
