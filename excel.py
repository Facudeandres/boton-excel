import streamlit as st
import pandas as pd

# Importa la función file_uploader
from streamlit import file_uploader

# Crea el botón y almacena el archivo seleccionado en una variable
archivo = file_uploader("Selecciona un archivo de Excel:", type="xlsx")

# Si se seleccionó un archivo, carga su contenido en un DataFrame de pandas
if archivo is not None:
    df = pd.read_excel(archivo)
    
    # Muestra el contenido del DataFrame en la aplicación
    st.write(df)
