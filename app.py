import pandas as pd
import plotly as plt
import streamlit as st

car_data = pd.read_csv('C:/Users/ax22180/project_sprint_7/vehicles_us.csv') # leer los datos
hist_header = st.header('Distribución por kilometraje')
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = plt.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
     