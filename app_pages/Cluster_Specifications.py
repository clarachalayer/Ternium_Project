# En cada archivo de página (como Home.py, Predictions.py, etc.)
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

def main():
    st.image("images/logo.png", width=100)
    st.header("Cluster pages")
    st.write("Este es el contenido de la página Home.")
    
    #Data for the table
    combined_data = pd.read_csv("datasets\combined_data_cleaned.csv")
    
    # Eliminar la columna "Steel_Type"
    combined_data = combined_data.drop(columns=["Steel_Type"])
    #Eliminar la categoria Unknown
    combined_data = combined_data[~combined_data["steel_category"].str.contains("Unknown", case=False, na=False)]
    
    # Select the 'Slab Weight' column for clustering
    slab_weight_data = combined_data[['Slab Weight']]
    
    # Crear un filtro por categoria de acero
    # Add a filter in the sidebar
    filter_variable = "steel_category"

    # Example: Filter by a specific column
    steel_categories = ['NONE'] + list(combined_data['steel_category'].unique())
    selected_category = st.selectbox("Select the category you want to look for:", steel_categories)

    # Filtrar los datos según la categoría seleccionada
    filtered_df = combined_data if selected_category == "NONE" else combined_data[combined_data['steel_category'] == selected_category]

    col1, col2 = st.columns([12, 8])

    with col2:
        # Filtro adicional por SGC
        sgc_values = ['NONE'] + list(filtered_df['SGC'].unique())
        selected_sgc = col2.selectbox("Selecciona la categoría SGC:", sgc_values)

        if selected_sgc != "NONE":
            filtered_df = filtered_df[filtered_df['SGC'] == selected_sgc]

        # Mostrar la tabla filtrada en col2
        col2.dataframe(filtered_df, height=500)

    with col1:
        st.subheader("Gráfica de Clustering")
        if filtered_df.empty:
            st.warning("No hay datos disponibles después de aplicar los filtros.")
        else:
            # Seleccionar datos para clustering
            if "Slab Weight" not in filtered_df.columns:
                st.error("La columna 'Slab Weight' no existe en los datos.")
            else:
                slab_weight_data = filtered_df[['Slab Weight']]

                # Crear y entrenar el modelo KMeans
                model = KMeans(n_clusters=4, random_state=0, n_init='auto')
                model.fit(slab_weight_data)

                # Agregar las etiquetas de los clusters al DataFrame
                filtered_df['Cluster_Weight'] = model.labels_

                # Crear un gráfico de dispersión
                fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
                for cluster in range(4):
                    cluster_data = filtered_df[filtered_df['Cluster_Weight'] == cluster]
                    ax.scatter(
                        cluster_data.index,
                        cluster_data['Slab Weight'],
                        label=f'Cluster {cluster}',
                        s=50,
                    )

                # Graficar los centroides
                centroids = model.cluster_centers_
                ax.scatter(
                    range(len(centroids)),
                    centroids[:, 0],
                    color='black',
                    label='Centroides',
                    marker='x',
                    s=100,
                )

                # Detalles del gráfico
                ax.set_title("Visualización de Clusters (Slab Weight)")
                ax.set_xlabel("Index")
                ax.set_ylabel("Slab Weight")
                ax.legend()

                # Mostrar el gráfico en Streamlit
                st.pyplot(fig)
            
    











