# Importar librerias
import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('/Users/margarita/Repositorios/TT_sprint5/vehicles_us.csv')  

# Casilla de Verificacion/ reemplaza Botón para construir histograma
hist_button = st.checkbox('Construir histograma')
if hist_button:
    # Mensaje al aplastar el boton
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Histograma
    fig = px.histogram(car_data, x = "odometer")
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Casilla de Verificacion/ reemplaza botón para construir gráfico de dispersión
scatter_button = st.checkbox('Construir gráfico de dispersión')
if scatter_button:
    # Mensaje al aplastar el boton
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="model_year", y="price", color="condition", marginal_y="violin", marginal_x="box")
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)





