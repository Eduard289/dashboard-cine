import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(
    page_title="ButacaVip Pro",
    page_icon="🎬",
    layout="wide"
)

# 2. Título
st.title("🎬 ButacaVip: Centro de Datos")
st.markdown("---")

# 3. Datos (Enlace de imágenes arreglados y estables)
data = {
    'Película': ['Avatar: El Sentido del Agua', 'Oppenheimer', 'Barbie', 'Dune: Parte 2', 'Godzilla x Kong', 'Super Mario Bros'],
    'Género': ['Ciencia Ficción', 'Drama', 'Comedia', 'Ciencia Ficción', 'Acción', 'Animación'],
    'Vistas': [2500, 3100, 2800, 2900, 1500, 2100],
    'Nota': [7.8, 8.9, 7.2, 9.0, 6.5, 7.5],
    'Poster': [
        'https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg',
        'https://image.tmdb.org/t/p/w500/ncKCQVXgk4BcQV6XbvesgZ2zGpZ.jpg',
        'https://image.tmdb.org/t/p/w500/fNtqD4BTFj0Bgo9lyoAucFWtexd.jpg',
        'https://image.tmdb.org/t/p/w500/czembW0Rk1Ke7lCJGahbOhdCuhV.jpg',
        'https://image.tmdb.org/t/p/w500/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg',
        'https://image.tmdb.org/t/p/w500/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg'
    ]
}
df = pd.DataFrame(data)

# 4. Barra Lateral
st.sidebar.header("🔍 Filtros")
genero_filtro = st.sidebar.multiselect(
    "Selecciona Género:",
    options=df['Género'].unique(),
    default=df['Género'].unique()
)

# Filtramos el dataframe
df_filtrado = df[df['Género'].isin(genero_filtro)]

# 5. Pestañas
tab1, tab2, tab3 = st.tabs(["📈 Estadísticas", "🖼️ Galería", "📋 Datos Crudos"])

with tab1:
    # Si no hay datos, mostramos aviso
    if df_filtrado.empty:
        st.warning("⚠️ No hay datos para mostrar. Selecciona un género en el menú lateral.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Películas Mostradas", len(df_filtrado))
        col2.metric("Total Visualizaciones", f"{df_filtrado['Vistas'].sum():,}")
        col3.metric("Nota Media", round(df_filtrado['Nota'].mean(), 1))
        
        st.subheader("Tendencias de Visualización")
        # COLOR AZUL PROFESIONAL APLICADO AQUÍ
        st.bar_chart(df_filtrado.set_index('Película')['Vistas'], color="#2E86C1")

with tab2:
    st.subheader("Cartelera Actual")
    
    # PROTECCIÓN ANTI-ERROR: Si la lista está vacía, no intenta crear columnas
    if df_filtrado.empty:
        st.info("👈 Selecciona algún género en la izquierda para ver las carátulas.")
    else:
        # Creamos un máximo de 4 columnas para que no se vean diminutas si hay muchas
        num_cols = len(df_filtrado)
        if num_cols > 4: num_cols = 4
        
        cols = st.columns(num_cols)
        for index, (i, row) in enumerate(df_filtrado.iterrows()):
            col_actual = cols[index % num_cols]
            with col_actual:
                st.image(row['Poster'], caption=row['Película'], use_container_width=True)
                st.write(f"⭐ **{row['Nota']}**")

with tab3:
    st.dataframe(df_filtrado, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por Eduard289")
