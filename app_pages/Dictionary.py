# En cada archivo de página (como Home.py, Predictions.py, etc.)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.image("images/logo.png", width=100)
    st.header("Dictionary")
    
    st.write("This section provides detailed information about various sensors and their respective parameters. Here you can explore the dataset by filtering specific sensors or viewing all available data. The table displays information such as sensor names, variable names, examples, and measurement units, enabling easy identification and understanding of sensor functionality.")

    #Data for the table
    df = pd.read_csv("datasets/Dicc_sensors.csv")

    # Add a filter in the sidebar
    filter_variable = "SENSOR_NAME"

    # Example: Filter by a specific column
    unique_values = df[filter_variable].unique()
    options = ['NONE'] + list(unique_values)
    selected_value = st.selectbox("Select the sensor you want to look for:", options)

    if selected_value == "NONE":
        st.dataframe(df,height = 500)
        
    else:
    # Filter the dataset based on the selection
        filtered_df = df[df[filter_variable] == selected_value]
        st.dataframe(filtered_df)


    #Categories image
    st.markdown("### Categories")
    
    st.write("In this section, you can further analyze coil data by selecting a category: Soft, Medium, or Hard. Each category corresponds to a specific dataset, allowing focused exploration of coil characteristics based on material hardness. By selecting a category, you can view and interact with the relevant data to gain insights into the material's properties and processing details. ")
        
    col1, col2, col3 = st.columns([8, 8, 8])
    selected_df = None
    with col1:
        st.image("images/soft_coil.png", width=290)

        # Añadir el botón de Streamlit con CSS para centrarlo
        centered_button = st.markdown(
            """
            <style>
            div.stButton > button {
                display: block;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.button("Soft"):
            selected_df = pd.read_csv("datasets/Soft_Coil.csv")

    with col2:
        st.image("images/medium_coil.png", width=160)
        # Añadir el botón de Streamlit con CSS para centrarlo
        centered_button = st.markdown(
            """
            <style>
            div.stButton > button {
                display: block;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.button("Medium"):
            selected_df = pd.read_csv("datasets/Medium_Coil.csv")

    with col3:
        st.image("images/hard_coil.png", width=210)
        # Añadir el botón de Streamlit con CSS para centrarlo
        centered_button = st.markdown(
            """
            <style>
            div.stButton > button {
                display: block;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.button("Hard"):
            selected_df = pd.read_csv("datasets/Hard_Coil.csv")


    # Muestra el DataFrame seleccionado en pantalla completa fuera de las columnas
    if selected_df is not None:
        st.write("### Data Selected: ")
        st.dataframe(selected_df, use_container_width=True)

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