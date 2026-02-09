# 🎬 ButacaVip Analytics: Dashboard de Inteligencia Cinematográfica

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B)
![Status](https://img.shields.io/badge/Status-Production-success)
![API](https://img.shields.io/badge/Data-TMDB_v3-green)

**ButacaVip Analytics** es una aplicación web interactiva de análisis de datos (Data Analytics Dashboard) diseñada para la exploración, visualización y comparativa de métricas cinematográficas en tiempo real.

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) ligero que consume datos de la API pública de **The Movie Database (TMDB)**, procesa la información mediante **Pandas** y renderiza visualizaciones dinámicas a través de **Streamlit**.

---

## 🚀 Funcionalidades Técnicas

### 1. Extracción de Datos en Tiempo Real
- **Conexión API REST:** Integración directa con los endpoints de TMDB (`/search/movie`) mediante peticiones HTTPS seguras.
- **Gestión de Respuestas:** Procesamiento de respuestas JSON para estructurar datos no relacionales en DataFrames tabulares.

### 2. Procesamiento y Limpieza de Datos (Pandas)
- **Normalización de Fechas:** Conversión y tipado de strings a objetos `datetime` para análisis de series temporales.
- **Filtrado de Calidad:** Algoritmos de limpieza que descartan registros con datos corruptos (`NaN`), fechas inexistentes o muestras estadísticamente insignificantes (bajo `vote_count`).
- **Indexación:** Reindexación dinámica basada en títulos o años para optimizar la generación de gráficos.

### 3. Visualización y UX/UI
- **Gráficos Interactivos:**
  - **Análisis de Tendencia (Line Chart):** Evolución temporal de la calidad cinematográfica (Rating vs Year).
  - **Ranking Comparativo (Bar Chart):** Distribución de calificaciones por título.
- **CSS Injection:** Personalización avanzada de la interfaz de Streamlit mediante inyección de CSS para adaptar la paleta de colores al branding corporativo (Azul `#2E86C1`).
- **Diseño Responsivo:** Layout fluido (`layout="wide"`) adaptado a dispositivos de escritorio y móviles.

---

## 🛠️ Stack Tecnológico

El proyecto está construido sobre un stack moderno de Python enfocado en Data Science:

| Componente | Tecnología | Uso Principal |
| :--- | :--- | :--- |
| **Lenguaje Core** | Python 3.10+ | Lógica de negocio y scripting. |
| **Frontend Framework** | Streamlit | Renderizado de la Web App y Widgets. |
| **Data Manipulation** | Pandas | Manipulación de estructuras de datos y limpieza. |
| **HTTP Client** | Requests | Comunicación con la API externa. |
| **Data Source** | TMDB API v3 | Fuente de datos bruta (JSON). |
| **Hosting/CI/CD** | Streamlit Cloud | Despliegue continuo desde GitHub. |

---

## 📂 Estructura del Proyecto

```text
dashboard-cine/
├── .streamlit/
│   └── config.toml      # Configuración del tema y servidor (Opcional)
├── app.py               # Punto de entrada (Main Script) y lógica completa
├── requirements.txt     # Dependencias y librerías necesarias
├── README.md            # Documentación técnica del proyecto
└── .gitignore           # Archivos excluidos del control de versiones
