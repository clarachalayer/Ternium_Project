import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.image("images/logo.png", width=100)
    st.header("Sensor visualization")
    #st.write("Este es el contenido de la página Sensor Visualization.")
    df = pd.read_csv("datasets/filtered_data.csv")

    # Add a filter in the sidebar
    st.subheader("Filter Options")

    filter_variable = "material_salida"

    # Example: Filter by a specific column
    unique_values = df[filter_variable].unique()
    options = ['NONE'] + list(unique_values)
    selected_value = st.selectbox("Select a material to filter:", options)

    if selected_value == "NONE":
        filtered_df = df
    else:
    # Filter the dataset based on the selection
        filtered_df = df[df[filter_variable] == selected_value]

    if not filtered_df.empty:
        col1, col2 = st.columns([3,1])

        with col1:

            plt.figure(figsize=(10, 5))
            plt.plot(
                filtered_df['tag'],
                filtered_df['Slab Thickness Encoded'],
                marker='o',
                linestyle='-',
                color='#76D7C4',
                label="Slab Thickness"
            )
            plt.xlabel("Material Salida")
            plt.ylabel("Slab Thickness Encoded")
            plt.title(f"Slab Thickness for Coil: {selected_value}")
            plt.legend()
            plt.xticks(rotation=45)

            # Display the plot in Streamlit
            st.pyplot(plt)
        with col2:
            st.write("Data Summary:")
            st.write(filtered_df['material_salida'])
    else:
        st.write("No data available for the selected month.")