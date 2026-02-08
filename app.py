import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(
    page_title="ButacaVip Analytics",
    page_icon="🎬",
    layout="wide"
)

# --- TRUCO CSS PARA CAMBIAR COLORES ---
# Esto inyecta código de diseño para forzar el cambio del rojo al azul
st.markdown("""
<style>
/* Cambia el fondo de las etiquetas del filtro (multiselect) */
span[data-baseweb="tag"] {
    background-color: #2E86C1 !important;
}
/* Oculta bordes rojos extraños */
span[data-baseweb="tag"] {
    border-color: #2E86C1 !important;
}
/* Cambia el color del texto dentro de las etiquetas a blanco */
span[data-baseweb="tag"] span {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)
# --------------------------------------

# 2. Título
st.title("🎬 ButacaVip: Centro de Datos")
st.markdown("---")

# 3. Datos (Limpios, sin imágenes que fallen)
data = {
    'Película': ['Avatar: El Sentido del Agua', 'Oppenheimer', 'Barbie', 'Dune: Parte 2', 'Godzilla x Kong', 'Super Mario Bros'],
    'Género': ['Ciencia Ficción', 'Drama', 'Comedia', 'Ciencia Ficción', 'Acción', 'Animación'],
    'Vistas': [2500, 3100, 2800, 2900, 1500, 2100],
    'Nota': [7.8, 8.9, 7.2, 9.0, 6.5, 7.5]
}
df = pd.DataFrame(data)

# 4. Barra Lateral
st.sidebar.header("🔍 Filtros Avanzados")
genero_filtro = st.sidebar.multiselect(
    "Filtrar por Categoría:",
    options=df['Género'].unique(),
    default=df['Género'].unique()
)

# Filtrar datos
df_filtrado = df[df['Género'].isin(genero_filtro)]

# 5. Pestañas (Simplificadas a dos)
tab1, tab2 = st.tabs(["📈 Dashboard Visual", "📋 Base de Datos"])

with tab1:
    if df_filtrado.empty:
        st.info("👈 Selecciona algún género en el menú lateral.")
    else:
        # Métricas principales
        col1, col2, col3 = st.columns(3)
        col1.metric("Películas Activas", len(df_filtrado))
        col2.metric("Impacto (Vistas)", f"{df_filtrado['Vistas'].sum():,}")
        col3.metric("Calidad Media", round(df_filtrado['Nota'].mean(), 1))
        
        st.markdown("### Rendimiento por Título")
        # Gráfico Azul Corporativo
        st.bar_chart(df_filtrado.set_index('Película')['Vistas'], color="#2E86C1")

with tab2:
    st.subheader("Detalle de Registros")
    if df_filtrado.empty:
        st.write("No hay datos disponibles con estos filtros.")
    else:
        # Tabla interactiva avanzada
        st.dataframe(
            df_filtrado,
            use_container_width=True,
            column_config={
                "Nota": st.column_config.ProgressColumn(
                    "Valoración del Público",
                    help="Puntuación sobre 10",
                    format="%.1f",
                    min_value=0,
                    max_value=10,
                ),
                "Vistas": st.column_config.NumberColumn(
                    "Visualizaciones",
                    format="%d 👁️"
                )
            }
        )

st.sidebar.markdown("---")
st.sidebar.caption("Panel de Control v1.2 | Eduard289")
