import streamlit as st
import pandas as pd

# Configuración
st.set_page_config(page_title="Cine Dashboard", page_icon="🎬")

# Título
st.title("🎬 Mi Primer Dashboard de Cine")
st.write("Bienvenido al panel de datos interactivo.")

# Datos falsos
datos = pd.DataFrame({
    'Película': ['Avatar 2', 'Oppenheimer', 'Barbie', 'Dune 2', 'Godzilla'],
    'Vistas': [1500, 2300, 1800, 2100, 900],
    'Nota': [4.5, 4.9, 4.3, 4.8, 3.5]
})

# Mostrar tabla y gráfico
col1, col2 = st.columns(2)
col1.subheader("📋 Datos")
col1.dataframe(datos)

col2.subheader("📊 Gráfico")
col2.bar_chart(datos.set_index('Película')['Vistas'])

# Botón
if st.button('Actualizar'):
    st.balloons()
    st.success("¡Datos cargados!")
