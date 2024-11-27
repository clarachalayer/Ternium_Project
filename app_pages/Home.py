import streamlit as st
import pandas as pd
import joblib

def main():
    st.image("images/logo.png", width=100)

    # Título y subtítulo
    st.header("Welcome to Seiketsu Plataform!")
    st.subheader('"Empowering businesses to achieve excellence through actionable insights and cutting-edge digital solutions."')
    st.write("This platform is designed to support process control and decision-making by leveraging data from hot rolling sensors. Our goal is to optimize processes, reduce defects on coils, and enhance operational efficiency.")

    # Carga de archivo
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file:
        # Leer el archivo cargado
        data = pd.read_csv(uploaded_file)

        # Mostrar los datos cargados en un formato estilizado
        st.write("Uploaded Data:")
        st.dataframe(data)  # Mejora la visualización de los datos

        # Definir las variables necesarias
        variables = [
            "Coil Thickness", "Deceleration", "Transfer Bar Thickness", "FM Final Speed", "STD Cycle Time",
            "Slab Thickness", "STD Rolling Time", "Slab Weight", "SSP Pacing Time", "1st Accel", "2nd Accel Time",
            "FCE Pacing Time", "Pacing CountDown Time", "SSP Width Tail Error", "Commander Slab Speed", "FDT",
            "FCE Waiting Time", "FM Thread Speed", "Transfer Bar Lenght", "SSP Width Head Error", "R1 Rolling Time",
            "PC Width", "PC Thickness", "Residence time in furnace Actual", "Discharge Temperature Actual Calculated",
            "Slab Width"
        ]

        # Verificar si todas las columnas requeridas están presentes
        if all(feature in data.columns for feature in variables):
            # Extraer las características
            input_features = data[variables]

            # Cargar el modelo pre-entrenado
            model = joblib.load("svc_model.pkl")

            # Hacer predicciones
            data['Prediction'] = model.predict(input_features)

            # Mostrar los resultados de las predicciones de una forma más visual
            st.write("Predictions:")
            st.dataframe(data[['Prediction']].style.applymap(lambda x: 'background-color: yellow' if x == 0 else 'background-color: lightgreen'))  # Colorear predicciones

        else:
            st.error("Please ensure the file contains the required columns.")

    # Footer
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
