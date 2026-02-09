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
    a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (CONEXIÓN CON REPO) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2503/2503508.png", width=50)
    st.header("Ecosistema ButacaVip")
    st.info("Este dashboard es una herramienta complementaria para el análisis de datos del addon oficial.")
    
    # EL BOTÓN AL REPO
    st.link_button("📥 Ir al Repositorio Kodi", "https://eduard289.github.io/repo-butacavip/#")
    
    st.divider()
    st.caption("Desarrollado por Eduard289 -JL. As - © 2026")

# --- CUERPO PRINCIPAL ---
st.title("📊 ButacaVip: Analítica de Cine")
st.markdown("Explora tendencias, compara sagas y visualiza el impacto en tiempo real.")

# 4. BUSCADOR
col1, col2 = st.columns([4, 1])
with col1:
    busqueda = st.text_input("Buscar Película o Saga:", placeholder="Ej: Marvel, Rocky, Star Wars...")
with col2:
    st.write("")
    st.write("")
    buscar = st.button("Analizar 🚀", use_container_width=True)

# 5. LÓGICA PRINCIPAL
if busqueda or buscar:
    # --- MODO BÚSQUEDA ---
    if not busqueda:
        st.warning("⚠️ Escribe algo para buscar.")
    else:
        try:
            url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={busqueda}&language=es-ES"
            res = requests.get(url).json()

            if res['results']:
                df = pd.DataFrame(res['results'])
                df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
                df = df.dropna(subset=['release_date', 'vote_average'])
                df = df[df['vote_count'] > 10]
                df['year'] = df['release_date'].dt.year
                df = df.sort_values(by='release_date')

                tab_graficas, tab_lista = st.tabs(["📈 Análisis Gráfico", "🎬 Cartelera"])

                with tab_graficas:
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Películas", len(df))
                    mej = df.loc[df['vote_average'].idxmax()]
                    c2.metric("Mejor Valorada", mej['title'], f"{mej['vote_average']} ")
                    c3.metric("Promedio Saga", f"{round(df['vote_average'].mean(), 2)}")
                    
                    st.divider()
                    col_g1, col_g2 = st.columns(2)
                    with col_g1:
                        st.subheader("Ranking de Notas")
                        st.bar_chart(df.sort_values('vote_average').set_index('title')['vote_average'], color="#2E86C1")
                    with col_g2:
                        st.subheader("Evolución Temporal")
                        st.line_chart(df.set_index('year')['vote_average'], color="#2E86C1")

                with tab_lista:
                    cols = st.columns(4)
                    for i, row in enumerate(df.itertuples()):
                        with cols[i % 4]:
                            if row.poster_path:
                                st.image(BASE_URL + row.poster_path, use_container_width=True)
                            st.write(f"**{row.title}**")
                            st.caption(f"{row.year} |  {row.vote_average}")
            else:
                st.error("No se encontraron resultados.")

        except Exception as e:
            st.error(f"Error: {e}")

else:
    # --- MODO INICIO (TENDENCIAS) ---
    # Esto sale cuando NO has buscado nada todavía
    st.divider()
    st.subheader("🔥 Tendencias Globales esta Semana")
    
    try:
        url_trending = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}&language=es-ES"
        res_trend = requests.get(url_trending).json()
        
        if res_trend['results']:
            # Mostramos las top 5 en columnas
            cols = st.columns(5)
            for i, peli in enumerate(res_trend['results'][:5]):
                with cols[i]:
                    if peli.get('poster_path'):
                        st.image(BASE_URL + peli['poster_path'], use_container_width=True)
                    st.write(f"**{peli.get('title', 'Sin título')}**")
                    st.caption(f"⭐ {peli.get('vote_average', 0)}")
    except:
        st.write("Conectando con satélite...")
