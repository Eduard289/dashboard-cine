import streamlit as st
import pandas as pd
import requests

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="ButacaVip Buscador",
    page_icon="🔎",
    layout="wide"
)

# --- TU CLAVE API (La llave maestra) ---
API_KEY = "5c88939574e202d8432edcb638e08e10"
BASE_URL = "https://image.tmdb.org/t/p/w500"  # Para las fotos

# --- ESTILOS CSS (AZUL PROFESIONAL) ---
st.markdown("""
<style>
    .stButton>button {
        color: white;
        background-color: #2E86C1;
        border-color: #2E86C1;
    }
    .stTextInput>div>div>input {
        color: #2E86C1;
    }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("🎬 ButacaVip: Buscador Global")
st.markdown("Conectado a **The Movie Database (TMDB)** en tiempo real.")
st.markdown("---")

# --- BARRA DE BÚSQUEDA ---
col1, col2 = st.columns([3, 1])
with col1:
    busqueda = st.text_input("🔍 Escribe el nombre de una película:", placeholder="Ej: Matrix, Titanic, Batman...")
with col2:
    st.write("")
    st.write("") 
    buscar_btn = st.button("Buscar Película 🚀", use_container_width=True)

# --- LÓGICA DE BÚSQUEDA ---
if busqueda or buscar_btn:
    if not busqueda:
        st.warning("⚠️ Por favor, escribe algo para buscar.")
    else:
        try:
            # 1. CONECTAR CON LA API
            url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={busqueda}&language=es-ES"
            respuesta = requests.get(url)
            datos = respuesta.json()

            # 2. VER SI HAY RESULTADOS
            if datos['results']:
                lista_pelis = datos['results']
                st.success(f"✅ Se han encontrado {len(lista_pelis)} resultados para '{busqueda}'.")
                
                # 3. MOSTRAR RESULTADOS EN REJILLA (GRID)
                # Creamos columnas de 4 en 4
                cols = st.columns(4)
                for i, peli in enumerate(lista_pelis):
                    # Solo mostramos las primeras 12 para no saturar
                    if i >= 12: break
                    
                    with cols[i % 4]:
                        # Título
                        st.markdown(f"### {peli['title']}")
                        
                        # Imagen (Si no tiene, ponemos una gris)
                        if peli['poster_path']:
                            img_url = BASE_URL + peli['poster_path']
                            st.image(img_url, use_container_width=True)
                        else:
                            st.info("🖼️ Sin imagen disponible")
                        
                        # Datos
                        st.caption(f"📅 Fecha: {peli.get('release_date', 'Desconocida')}")
                        st.markdown(f"⭐ **Nota: {peli['vote_average']}/10**")
                        
                        # Sinopsis (con desplegable para no ocupar mucho)
                        with st.expander("Leer Sinopsis"):
                            st.write(peli['overview'] if peli['overview'] else "Sin descripción disponible.")
                        
                        st.markdown("---")
            else:
                st.error("❌ No se encontraron películas con ese nombre.")

        except Exception as e:
            st.error(f"Error de conexión: {e}")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown("Datos proporcionados por **TMDB**. Desarrollado por **Eduard289**.")
