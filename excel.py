import streamlit as st

# Importa la función file_uploader
from streamlit import file_uploader

# Crea el botón y almacena el archivo seleccionado en una variable
archivo = file_uploader("Selecciona un archivo de Excel:", type="xlsx")

# Si se seleccionó un archivo, muestra su contenido
if archivo is not None:
    df = pd.read_excel(archivo)
    st.write(df)