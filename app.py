import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import time
import base64
from streamlit_lottie import st_lottie
import requests
import json

# Set page config MUST be first Streamlit call
st.set_page_config(
    page_title="Python for Health Data - Interactive Guide",
    layout="wide",
    page_icon="🩺"
)

# -- Function to load Lottie animations --
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -- Load animations --
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_health = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_5njp3vgg.json")
lottie_chart = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_xlkxtmul.json")

# -- Custom Styles for Colors, Fonts & Layout --
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&family=Poppins:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        background-color: #f8f9fa;
    }
    
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header container with gradient */
    .header-container {
        position: fixed;
        top: 10px;
        left: 20px;
        text-align: left;
        padding: 15px 20px;
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(240,248,255,0.95));
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        z-index: 1000;
        border-left: 5px solid #2A9D8F;
    }
    
    .header-container h1 {
        margin: 0;
        font-size: 1.4rem;
        color: #1e3a8a;
        font-weight: 700;
    }
    
    .header-container hr {
        width: 60px;
        border: 2px solid #F4A261;
        margin: 6px 0;
    }
    
    .header-container h4 {
        margin: 0;
        font-size: 1rem;
        color: #2A9D8F;
        font-weight: 500;
    }
    
    /* Custom card styling */
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-top: 4px solid #2A9D8F;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #2A9D8F;
        color: white;
        border-radius: 5px;
        padding: 5px 15px;
        font-weight: 500;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #1e7d71;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Code block styling */
    code {
        border-radius: 5px;
        background-color: #f1f3f5 !important;
        color: #333 !important;
        padding: 4px 6px !important;
        font-family: 'Consolas', monospace !important;
    }
    
    /* Sidebar improvements */
    .stSidebar {
        background-color: #FFFFFF;
        box-shadow: 2px 0 5px rgba(0,0,0,0.05);
    }
    
    /* Main content spacing */
    .css-18e3th9 {
        padding-top: 100px;
    }
    
    /* Section headers with underline */
    h2 {
        border-bottom: 2px solid #F4A261;
        padding-bottom: 8px;
        margin-bottom: 20px;
    }
    
    /* Subheaders with accent color */
    h3 {
        color: #2A9D8F;
        margin-top: 30px;
    }
    
    /* Radio buttons in sidebar */
    .stRadio > div {
        padding: 10px;
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    
    /* Custom progress bar */
    .stProgress > div > div {
        background-color: #2A9D8F;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 4px 8px;
        background-color: #e9ecef;
        color: #495057;
        border-radius: 4px;
        font-size: 0.8rem;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    
    .badge-python {
        background-color: #306998;
        color: white;
    }
    
    .badge-pandas {
        background-color: #130654;
        color: white;
    }
    
    .badge-viz {
        background-color: #E86444;
        color: white;
    }
    
    /* Timeline styling */
    .timeline-item {
        padding-left: 20px;
        border-left: 2px solid #2A9D8F;
        padding-bottom: 15px;
        position: relative;
    }
    
    .timeline-item:before {
        content: "";
        position: absolute;
        left: -8px;
        top: 0;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #2A9D8F;
    }
    
    /* Info box */
    .info-box {
        background-color: #e7f5ff;
        border-left: 4px solid #1e88e5;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    /* Warning box */
    .warning-box {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    /* Success box */
    .success-box {
        background-color: #e8f5e9;
        border-left: 4px solid #43a047;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    /* Code expander */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #2A9D8F;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a sample dataset for demonstrations
@st.cache_data
def create_sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    np.random.seed(42)
    
    # Create seasonal pattern with peaks every few months
    seasonal = 10 * np.sin(np.linspace(0, 4*np.pi, len(dates)))
    
    # Add trend
    trend = np.linspace(20, 40, len(dates))
    
    # Add noise
    noise = np.random.normal(0, 5, len(dates))
    
    # Combine components
    cases = trend + seasonal + noise
    cases = np.maximum(cases, 0)  # No negative cases
    
    # Add some anomaly days (outbreaks)
    outbreak_days = [50, 150, 250]
    for day in outbreak_days:
        cases[day:day+14] += np.random.randint(10, 30)
    
    # Demographics data
    age_groups = ['0-18', '19-35', '36-50', '51-65', '65+']
    gender = ['Male', 'Female']
    
    # Create patient records
    data = {
        'date': dates,
        'cases': cases.astype(int),
        'recovered': (cases * 0.8).astype(int),
        'tests': (cases * np.random.randint(5, 15, len(dates))).astype(int),
        'age_group': np.random.choice(age_groups, len(dates)),
        'gender': np.random.choice(gender, len(dates), p=[0.48, 0.52]),
        'region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], len(dates)),
        'hospitalized': (cases * 0.12).astype(int)
    }
    
    df = pd.DataFrame(data)
    return df

# Function to show header on every page
def show_header():
    st.markdown(
        """
        <div class="header-container">
            <h1>Dra. Aura Victoria Gutiérrez</h1>
            <hr />
            <h4>MD, Clinical Epidemiologist</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

# Function to show custom card
def show_card(title, content, key=None):
    st.markdown(f"""
    <div class="card">
        <h3>{title}</h3>
        {content}
    </div>
    """, unsafe_allow_html=True)

# Function to create badges
def badge(text, badge_type=""):
    return f'<span class="badge {badge_type}">{text}</span>'

# Function to display info box
def info_box(text):
    st.markdown(f'<div class="info-box">📘 {text}</div>', unsafe_allow_html=True)

# Function to display warning box
def warning_box(text):
    st.markdown(f'<div class="warning-box">⚠️ {text}</div>', unsafe_allow_html=True)

# Function to display success box
def success_box(text):
    st.markdown(f'<div class="success-box">✅ {text}</div>', unsafe_allow_html=True)

# Function to display timeline item
def timeline_item(title, content):
    st.markdown(f"""
    <div class="timeline-item">
        <h4>{title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

# Main app function
def main():
    # Display the custom header
    show_header()
    
    # Create sample data
    df = create_sample_data()

    # Sidebar with improved styling
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/python.png", width=80)
        st.title("Guía Interactiva")
        
        # Tracking progress
        progress = st.progress(0)
        
        # Navigation with hover effects
        st.markdown("""
        <style>
        div.stRadio > div:hover {
            background-color: #edf7f6;
            cursor: pointer;
            transition: background 0.3s;
        }
        </style>
        """, unsafe_allow_html=True)
        
        page = st.radio(
            "Navegación", [
                "🏠 Introducción",
                "🐍 ¿Qué es Python?",
                "📊 ¿Por qué Python?",
                "⚙️ Configuración del Entorno",
                "👨‍💻 Tu Primer Script",
                "📋 Cargar y Visualizar Datos",
                "🔤 Entender Tipos de Datos",
                "🎨 Personalizar y Guardar Gráficos",
                "📱 Gráficos Interactivos",
                "🧮 Análisis Estadístico",
                "🔄 Flujos de Trabajo",
                "📚 Descargar eBook"
            ]
        )
        
        # Dynamic progress based on page selection
        page_index = [
            "🏠 Introducción",
            "🐍 ¿Qué es Python?",
            "📊 ¿Por qué Python?",
            "⚙️ Configuración del Entorno",
            "👨‍💻 Tu Primer Script",
            "📋 Cargar y Visualizar Datos",
            "🔤 Entender Tipos de Datos",
            "🎨 Personalizar y Guardar Gráficos",
            "📱 Gráficos Interactivos",
            "🧮 Análisis Estadístico",
            "🔄 Flujos de Trabajo",
            "📚 Descargar eBook"
        ].index(page)
        progress_value = (page_index + 1) / 12
        progress.progress(progress_value)
        
        # Track and show progress
        st.caption(f"Progreso: {int(progress_value * 100)}%")
        
        # Easter egg in sidebar
        if st.button("💡 Tip del día"):
            tips = [
                "Usa 'df.info()' para ver rápidamente los tipos de datos y valores faltantes.",
                "El método '.describe()' funciona para columnas categóricas con 'include=\"object\"'.",
                "Crea una copia con 'df.copy()' antes de modificar un DataFrame para evitar sorpresas.",
                "f-strings (f'texto {variable}') son más rápidos y legibles que concatenar strings.",
                "Usa 'plt.tight_layout()' para evitar que tus etiquetas se solapen en matplotlib."
            ]
            st.info(np.random.choice(tips))
        
        st.markdown("---")
        st.markdown("📧 contacto@auragutierrez.md")

    # Main content area based on page selection
    if page == "🏠 Introducción":
        show_introduction()
    elif page == "🐍 ¿Qué es Python?":
        show_what_is_python()
    elif page == "📊 ¿Por qué Python?":
        show_why_python()
    elif page == "⚙️ Configuración del Entorno":
        show_setup()
    elif page == "👨‍💻 Tu Primer Script":
        show_hello_world()
    elif page == "📋 Cargar y Visualizar Datos":
        show_load_preview(df)
    elif page == "🔤 Entender Tipos de Datos":
        show_data_types(df)
    elif page == "🎨 Personalizar y Guardar Gráficos":
        show_customize_plots(df)
    elif page == "📱 Gráficos Interactivos":
        show_interactive(df)
    elif page == "🧮 Análisis Estadístico":
        show_statistics(df)
    elif page == "🔄 Flujos de Trabajo":
        show_workflows()
    elif page == "📚 Descargar eBook":
        show_download()

# Section: Introduction with animation
def show_introduction():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Python para Datos de Salud")
        st.subheader("Una Guía Completa para Principiantes")
        
        st.markdown("""
        **Sin jerga, sin suposiciones previas.** En esta guía, cada sección se divide en pequeños pasos que 
        cualquiera puede seguir, desde la instalación de Python hasta la creación de gráficos interactivos.
        """)
        
        info_box("""
        Este tutorial está diseñado para profesionales de la salud sin experiencia previa en programación.
        Si ya tienes experiencia con Python, puedes saltar directamente a las secciones más avanzadas.
        """)
    
    with col2:
        st_lottie(lottie_health, height=200, key="intro_animation")
    
    st.markdown("---")
    
    # What you'll learn section
    st.header("Lo que aprenderás")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        show_card("Fundamentos", f"""
        {badge("Python Básico", "badge-python")}
        {badge("Pandas", "badge-pandas")}
        {badge("Matplotlib", "badge-viz")}
        <ul>
            <li>Sintaxis de Python</li>
            <li>Estructuras de datos</li>
            <li>Manipulación de datos</li>
        </ul>
        """)
        
    with col2:
        show_card("Análisis & Visualización", f"""
        {badge("Estadística", "badge-python")}
        {badge("Gráficos", "badge-viz")}
        <ul>
            <li>Estadísticas descriptivas</li>
            <li>Visualizaciones estáticas</li>
            <li>Gráficos interactivos</li>
        </ul>
        """)
        
    with col3:
        show_card("Aplicaciones Prácticas", f"""
        {badge("Streamlit", "badge-python")}
        {badge("Workflow", "badge-pandas")}
        <ul>
            <li>Aplicaciones web</li>
            <li>Automatización</li>
            <li>Reportes dinámicos</li>
        </ul>
        """)
    
    # Testimonials
    st.header("Lo que dicen nuestros estudiantes")
    
    testimonial_cols = st.columns(3)
    
    testimonials = [
        {"name": "Dr. Carlos Méndez", "role": "Médico Epidemiólogo", "text": "Esta guía me permitió automatizar el análisis de datos COVID en mi hospital en menos de un mes."},
        {"name": "Dra. Laura Sánchez", "role": "Investigadora Clínica", "text": "Nunca pensé que podría programar, pero esta guía me mostró que cualquiera puede aprender Python para datos de salud."},
        {"name": "David Torres", "role": "Estudiante de Medicina", "text": "Los ejemplos prácticos me ayudaron a entender cómo puedo aplicar Python a mi investigación de tesis."}
    ]
    
    for i, col in enumerate(testimonial_cols):
        with col:
            st.markdown(f"""
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; height: 200px;">
                <div style="color: #2A9D8F; font-size: 24px;">"</div>
                <p style="font-style: italic;">{testimonials[i]['text']}</p>
                <div style="margin-top: 20px;">
                    <p style="margin: 0; font-weight: bold;">{testimonials[i]['name']}</p>
                    <p style="margin: 0; font-size: 0.9rem; color: #6c757d;">{testimonials[i]['role']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # FAQ Expander
    with st.expander("Preguntas Frecuentes"):
        st.markdown("""
        **¿Necesito experiencia previa en programación?**
        
        No, esta guía está diseñada para principiantes absolutos.
        
        **¿Cuánto tiempo lleva completar el tutorial?**
        
        El tutorial completo puede completarse en aproximadamente 4-6 horas, pero recomendamos dividirlo en sesiones de 1 hora.
        
        **¿Qué tipo de datos de salud puedo analizar con Python?**
        
        Prácticamente cualquier dato estructurado: registros de pacientes, resultados de laboratorio, datos epidemiológicos, imágenes médicas (con bibliotecas adicionales), y más.
        """)

# Section: What is Python? with animation
def show_what_is_python():
    st.title("¿Qué es Python?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Paso 1: Entender Python")
        st.write(
            """
            Python es un **lenguaje de programación** utilizado para escribir instrucciones que una computadora puede ejecutar.
            A diferencia de otros lenguajes, Python prioriza la legibilidad y simplicidad.
            """
        )
        
        timeline_item("1991", "Guido van Rossum crea Python con enfoque en la simplicidad y legibilidad")
        timeline_item("2000s", "Emergen bibliotecas científicas como NumPy y pandas")
        timeline_item("2010s", "Python se convierte en lenguaje preferido para ciencia de datos")
        timeline_item("Hoy", "Uno de los lenguajes más populares para análisis de datos en salud")
        
    with col2:
        st_lottie(lottie_coding, height=300, key="python_animation")
    
    st.markdown("---")
    
    st.subheader("Paso 2: ¿Por qué Python es especial?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        show_card("Legible", """
        <p>Sintaxis que se parece al inglés y usa indentación para estructurar el código, no llaves o puntos y comas.</p>
        <pre><code># Ejemplo de legibilidad
if paciente_edad > 65:
    print("Grupo de riesgo")
else:
    print("No en grupo de riesgo")</code></pre>
        """)
        
    with col2:
        show_card("Versátil", """
        <p>El mismo lenguaje sirve para análisis de datos, desarrollo web, inteligencia artificial, automatización y más.</p>
        <p>Tiene bibliotecas específicas para cada campo:</p>
        <ul>
            <li>Pandas para datos tabulares</li>
            <li>Matplotlib para visualización</li>
            <li>Scikit-learn para machine learning</li>
        </ul>
        """)
        
    with col3:
        show_card("Comunidad Enorme", """
        <p>Millones de desarrolladores y científicos comparten código, resuelven problemas y crean recursos.</p>
        <p>Recursos principales:</p>
        <ul>
            <li>Stack Overflow</li>
            <li>GitHub</li>
            <li>PyPI (Python Package Index)</li>
        </ul>
        """)
    
    st.markdown("---")
    
    st.subheader("Paso 3: Prueba el Intérprete de Python")
    
    with st.expander("Ver Demo del Intérprete de Python"):
        st.code("""
>>> python3
Python 3.9.7 (default, Sep 16 2021, 13:09:58)
>>> print('¡Hola, Python!')
¡Hola, Python!
>>> 2 + 3
5
>>> pacientes = ['Juan', 'María', 'Carlos']
>>> for paciente in pacientes:
...     print(f"Analizando datos de {paciente}")
... 
Analizando datos de Juan
Analizando datos de María
Analizando datos de Carlos
>>> exit()
        """)
    
    warning_box("""
    No te preocupes si esto parece confuso ahora. Pronto estarás escribiendo tu propio código Python 
    y entenderás cómo funciona cada parte.
    """)

def show_why_python():
    st.title("¿Por qué Python para Datos de Salud?")

    # Comparación con otras herramientas
    st.subheader("Comparación con otras herramientas")
    comparison_data = {
        "Criterio": [
            "Curva de aprendizaje", "Flexibilidad", "Reproducibilidad",
            "Visualización", "Análisis estadístico", "Automatización", "Costo"
        ],
        "Python":   ["Moderada", "Muy alta", "Excelente", "Excelente", "Muy bueno", "Excelente", "Gratis"],
        "R":        ["Moderada", "Alta",    "Excelente", "Muy buena","Excelente",  "Buena",    "Gratis"],
        "Excel":    ["Baja",     "Limitada","Limitada",  "Básica",  "Básica",    "Limitada", "Pagado"],
        "SPSS":     ["Baja",     "Limitada","Buena",     "Buena",   "Excelente", "Limitada", "Muy costoso"]
    }
    df = pd.DataFrame(comparison_data)
    st.table(df.set_index("Criterio"))
    st.markdown("---")

    # Beneficios visualizados
    st.subheader("Beneficios para Profesionales de la Salud")
    col1, col2 = st.columns([2, 1])

    with col1:
        benefits = {
            "Ahorro de tiempo":      85,
            "Reproducibilidad":       95,
            "Análisis complejos":     90,
            "Automatización":         80,
            "Visualización avanzada": 85
        }
        fig = go.Figure([
            go.Bar(
                x=list(benefits.values()),
                y=list(benefits.keys()),
                orientation='h',
                marker=dict(
                    color=['#2A9D8F', '#E9C46A', '#F4A261', '#E76F51', '#264653'],
                    line=dict(color='rgba(0,0,0,0.1)', width=1)
                )
            )
        ])
        fig.update_layout(
            title="Impacto clave de Python",
            xaxis_title="Puntuación (%)",
            yaxis=dict(autorange="reversed"),
            template="plotly_white",
            margin=dict(l=20, r=20, t=40, b=20),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("""
- **Ahorro de tiempo**  
  Automatiza tareas repetitivas.  
- **Reproducibilidad**  
  Comparte tu código y resultados.  
- **Análisis complejos**  
  Fácil con librerías como Pandas.  
- **Automatización**  
  Genera reportes automáticamente.  
- **Visualización avanzada**  
  Gráficos dinámicos y personalizables.
        """)
        st_lottie(lottie_chart, height=300, key="benefits_animation")

    st.markdown("---")

    # Aplicaciones en el Mundo Real
    st.header("Aplicaciones en el Mundo Real")
    ex1, ex2, ex3 = st.columns(3)
    with ex1:
        st.markdown("""
        ### 🦠 Epidemiología
        - Modelado de brotes
        - Análisis espacial de enfermedades
        - Predicción de propagación
        - Visualización de tendencias
        """)
    with ex2:
        st.markdown("""
        ### 🏥 Gestión Hospitalaria
        - Análisis de flujo de pacientes
        - Optimización de recursos
        - Predicción de readmisiones
        - Dashboards en tiempo real
        """)
    with ex3:
        st.markdown("""
        ### 🧬 Investigación Clínica
        - Análisis de estudios clínicos
        - Procesamiento de datos genómicos
        - Métodos estadísticos avanzados
        - Reportes automáticos
        """)

    st.markdown("---")

    # Caso de Estudio
    st.subheader("Caso de Estudio: Análisis COVID-19")
    with st.expander("Ver Ejemplo de Análisis de Datos COVID"):
        st.code("""
# Cargar datos
covid_df = pd.read_csv('covid_data.csv', parse_dates=['date'])

# Resumen estadístico
print(covid_df.describe())

# Casos por región
import seaborn as sns
sns.barplot(x='region', y='cases', data=covid_df)
plt.title('Casos COVID por Región')
plt.xticks(rotation=45)
plt.tight_layout()

# Tendencia temporal
covid_df.groupby('date')['cases'].sum().plot()
plt.title('Evolución de Casos')
plt.tight_layout()
        """, language="python")

    success_box("Con menos de 20 líneas de código, puedes replicar este análisis que en otros entornos llevaría horas.")

# Section: Environment Setup
def show_setup():
    st.title("Configuración del Entorno")
    
    st.subheader("Opciones de Instalación")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("Opción 1: Google Colab (Recomendada para principiantes)"):
            st.markdown("""
            1. Visita [Google Colab](https://colab.research.google.com/)
            2. Inicia sesión con tu cuenta de Google
            3. Crea un nuevo notebook: Archivo → Nuevo Notebook
            4. ¡Listo! Ya puedes empezar a programar
            
            **Ventajas:**
            * No requiere instalación
            * Incluye todas las bibliotecas necesarias
            * Permite compartir fácilmente
            * Funciona en cualquier dispositivo
            
            **Desventajas:**
            * Requiere conexión a internet
            * Limitaciones de tiempo de ejecución en versión gratuita
            """)
            
            if st.button("Tutorial de Google Colab"):
                st.video("https://www.youtube.com/watch?v=inN8seMm7UI")
    
    with col2:
        with st.expander("Opción 2: Anaconda (Instalación local)"):
            st.markdown("""
            1. Descarga [Anaconda](https://www.anaconda.com/products/individual)
            2. Instala siguiendo las instrucciones
            3. Abre "Anaconda Navigator"
            4. Lanza "Jupyter Notebook" o "Spyder"
            
            **Ventajas:**
            * Funciona sin internet
            * Sin limitaciones de tiempo
            * Entorno completo pre-configurado
            * Mayor control sobre el entorno
            
            **Desventajas:**
            * Requiere espacio en disco (~3GB)
            * Instalación más compleja
            """)
            
            if st.button("Tutorial de Anaconda"):
                st.video("https://www.youtube.com/watch?v=5mDYijMfSzs")
    
    st.markdown("---")
    
    # Essential packages
    st.subheader("Paquetes Esenciales para Datos de Salud")
    
    packages = {
        "pandas": "Manipulación y análisis de datos estructurados",
        "numpy": "Operaciones numéricas y arrays multidimensionales",
        "matplotlib": "Visualizaciones estáticas (gráficos, histogramas)",
        "seaborn": "Visualizaciones estadísticas de alto nivel",
        "plotly": "Gráficos interactivos para exploración",
        "scikit-learn": "Algoritmos de machine learning",
        "statsmodels": "Modelos estadísticos y tests",
        "jupyter": "Notebooks interactivos para análisis"
    }
    
    pkg_df = pd.DataFrame({"Descripción": packages}).reset_index()
    pkg_df.columns = ["Paquete", "Descripción"]
    
    st.table(pkg_df)
    
    # Code snippet for installing packages
    st.subheader("Instalación de Paquetes")
    
    with st.expander("Código para instalar paquetes"):
        st.code("""
# En terminal o línea de comandos:
pip install pandas numpy matplotlib seaborn plotly scikit-learn statsmodels jupyter

# O con conda:
conda install pandas numpy matplotlib seaborn plotly scikit-learn statsmodels jupyter

# En un notebook de Jupyter/Colab:
!pip install pandas numpy matplotlib seaborn plotly scikit-learn statsmodels
        """)
    
    warning_box("""
    Si usas Google Colab, todos estos paquetes ya están instalados por defecto.
    Solo necesitarás instalar paquetes menos comunes.
    """)
    
    # IDE options
    st.subheader("Entornos de Desarrollo (IDE)")
    
    ide_cols = st.columns(3)
    
    ides = [
        {
            "name": "Jupyter Notebook",
            "image": "https://img.icons8.com/fluency/96/jupyter.png",
            "desc": "Ideal para análisis interactivo y prototipado rápido. Permite mezclar código, texto y visualizaciones."
        },
        {
            "name": "VS Code",
            "image": "https://img.icons8.com/color/96/visual-studio-code-2019.png",
            "desc": "Editor versátil con excelente soporte para Python. Bueno para proyectos más grandes y desarrollo."
        },
        {
            "name": "PyCharm",
            "image": "https://img.icons8.com/color/96/pycharm.png",
            "desc": "IDE profesional específico para Python con muchas herramientas integradas. Curva de aprendizaje mayor."
        }
    ]
    
    for i, col in enumerate(ide_cols):
        with col:
            st.image(ides[i]["image"], width=60)
            st.subheader(ides[i]["name"])
            st.write(ides[i]["desc"])
    
    info_box("""
    Para principiantes, recomendamos comenzar con Jupyter Notebook o Google Colab
    por su simplicidad y enfoque interactivo.
    """)

# Section: First script
def show_hello_world():
    st.title("Tu Primer Script Python para Datos de Salud")
    
    st.write("""
    Comenzaremos con algo simple para entender la sintaxis básica de Python y cómo funciona un script.
    Sigue estos pasos para crear y ejecutar tu primer programa.
    """)
    
    # Step 1: Basic script
    st.header("Paso 1: Script Básico")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.code("""
# Mi primer script de Python para datos de salud
print("¡Hola! Bienvenido al análisis de datos de salud con Python")

# Variables para almacenar datos de pacientes
paciente_nombre = "Juan Pérez"
paciente_edad = 45
paciente_hipertension = True
paciente_colesterol = 210.5

# Mostrar información del paciente
print(f"Paciente: {paciente_nombre}")
print(f"Edad: {paciente_edad} años")
print(f"Hipertensión: {paciente_hipertension}")
print(f"Colesterol: {paciente_colesterol} mg/dL")

# Análisis básico
if paciente_edad > 60:
    print("Paciente en grupo de edad avanzada")
else:
    print("Paciente no es de edad avanzada")
    
if paciente_colesterol > 200:
    print("Colesterol elevado - Requiere seguimiento")
        """)
    
    with col2:
        st.write("""
        **Conceptos clave:**
        
        1. **Comentarios** con `#`
        2. **Variables** para almacenar datos
        3. **Tipos de datos**:
           - Texto (string): `"Juan Pérez"`
           - Número entero (int): `45`
           - Booleano (bool): `True`
           - Decimal (float): `210.5`
        4. **Formato de strings** con `f"texto {variable}"`
        5. **Condicionales** con `if/else`
        """)
    
    # Output of the script
    st.subheader("Resultado:")
    st.code("""
¡Hola! Bienvenido al análisis de datos de salud con Python
Paciente: Juan Pérez
Edad: 45 años
Hipertensión: True
Colesterol: 210.5 mg/dL
Paciente no es de edad avanzada
Colesterol elevado - Requiere seguimiento
    """, language="text")
    
    # Step 2: Basic data structures
    st.header("Paso 2: Estructuras de Datos Básicas")
    
    with st.expander("Expandir Ejemplo con Listas y Diccionarios"):
        st.code("""
# Lista de pacientes
pacientes = ["Juan Pérez", "María López", "Carlos Gómez", "Ana Martínez"]

# Imprimir lista de pacientes
print("Lista de pacientes:")
for paciente in pacientes:
    print(f"- {paciente}")

# Acceder a un paciente específico (índice comienza en 0)
print(f"Primer paciente: {pacientes[0]}")
print(f"Último paciente: {pacientes[-1]}")

# Diccionario con datos de paciente
paciente_info = {
    "nombre": "Juan Pérez",
    "edad": 45,
    "hipertension": True,
    "colesterol": 210.5,
    "medicamentos": ["Enalapril", "Aspirina"],
    "ultima_visita": "2023-03-15"
}

# Acceder a datos del diccionario
print(f"Nombre: {paciente_info['nombre']}")
print(f"Medicamentos: {', '.join(paciente_info['medicamentos'])}")

# Lista de diccionarios (formato común para datos tabulares)
todos_pacientes = [
    {"nombre": "Juan Pérez", "edad": 45, "colesterol": 210.5},
    {"nombre": "María López", "edad": 52, "colesterol": 185.2},
    {"nombre": "Carlos Gómez", "edad": 38, "colesterol": 230.1}
]

# Calcular colesterol promedio
total_colesterol = 0
for paciente in todos_pacientes:
    total_colesterol += paciente["colesterol"]

promedio_colesterol = total_colesterol / len(todos_pacientes)
print(f"Colesterol promedio: {promedio_colesterol:.2f} mg/dL")
        """)
        
        st.markdown("""
        **Conceptos nuevos:**
        
        1. **Listas** - Colecciones ordenadas: `["Juan", "María", ...]`
        2. **Diccionarios** - Pares clave-valor: `{"nombre": "Juan", "edad": 45}`
        3. **Bucles `for`** - Para iterar sobre colecciones
        4. **Indexación** - Acceder a elementos: `lista[0]` o `diccionario["clave"]`
        5. **Funciones integradas** - Como `len()` para obtener longitud
        6. **Formato con precisión** - `{valor:.2f}` para 2 decimales
        """)
    
    # Step 3: Functions
    st.header("Paso 3: Crear Funciones")
    
    st.write("Las funciones permiten reutilizar código y organizar mejor tus scripts:")
    
# Paso 3: Crear Funciones
st.header("Paso 3: Crear Funciones")
st.write("Las funciones permiten reutilizar código y organizar mejor tus scripts:")

st.code('''
# Definir una función para calcular IMC
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)
    
    Parámetros:
    peso -- en kilogramos (float)
    altura -- en metros (float)
    
    Retorna:
    IMC como float
    """
    if altura <= 0:
        return None  # Evitar división por cero
    
    imc = peso / (altura ** 2)
    return imc

# Definir función para interpretar IMC
def interpretar_imc(imc):
    """
    Interpreta el valor del IMC según categorías estándar
    
    Parámetros:
    imc -- Índice de Masa Corporal (float)
    
    Retorna:
    Categoría como string
    """
    if imc is None:
        return "Error en el cálculo"
    elif imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Usar las funciones con datos de pacientes
pacientes_datos = [
    {"nombre": "Juan Pérez", "peso": 85.5, "altura": 1.75},
    {"nombre": "María López", "peso": 62.0, "altura": 1.65},
    {"nombre": "Carlos Gómez", "peso": 79.2, "altura": 1.70}
]

# Analizar cada paciente
for paciente in pacientes_datos:
    nombre = paciente["nombre"]
    peso = paciente["peso"]
    altura = paciente["altura"]
    
    imc = calcular_imc(peso, altura)
    categoria = interpretar_imc(imc)
    
    print(f"{nombre}: IMC = {imc:.2f}, Categoría: {categoria}")
''', language="python")

st.subheader("Resultado:")
st.code('''
Juan Pérez: IMC = 27.92, Categoría: Sobrepeso
María López: IMC = 22.77, Categoría: Peso normal
Carlos Gómez: IMC = 27.40, Categoría: Sobrepeso
''', language="text")

# Section: Load and preview data
def show_load_preview(df):
    st.title("Cargar y Visualizar Datos")
    
    st.write("""
    En el mundo real, los datos de salud suelen venir en archivos CSV, Excel, o bases de datos.
    Python tiene herramientas excelentes para trabajar con ellos, principalmente la biblioteca **pandas**.
    """)
    
    # Step 1: Loading data
    st.header("Paso 1: Cargar Datos")
    
    loading_code = """
# Importar pandas, la biblioteca principal para datos tabulares
import pandas as pd

# Cargar datos desde diferentes fuentes
# Desde CSV
df = pd.read_csv('datos_pacientes.csv')

# Desde Excel
df_excel = pd.read_excel('datos_hospital.xlsx', sheet_name='Admisiones')

# Desde SQL (requiere biblioteca adicional)
import sqlite3
conn = sqlite3.connect('hospital.db')
df_sql = pd.read_sql('SELECT * FROM pacientes', conn)

# Ver las primeras filas para confirmar que se cargó correctamente
print(df.head())
    """
    
    st.code(loading_code)
    
    # Step 2: Exploring data
    st.header("Paso 2: Explorar los Datos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Métodos de exploración básicos")
        exploration_code = """
# Ver las primeras 5 filas
print(df.head())

# Ver las últimas 5 filas
print(df.tail())

# Información sobre el DataFrame
print(df.info())

# Estadísticas descriptivas
print(df.describe())

# Dimensiones (filas, columnas)
print(f"Dimensiones: {df.shape}")

# Nombres de columnas
print(f"Columnas: {df.columns.tolist()}")

# Valores únicos en una columna
print(f"Regiones: {df['region'].unique()}")

# Contar valores en una columna
print(df['gender'].value_counts())
        """
        st.code(exploration_code)
    
    with col2:
        st.subheader("Ejemplo con datos reales")
        st.dataframe(df.head())
        st.code("""
# Información del DataFrame
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 365 entries, 0 to 364
Data columns (total 8 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   date         365 non-null    datetime64[ns]
 1   cases        365 non-null    int64         
 2   recovered    365 non-null    int64         
 3   tests        365 non-null    int64         
 4   age_group    365 non-null    object        
 5   gender       365 non-null    object        
 6   region       365 non-null    object        
 7   hospitalized 365 non-null    int64         
dtypes: datetime64[ns](1), int64(4), object(3)
memory usage: 22.9+ KB
        """)
    
    # Step 3: Basic visualization
    st.header("Paso 3: Visualización Básica")
    
    st.write("Pandas incluye funcionalidad básica de visualización basada en matplotlib:")
    
    viz_code = """
# Importar matplotlib para personalizar gráficos
import matplotlib.pyplot as plt

# Configurar tamaño de figura por defecto
plt.figure(figsize=(10, 6))

# Gráfico de líneas simple para casos en el tiempo
df.plot(x='date', y='cases', title='Casos Diarios')
plt.ylabel('Número de casos')
plt.grid(True, alpha=0.3)
plt.savefig('casos_diarios.png')  # Guardar gráfico

# Gráfico de barras para casos por región
casos_por_region = df.groupby('region')['cases'].sum().sort_values(ascending=False)
casos_por_region.plot(kind='bar', title='Total de Casos por Región')
plt.ylabel('Número de casos')
plt.grid(True, alpha=0.3)
plt.tight_layout()  # Ajustar layout

# Histograma de una variable
df['hospitalized'].plot(kind='hist', bins=20, title='Distribución de Hospitalizaciones')

# Diagrama de caja (boxplot)
df.boxplot(column='cases', by='region', figsize=(10, 6))
plt.title('Distribución de Casos por Región')
plt.suptitle('')  # Eliminar título automático
    """
    
    st.code(viz_code)
    
    # Example plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(x='date', y='cases', ax=ax, title='Casos Diarios')
    ax.set_ylabel('Número de casos')
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    # Step 4: Basic data manipulation
    st.header("Paso 4: Manipulación Básica de Datos")
    
    manipulation_code = """
# Filtrar datos
solo_norte = df[df['region'] == 'North']
alta_hospitalizacion = df[df['hospitalized'] > 5]
multiples_condiciones = df[(df['gender'] == 'Male') & (df['age_group'] == '65+')]

# Crear nuevas columnas
df['tasa_positivos'] = df['cases'] / df['tests'] * 100
df['fecha_texto'] = df['date'].dt.strftime('%b %d')  # Convertir fecha a formato texto

# Agrupar y agregar datos
por_region = df.groupby('region').agg({
    'cases': 'sum',
    'tests': 'sum',
    'hospitalized': 'mean'
})
por_region['tasa_hospitalizacion'] = por_region['hospitalized'] / por_region['cases'] * 100

# Ordenar datos
mas_casos = por_region.sort_values('cases', ascending=False)

# Unir (merge) conjuntos de datos
# Supongamos que tenemos otro DataFrame con información adicional por región
info_regiones = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West', 'Central'],
    'poblacion': [2.1, 3.5, 2.7, 4.2, 3.8],  # en millones
    'hospitales': [12, 15, 8, 20, 14]
})

# Unir los DataFrames
datos_completos = por_region.merge(info_regiones, on='region')

# Calcular tasas por millón
datos_completos['casos_por_millon'] = datos_completos['cases'] / datos_completos['poblacion']
    """
    
    with st.expander("Ver código de manipulación de datos"):
        st.code(manipulation_code)
    
    # Tips
    info_box("""
    Consejo profesional: pandas tiene más de 200 funciones para manipular datos.
    No intentes memorizarlas todas - aprende los conceptos básicos y consulta la documentación
    según sea necesario.
    """)
    
    # Challenge
    st.markdown("---")
    st.subheader("Mini Desafío")
    
    st.write("""
    Intenta escribir código para responder a estas preguntas usando los datos de ejemplo:
    
    1. ¿Qué región tiene la mayor proporción de casos que requieren hospitalización?
    2. ¿Cómo se comparan las tasas de casos entre hombres y mujeres?
    3. Crea un gráfico que muestre la evolución de los casos recuperados vs. nuevos en el tiempo.
    """)
    
    if st.button("Ver Soluciones"):
        solution_code = """
# 1. Región con mayor proporción de hospitalización
tasa_hosp = df.groupby('region').agg({
    'hospitalized': 'sum',
    'cases': 'sum'
})
tasa_hosp['prop_hospitalizacion'] = tasa_hosp['hospitalized'] / tasa_hosp['cases'] * 100
region_max_hosp = tasa_hosp.sort_values('prop_hospitalizacion', ascending=False)
print(f"Región con mayor prop. hospitalización: {region_max_hosp.index[0]} ({region_max_hosp['prop_hospitalizacion'].iloc[0]:.2f}%)")

# 2. Comparar tasas entre géneros
por_genero = df.groupby('gender').agg({
    'cases': 'sum',
    'tests': 'sum'
})
por_genero['tasa_positivos'] = por_genero['cases'] / por_genero['tests'] * 100
print(por_genero)

# 3. Gráfico de evolución temporal
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['cases'], label='Nuevos casos')
plt.plot(df['date'], df['recovered'], label='Recuperados')
plt.title('Evolución de Casos vs Recuperados')
plt.xlabel('Fecha')
plt.ylabel('Número')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
        """
        st.code(solution_code)
        
        # Sample visualization for solution 3
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df['date'], df['cases'], label='Nuevos casos')
        ax.plot(df['date'], df['recovered'], label='Recuperados')
        ax.set_title('Evolución de Casos vs Recuperados')
        ax.set_xlabel('Fecha')
        ax.set_ylabel('Número')
        ax.grid(True, alpha=0.3)
        ax.legend()
        plt.tight_layout()
        st.pyplot(fig)

# Function to continue with additional sections
def show_data_types(df):
    st.title("Entender Tipos de Datos")
    
    st.write("""
    En datos de salud, encontrarás diferentes tipos de variables que requieren distintos tratamientos.
    Entender estos tipos es fundamental para el análisis correcto.
    """)
    
    # Types of variables in health data
    st.header("Tipos de Variables en Datos de Salud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Variables Numéricas")
        st.markdown("""
        **Continuas:**
        - Presión arterial: 120/80 mmHg
        - Temperatura: 37.2°C
        - Niveles de glucosa: 95 mg/dL
        - IMC: 24.5
        
        **Discretas:**
        - Número de hospitalizaciones: 2
        - Días de estancia: 5
        - Hijos: 3
        - Medicamentos prescritos: 4
        """)
    
    with col2:
        st.subheader("Variables Categóricas")
        st.markdown("""
        **Nominales (sin orden):**
        - Género: M/F
        - Grupo sanguíneo: A+, B-, O+
        - Diagnóstico: Diabetes, Hipertensión
        - Región: Norte, Sur, Este, Oeste
        
        **Ordinales (con orden):**
        - Severidad: Leve, Moderada, Severa
        - Nivel de dolor: 0-10
        - Estadio de cáncer: I, II, III, IV
        - Clasificación ASA: 1-5
        """)
    
    # Code for identifying data types in pandas
    st.header("Identificar Tipos en Pandas")
    
    identify_code = """
# Ver tipos de datos en el DataFrame
print(df.dtypes)

# Información más detallada
print(df.info())

# Para columnas numéricas
print(df.describe())

# Para columnas categóricas
print(df.describe(include=['object', 'category']))

# Convertir explícitamente a tipos específicos
df['gender'] = df['gender'].astype('category')
df['severity'] = df['severity'].astype('category')

# Para variables ordinales, especificar el orden
df['severity'] = pd.Categorical(
    df['severity'],
    categories=['Mild', 'Moderate', 'Severe'],
    ordered=True
)

# Convertir fechas
df['admission_date'] = pd.to_datetime(df['admission_date'])
    """
    
    st.code(identify_code)
    
    # Working with different data types
    st.header("Trabajar con Diferentes Tipos de Datos")
    
    datatypes_tabs = st.tabs(["Numéricos", "Categóricos", "Fechas", "Texto"])
    
    with datatypes_tabs[0]:
        st.subheader("Datos Numéricos")
        st.code("""
# Estadísticas descriptivas
print(df['age'].describe())

# Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=20, edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')

# Normalizar valores numéricos (útil para machine learning)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['age_normalized'] = scaler.fit_transform(df[['age']])

# Crear categorías a partir de datos numéricos
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 35, 50, 65, 100],
    labels=['0-18', '19-35', '36-50', '51-65', '65+']
)
        """)
        
        # Example with
