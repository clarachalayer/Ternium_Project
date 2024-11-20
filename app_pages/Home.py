import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.image("images/ternium_logo.png", width=100) 
    st.header("Welcome back!")
    st.write("It’s time to get to work hard and analyze some data.")
    st.write("Here is a weekly quick summary")

    # Datos de ejemplo
    elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]
    serie1 = [10, 20, 30, 40, 30]
    serie2 = [5, 15, 25, 35, 45]
    serie3 = [20, 10, 35, 25, 50]

    # Configuración de la gráfica
    plt.figure(figsize=(8, 5))
    plt.plot(elementos, serie1, marker='o', linestyle='-', color='#76D7C4', label="Serie 1")  # Color de Serie 1
    plt.plot(elementos, serie2, marker='o', linestyle='-', color='#5DADE2', label="Serie 2")  # Color de Serie 2
    plt.plot(elementos, serie3, marker='o', linestyle='-', color='#2874A6', label="Serie 3")  # Color de Serie 3

    # Personalización de la leyenda y ejes
    plt.legend(loc="upper left")
    plt.xlabel("Elementos")
    plt.ylabel("Valores")
    plt.ylim(0, 55)

    # Fondo redondeado
    plt.gca().set_facecolor((0.9, 0.9, 0.9, 0.8))  # Color de fondo de la gráfica
    plt.gcf().patch.set_facecolor((1, 1, 1, 0))     # Fondo transparente alrededor de la gráfica

    # Mostrar la gráfica en Streamlit
    st.pyplot(plt)
    
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
    


