# En cada archivo de página (como Home.py, Predictions.py, etc.)
import streamlit as st

def main():
    st.image("images/logo.png", width=100)
    st.header("Bienvenido a la página principal")
    st.write("Este es el contenido de la página Home.")

