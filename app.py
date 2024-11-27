import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from recomendation import retorno, productoras, peliculas_pais, franquicia, peliculas_dia, peliculas_mes, obtener_recomendaciones
import pandas as pd 

# Establecer la configuración de la página a layout de ancho completo
st.set_page_config(layout="centered")


# Función para cargar el JSON de Lottie desde una URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Usar una URL válida de Lottie
lottie_codding = load_lottieurl("https://lottie.host/b1493fb9-d780-4004-94ef-3e43d43368af/ZyZPa1dYIV.json")


# Crear columnas para el título y la animación
col1Title, col2Title = st.columns([8, 2])  # Ajustar la proporción de las columnas
with col1Title:
    # Título de la página
    st.title("Recomendador de Películas")
with col2Title:
    # Muestra la animación de Lottie
    if lottie_codding:
        st_lottie(lottie_codding, height=100, key="coding")


with st.container():
    # Contenedor para las recomendaciones
    st.subheader("Recomendar Peliculas")
    # Crear un input de texto para que el usuario escriba una película
    recomendation_input = st.text_input("Ingresa el nombre de una película:", key="recomendation_input")

    # Botón para obtener recomendaciones
    if st.button("Obtener Recomendaciones"):
        if recomendation_input:
            # Obtener las recomendaciones basadas en el nombre de la película ingresada
            recomendaciones = obtener_recomendaciones(recomendation_input)
            
            if recomendaciones:
                # Mostrar las recomendaciones
                st.write(f"Películas recomendadas basadas en: {recomendation_input}")
                for pelicula in recomendaciones:
                    st.write(f"- {pelicula}")
            else:
                st.write("No se encontraron recomendaciones para esa película.")
        else:
            st.write("Por favor ingresa el nombre de una película.")

    # Sección de consulta de retorno de inversión de una película
    st.subheader("Consulta de Retorno de inversión Película")
    pelicula_input = st.text_input("Ingresa el nombre de una película:", key="pelicula_input")
    if st.button("Consultar Retorno"):
        if pelicula_input:
            resultado = retorno(pelicula_input)
            st.write(f"Pelicula: {resultado['pelicula']}")
            st.write(f"Inversión: {resultado['inversion']}")
            st.write(f"Ganancia: {resultado['ganacia']}")
            st.write(f"Retorno: {resultado['retorno']}")
            st.write(f"Año: {resultado['anio']}")
        else:
            st.write("Por favor ingresa el nombre de una película.")

    # Sección de consulta por Productora
    st.subheader("Consulta informacion de la Productora")
    productora_input = st.text_input("Ingresa el nombre de una productora:", key="productora_input")
    if st.button("Consultar Productora"):
        if productora_input:
            resultado = productoras(productora_input)
            st.write(f"Productora: {resultado['productora']}")
            st.write(f"Ganancia Total: {resultado['ganancia_total']}")
            st.write(f"Número de Películas: {resultado['cantidad']}")
        else:
            st.write("Por favor ingresa el nombre de una productora.")

    # Sección de consulta por País
    st.subheader("Consulta la Cantidad de Películas por País")
    pais_input = st.text_input("Ingresa el nombre de un país:", key="pais_input")
    if st.button("Consultar País"):
        if pais_input:
            resultado = peliculas_pais(pais_input)
            st.write(f"País: {resultado['pais']}")
            st.write(f"Cantidad de Películas: {resultado['cantidad de peliculas']}")
        else:
            st.write("Por favor ingresa el nombre de un país.")

    # Sección de consulta por Franquicia
    st.subheader("Consulta de Franquicia")
    franquicia_input = st.text_input("Ingresa el nombre de una franquicia:", key="franquicia_input")
    if st.button("Consultar Franquicia"):
        if franquicia_input:
            resultado = franquicia(franquicia_input)
            st.write(f"Franquicia: {resultado['franquicia']}")
            st.write(f"Número de Películas: {resultado['cantidad']}")
            st.write(f"Ganancia Total: {resultado['ganancia_total']}")
            st.write(f"Ganancia Promedio: {resultado['ganancia_promedio']}")
        else:
            st.write("Por favor ingresa el nombre de una franquicia.")

    # Sección de consulta de Películas por Día de la Semana
    st.subheader("Consulta de Películas por Día de la Semana")
    dia_input = st.text_input("Ingresa el día de la semana (lunes, martes, etc.):", key="dia_input")
    if st.button("Consultar Día"):
        if dia_input:
            resultado = peliculas_dia(dia_input)
            st.write(f"Día: {resultado['dia']}")
            st.write(f"Cantidad de Películas: {resultado['cantidad']}")
        else:
            st.write("Por favor ingresa el nombre de un día de la semana.")

    # Sección de consulta de Películas por Mes
    st.subheader("Consulta de Películas por Mes")
    mes_input = st.text_input("Ingresa el mes (enero, febrero, etc.):", key="mes_input")
    if st.button("Consultar Mes"):
        if mes_input:
            resultado = peliculas_mes(mes_input)
            st.write(f"Mes: {resultado['mes']}")
            st.write(f"Cantidad de Películas: {resultado['cantidad']}")
        else:
            st.write("Por favor ingresa el nombre de un mes.")