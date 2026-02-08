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

# 3. Datos (¡Con IMÁGENES ARREGLADAS!)
data = {
    'Película': ['Avatar: El Sentido del Agua', 'Oppenheimer', 'Barbie', 'Dune: Parte 2', 'Godzilla x Kong', 'Super Mario Bros'],
    'Género': ['Ciencia Ficción', 'Drama', 'Comedia', 'Ciencia Ficción', 'Acción', 'Animación'],
    'Vistas': [2500, 3100, 2800, 2900, 1500, 2100],
    'Nota': [7.8, 8.9, 7.2, 9.0, 6.5, 7.5],
    'Poster': [
        'https://image.tmdb.org/t/p/w200/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg',  # Avatar 2
        'https://image.tmdb.org/t/p/w200/8Gxv8gSFCU0XGDykIGy72X9Yv6O.jpg',  # Oppenheimer (Nuevo link)
        'https://image.tmdb.org/t/p/w200/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg',  # Barbie (Nuevo link)
        'https://image.tmdb.org/t/p/w200/czembW0Rk1Ke7lCJGahbOhdCuhV.jpg',  # Dune 2
        'https://image.tmdb.org/t/p/w200/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg',  # Godzilla x Kong
        'https://image.tmdb.org/t/p/w200/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg'   # Super Mario Bros (Nuevo link)
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
df_filtrado = df[df['Género'].isin(genero_filtro)]

# 5. Pestañas
tab1, tab2, tab3 = st.tabs(["📈 Estadísticas", "🖼️ Galería", "📋 Datos Crudos"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Películas Mostradas", len(df_filtrado))
    col2.metric("Total Visualizaciones", f"{df_filtrado['Vistas'].sum():,}")
    col3.metric("Nota Media", round(df_filtrado['Nota'].mean(), 1))
    
    st.subheader("Tendencias de Visualización")
    # ¡AQUÍ ESTÁ EL CAMBIO DE COLOR! (Azul profesional)
    st.bar_chart(df_filtrado.set_index('Película')['Vistas'], color="#2E86C1")

with tab2:
    st.subheader("Cartelera Actual")
    cols = st.columns(len(df_filtrado))
    for index, (i, row) in enumerate(df_filtrado.iterrows()):
        col_actual = cols[index % len(cols)] if len(cols) > 0 else st
        with col_actual:
            st.image(row['Poster'], caption=row['Película'])
            st.write(f"⭐ {row['Nota']}")

with tab3:
    st.dataframe(df_filtrado, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por Eduard289")
