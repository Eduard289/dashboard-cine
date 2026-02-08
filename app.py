import streamlit as st
import pandas as pd

# 1. Configuración de la página (¡Ahora con layout ancho!)
st.set_page_config(
    page_title="ButacaVip Pro",
    page_icon="🎬",
    layout="wide"
)

# 2. Título y Estilo
st.title("🎬 ButacaVip: Centro de Datos")
st.markdown("---") # Una línea separadora elegante

# 3. Datos "Simulados" (Ahora con URLs de imágenes reales)
data = {
    'Película': ['Avatar: El Sentido del Agua', 'Oppenheimer', 'Barbie', 'Dune: Parte 2', 'Godzilla x Kong', 'Super Mario Bros'],
    'Género': ['Ciencia Ficción', 'Drama', 'Comedia', 'Ciencia Ficción', 'Acción', 'Animación'],
    'Vistas': [2500, 3100, 2800, 2900, 1500, 2100],
    'Nota': [7.8, 8.9, 7.2, 9.0, 6.5, 7.5],
    'Poster': [
        'https://image.tmdb.org/t/p/w200/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg',
        'https://image.tmdb.org/t/p/w200/ncKCQVXgk4BcQV6XbvesgZ2zGpZ.jpg',
        'https://image.tmdb.org/t/p/w200/fNtqD4BTFj0Bgo9lyoAucFWtexd.jpg',
        'https://image.tmdb.org/t/p/w200/czembW0Rk1Ke7lCJGahbOhdCuhV.jpg',
        'https://image.tmdb.org/t/p/w200/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg',
        'https://image.tmdb.org/t/p/w200/zNKs1T0VZuJiVuhuL5GSCNk3trF.jpg'
    ]
}
df = pd.DataFrame(data)

# 4. LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("🔍 Filtros")
genero_filtro = st.sidebar.multiselect(
    "Selecciona Género:",
    options=df['Género'].unique(),
    default=df['Género'].unique()
)

# Filtrar los datos según lo que el usuario elija
df_filtrado = df[df['Género'].isin(genero_filtro)]

# 5. PESTAÑAS PRINCIPALES
tab1, tab2, tab3 = st.tabs(["📈 Estadísticas", "🖼️ Galería", "📋 Datos Crudos"])

with tab1:
    # Métricas (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("Películas Mostradas", len(df_filtrado))
    col2.metric("Total Visualizaciones", f"{df_filtrado['Vistas'].sum():,}")
    col3.metric("Nota Media", round(df_filtrado['Nota'].mean(), 1))
    
    # Gráfico
    st.subheader("Tendencias de Visualización")
    st.bar_chart(df_filtrado.set_index('Película')['Vistas'], color="#ff4b4b")

with tab2:
    st.subheader("Cartelera Actual")
    # Mostrar imágenes en columnas (Grid)
    cols = st.columns(len(df_filtrado))
    for index, (i, row) in enumerate(df_filtrado.iterrows()):
        # Ajustamos para que no falle si hay muchas pelis
        col_actual = cols[index % len(cols)] if len(cols) > 0 else st
        with col_actual:
            st.image(row['Poster'], caption=row['Película'])
            st.write(f"⭐ {row['Nota']}")

with tab3:
    st.dataframe(df_filtrado, use_container_width=True)

# 6. Pie de página
st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por Eduard289")
