import streamlit as st
import pandas as pd
import requests

# 1. CONFIGURACIÓN
st.set_page_config(page_title="ButacaVip Analytics", page_icon="📊", layout="wide")

# 2. TU CLAVE API
API_KEY = "5c88939574e202d8432edcb638e08e10"
BASE_URL = "https://image.tmdb.org/t/p/w500"

# 3. ESTILO CSS (AZUL)
st.markdown("""
<style>
    .stButton>button { background-color: #2E86C1; color: white; border: none; }
    .stMetric { background-color: #F0F2F6; padding: 10px; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

st.title("📊 ButacaVip: Analítica de Cine")
st.markdown("Busca una saga (ej: *Harry Potter*, *Avengers*) y analiza sus datos.")

# 4. BUSCADOR
col1, col2 = st.columns([4, 1])
with col1:
    busqueda = st.text_input("Película o Saga:", placeholder="Escribe aquí...")
with col2:
    st.write("")
    st.write("")
    buscar = st.button("Analizar 🚀", use_container_width=True)

if busqueda or buscar:
    if not busqueda:
        st.warning("⚠️ Escribe algo para buscar.")
    else:
        try:
            # CONEXIÓN API
            url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={busqueda}&language=es-ES"
            res = requests.get(url).json()

            if res['results']:
                # --- PROCESAMIENTO DE DATOS CON PANDAS ---
                df = pd.DataFrame(res['results'])
                
                # Limpiamos datos: Quitamos las que no tienen fecha o nota
                df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
                df = df.dropna(subset=['release_date', 'vote_average'])
                df = df[df['vote_count'] > 10] # Quitamos pelis con pocos votos
                df['year'] = df['release_date'].dt.year

                # Ordenamos por fecha
                df = df.sort_values(by='release_date')

                # --- PESTAÑAS ---
                tab_graficas, tab_lista = st.tabs(["📈 Análisis Gráfico", "🎬 Cartelera"])

                with tab_graficas:
                    # 1. KPIs (Indicadores Clave)
                    mejor_peli = df.loc[df['vote_average'].idxmax()]
                    
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Películas Encontradas", len(df))
                    c2.metric("Mejor Valorada", mejor_peli['title'], f"{mejor_peli['vote_average']} ⭐")
                    c3.metric("Promedio de la Búsqueda", f"{round(df['vote_average'].mean(), 2)} / 10")
                    
                    st.divider()

                    # 2. GRÁFICAS
                    col_g1, col_g2 = st.columns(2)
                    
                    with col_g1:
                        st.subheader("🏆 Ranking de Notas")
                        # Gráfico de barras horizontal ordenado por nota
                        df_sorted = df.sort_values(by='vote_average', ascending=True)
                        st.bar_chart(df_sorted.set_index('title')['vote_average'], color="#2E86C1")
                    
                    with col_g2:
                        st.subheader("📅 Evolución Temporal")
                        # Gráfico de línea por año
                        st.line_chart(df.set_index('year')['vote_average'], color="#2E86C1")
                        st.caption("¿Las películas han mejorado o empeorado con los años?")

                with tab_lista:
                    st.subheader(f"Resultados para '{busqueda}'")
                    cols = st.columns(4)
                    for i, row in enumerate(df.itertuples()):
                        with cols[i % 4]:
                            if row.poster_path:
                                st.image(BASE_URL + row.poster_path, use_container_width=True)
                            st.write(f"**{row.title}**")
                            st.caption(f"{row.year} | ⭐ {row.vote_average}")
            else:
                st.error("No se encontraron resultados.")

        except Exception as e:
            st.error(f"Error: {e}")
