
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

# 3. Datos (¡Con enlaces de imágenes de Wikipedia, más estables!)
data = {
    'Película': ['Avatar: El Sentido del Agua', 'Oppenheimer', 'Barbie', 'Dune: Parte 2', 'Godzilla x Kong', 'Super Mario Bros'],
    'Género': ['Ciencia Ficción', 'Drama', 'Comedia', 'Ciencia Ficción', 'Acción', 'Animación'],
    'Vistas': [2500, 3100, 2800, 2900, 1500, 2100],
    'Nota': [7.8, 8.9, 7.2, 9.0, 6.5, 7.5],
    'Poster': [
        'https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg', # Avatar
        'https://upload.wikimedia.org/wikipedia/en/4/4a/Oppenheimer_%28film%29.jpg', # Oppenheimer (Wikipedia)
        'https://upload.wikimedia.org/wikipedia/en/0/0b/Barbie_2023_film_poster.jpg', # Barbie (Wikipedia)
        'https://image.tmdb.org/t/p/w500/czembW0Rk1Ke7lCJGahbOhdCuhV.jpg', # Dune 2
        'https://image.tmdb.org/t/p/w500/z1p34vh7dEOnLDmyCrlUVLuoDzd.jpg', # Godzilla
        'https://upload.wikimedia.org/wikipedia/en/4/44/The_Super_Mario_Bros._Movie_poster.jpg' # Mario (Wikipedia)
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
    if df_filtrado.empty:
        st.info("👈 Selecciona algún género en el menú lateral para ver datos.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Películas Mostradas", len(df_filtrado))
        col2.metric("Total Visualizaciones", f"{df_filtrado['Vistas'].sum():,}")
        col3.metric("Nota Media", round(df_filtrado['Nota'].mean(), 1))
        
        st.subheader("Tendencias de Visualización")
        # Usamos el mismo azul profesional que configuraremos en el tema
        st.bar_chart(df_filtrado.set_index('Película')['Vistas'], color="#2E86C1")

with tab2:
    st.subheader("Cartelera Actual")
    if df_filtrado.empty:
        st.info("👈 Selecciona algún género para ver las carátulas.")
    else:
        # Lógica para columnas dinámicas (evita errores y carátulas gigantes)
        num_pelis = len(df_filtrado)
        # Si hay pocas pelis (menos de 4), usamos tantas columnas como pelis haya.
        # Si hay muchas, limitamos a 4 columnas máximo para que quede bien.
        cols_to_use = num_pelis if num_pelis > 0 and num_pelis < 4 else 4
        
        cols = st.columns(cols_to_use)
        for index, (i, row) in enumerate(df_filtrado.iterrows()):
            col_actual = cols[index % cols_to_use]
            with col_actual:
                st.image(row['Poster'], caption=row['Película'], use_container_width=True)
                st.write(f"⭐ **{row['Nota']}**")

with tab3:
    st.dataframe(df_filtrado, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por Eduard289")
