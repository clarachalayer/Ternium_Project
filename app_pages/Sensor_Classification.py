import streamlit as st
import pandas as pd

def main():
    st.image("images/logo.png", width=100)
    
    # Cargar los datos previamente cargados
    file_path = 'datasets/evaluated_data.csv'  # Asegúrate de que la ruta del archivo sea correcta
    df = pd.read_csv(file_path)

    # Título de la aplicación
    st.title("Mahalanobis Distance for sensor's Classification")

    # Mostrar el conjunto de datos
    st.write("""
    ### Data Overview

    Here is the dataset containing information about different materials and sensor data. The material output is pre-classified as either "Approved" or "Defective" based on quality standards.

    """)
    st.dataframe(df)

    # Explicación de la Distancia de Mahalanobis
    st.write("""
    ### Mahalanobis Distance Explanation

    The **Mahalanobis distance** is a measure of the distance between a point and a distribution in a multivariate space. Unlike the Euclidean distance, which measures straight-line distances, the Mahalanobis distance takes into account correlations of the data set and the variance of each variable. 

    #### Why Mahalanobis Distance?

    - **Ideal for detecting anomalies**, like faulty sensors in a production environment.
    - It measures how far a sensor’s values are from an “expected pattern,” considering:
        - The **relationships between variables** (e.g., temperature, pressure, etc.).
        - The **expected dispersion** in approved data.

    #### How Does It Work?

    **Initial Data**:
    - The material output is pre-classified as either “Approved” or “Defective” based on quality standards.

    **Global Reference**: 
    - We use **only approved materials** to build the “expected pattern.”
    - The **multivariate mean** represents typical values of sensors during the production of approved material.
    - The **inverse covariance matrix** captures the relationships between the sensors, helping us understand how they vary together.

    **Material Classification**: 
    For each sensor and material output:
    - We calculate the **Mahalanobis distance** of the sensors from the expected pattern.
    - We then compare this distance to a **dynamic threshold** (the 95th percentile of distances calculated from the approved materials).
    - Finally, we label the sensor as:
        - **Approved**: If its distance is within the threshold.
        - **Defective**: If its distance exceeds the threshold.

    #### Mathematical Formula:
    The formula for Mahalanobis distance is:

    $$D_M = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}$$

    Where:
    - \(x\) is the vector representing the sensor data.
    - \(\mu\) is the mean vector of the approved materials.
    - \(\Sigma^{-1}\) is the inverse covariance matrix of the approved data.
    """)
    
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