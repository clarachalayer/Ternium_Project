import streamlit as st
from streamlit_option_menu import option_menu
from app_pages import Home, Predictions, Sensor_Visualization, Cluster_Specifications, Dictionary, Profile

st.set_page_config(
    page_title="Ternium",
    layout="wide",
    page_icon="😡"
)


# Configuración del menú en el sidebar
with st.sidebar:
    
    # Imagen de perfil centrada con columnas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("./profile_image.png", width=140)

    # Información del usuario
    st.markdown("""
    <div class="user-info" style="text-align: center; padding: 2px 0;">
        <strong style="font-size: 17px;">Sarah Connor</strong><br>
        <span style="font-size: 14px; color: gray;">sarahc@gmail.com</span><br>
    </div>
    """, unsafe_allow_html=True)

    # Menú de navegación con título e ícono centrados
    selected = option_menu(
        menu_title="Ternium",
        options=["Home", "Predictions", "Sensor Visualization", 
                "Cluster Specifications", "Dictionary", "Profile"],
        icons=["house", "bar-chart", "eye", "boxes", "book", "person"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "2px", "background-color": "#f0f2f6"},
            "icon": {"color": "blue", "font-size": "25px"},
            "nav-link": {
                "font-size": "15px", 
                "text-align": "left", 
                "padding": "2px 10px",
                "margin": "2px 0px", 
                "--hover-color": "#eee"
            },
            "nav-link-selected": {"background-color": "#1E90FF"},
            "menu-title": {
                "font-size": "17px",
                "font-weight": "bold",
                "text-align": "center",
                "margin": "0px",
                "color": "#333",
            }
        }
    )

    # Logo de Ternium centrado con columnas
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("./ternium_logo.png", width=200)

# Enrutamiento de páginas
# Llama a la función `main()` de cada archivo de acuerdo con la selección
if selected == "Home":
    Home.main()
elif selected == "Predictions":
    Predictions.main()
elif selected == "Sensor Visualization":
    Sensor_Visualization.main()
elif selected == "Cluster Specifications":
    Cluster_Specifications.main()
elif selected == "Dictionary":
    Dictionary.main()
elif selected == "Profile":
    Profile.main()
