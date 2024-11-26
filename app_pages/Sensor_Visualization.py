import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.image("images/logo.png", width=100)
 
    # Cargar el dataset procesado
    file_path = "datasets/filtered_data.csv"  # Ruta actualizada del archivo procesado
    df = pd.read_csv(file_path)


    # Asegurarse de que las columnas X y Y se lean como listas
    import ast
    df['X'] = df['X'].apply(ast.literal_eval)
    df['Y'] = df['Y'].apply(ast.literal_eval)

    # Página de visualización
    st.title("Sensor Visualization")

    # Filtros: Material de salida y sensor (tag)
    material_salida_options = ["NONE", "Show All"] + df['material_salida'].unique().tolist()
    selected_material = st.selectbox("Select Material de Salida", material_salida_options)

    if selected_material not in ["NONE", "Show All"]:
        tag_options = ["NONE", "Show All"] + df[df['material_salida'] == selected_material]['tag'].unique().tolist()
    else:
        tag_options = ["NONE", "Show All"] + df['tag'].unique().tolist()

    selected_tag = st.selectbox("Select Sensor (Tag)", tag_options)

    # Checkbox para seleccionar el estado de Material (diseñado horizontalmente)
    status_filter = st.radio(
        "Select Material Status:",
        options=["Both", "Aprobado", "Defectuoso"],
        index=0,
        horizontal=True  # Opciones en formato horizontal
    )

    # Filtrar el dataframe según el estado seleccionado
    if status_filter != "Both":
        df = df[df['Material status'] == status_filter]

    # Mostrar mensaje cuando no se selecciona ninguna opción válida
    if selected_material == "NONE" or selected_tag == "NONE":
        st.write("Choose an option from both filters to visualize a graph.")
    else:
        # Función para generar gráficos con colores basados en Material status
        def plot_graph(x_values, y_values, title, status):
            # Seleccionar el color basado en Material status
            color = 'green' if status == 'Aprobado' else 'red'
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(x_values, y_values, marker='o', color=color)
            ax.set_title(title, fontsize=16)
            ax.set_xlabel("Time (s)", fontsize=14)
            ax.set_ylabel("Y Values", fontsize=14)
            ax.tick_params(axis='x', rotation=45)
            st.pyplot(fig)

        # Mostrar gráficos basados en la selección
        if selected_material == "Show All" and selected_tag == "Show All":
            st.write(f"Showing all {status_filter} sensors (tags) for all materials:")
            grouped = df.groupby(['material_salida', 'tag'])
            for (material, tag), group in grouped:
                x_values = group.iloc[0]['X']
                y_values = group.iloc[0]['Y']
                status = group.iloc[0]['Material status']
                plot_graph(x_values, y_values, f"{material} - {tag}", status)
        elif selected_material != "Show All" and selected_tag == "Show All":
            st.write(f"Showing all {status_filter} sensors (tags) for material: {selected_material}")
            filtered_df = df[df['material_salida'] == selected_material]
            for tag in filtered_df['tag'].unique():
                group = filtered_df[filtered_df['tag'] == tag].iloc[0]
                x_values = group['X']
                y_values = group['Y']
                status = group['Material status']
                plot_graph(x_values, y_values, f"{selected_material} - {tag}", status)
        elif selected_material != "Show All" and selected_tag != "Show All":
            st.write(f"Showing graph for material: {selected_material}, sensor (tag): {selected_tag}")
            filtered_df = df[(df['material_salida'] == selected_material) & (df['tag'] == selected_tag)]
            if not filtered_df.empty:
                group = filtered_df.iloc[0]
                x_values = group['X']
                y_values = group['Y']
                status = group['Material status']
                plot_graph(x_values, y_values, f"{selected_material} - {selected_tag}", status)
            else:
                st.write("No data available for this selection.")
                
        
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
