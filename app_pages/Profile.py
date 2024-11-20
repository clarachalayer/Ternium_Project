import streamlit as st

def main():
    st.image("images/ternium_logo.png", width=140) 
    # Encabezado de la página de perfil
    st.title("Perfil de Usuario")
    st.write("Aquí puedes ver la información básica de tu perfil.")

    # Contenedor principal
    with st.container():
        col1, col2 = st.columns([1, 3])

        # Foto de perfil
        with col1:
            st.image("images/profile_image.png", width=150)  # Asegúrate de que la imagen esté en la ruta correcta

        # Información del usuario
        with col2:
            st.subheader("Team 4 Seiketsu")
            st.write("seiketsu@gmail.com")
            st.write("📍 Monterrey, NL")
            st.write("🔶 Análisis de datos y gestión de proyectos.")

    st.markdown("---")

    # Sección de información adicional
    st.subheader("Información Personal")
    st.write("**Fecha de nacimiento:** 12 de mayo de 1990")
    st.write("**Teléfono:** +1 234 567 890")
    st.write("**Ocupación:** Ingeniera de Software")
    st.write("**Intereses:** Data Science, Machine Learning, Project Management")
    
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
    

