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
    
    # Mostrar el DataFrame actualizado
    st.dataframe(combined_data)

    # Select the 'Slab Weight' column for clustering
    slab_weight_data = combined_data[['Slab Weight']]

    # Create and train the KMeans model
    model = KMeans(n_clusters=4, random_state=0, n_init='auto')

    # Model training
    model.fit(slab_weight_data)

    # Add cluster labels to the original DataFrame
    combined_data['Cluster_Weight'] = model.labels_

    # Create a scatter plot to visualize the clusters
    f1 = plt.figure(figsize=(8, 6), dpi=100)
    for cluster in range(4):  # Loop through each cluster
        cluster_data = combined_data[combined_data['Cluster_Weight'] == cluster]
        plt.scatter(cluster_data.index, cluster_data['Slab Weight'], label=f'Cluster {cluster}', s=50)

    # Plot the cluster centers
    plt.scatter(
        range(len(model.cluster_centers_)),
        model.cluster_centers_,
        color='black',
        label='Centroids',
        marker='x',
        s=100,
    )

    # Add plot details
    plt.title("Cluster Visualization (Slab Weight)")
    plt.xlabel("Index")
    plt.ylabel("Slab Weight")
    plt.legend()
    plt.show()
    st.pyplot(f1)
