# pages/Home.py
import streamlit as st

def main():
    st.image("images/logo.png", width=100)
    st.header("Bienvenido a la página principal")
    st.write("Este es el contenido de la página Home.")

    #Agregar el codigo necesario


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
