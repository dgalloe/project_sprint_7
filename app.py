import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:/Users/ax22180/project_sprint_7/vehicles_us.csv') # leer los datos
hist_header = st.header('Distribución por kilometraje')
#hist_button = st.button('Construir histograma') # crear un botón
build_histogram = st.checkbox('Construir un histograma')
     
#if hist_button: # al hacer clic en el botón
if build_histogram:
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_header = st.header('Relación Precio y kilometraje')
#scatter_button = st.button('Construir un gráfico de disperción') # crear un botón
build_scatter = st.checkbox('Construir un gráfico de disperción')    

#if scatter_button: # al hacer clic en el botón
if build_scatter:
    # escribir un mensaje
    st.write('Creación de un gráfico de disperción para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
     