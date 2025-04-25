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

# Section: Why Python?
def show_why_python():
    st.title("¿Por qué Python para Datos de Salud?")
    
    # Comparison with other tools
    st.subheader("Comparación con otras herramientas")
    
    comparison_data = {
        "Criterio": ["Curva de aprendizaje", "Flexibilidad", "Reproducibilidad", "Visualización", "Análisis estadístico", "Automatización", "Costo"],
        "Python": ["Moderada", "Muy alta", "Excelente", "Excelente", "Muy bueno", "Excelente", "Gratis"],
        "R": ["Moderada", "Alta", "Excelente", "Muy buena", "Excelente", "Buena", "Gratis"],
        "Excel": ["Baja", "Limitada", "Limitada", "Básica", "Básica", "Limitada", "Pagado"],
        "SPSS": ["Baja", "Limitada", "Buena", "Buena", "Excelente", "Limitada", "Muy costoso"]
    }
    
    comparison_df = pd.DataFrame(comparison_data)
    st.table(comparison_df.set_index("Criterio"))
    
    st.markdown("---")
    
    # Benefits visualized
    st.subheader("Beneficios para Profesionales de la Salud")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        benefits = {
            "Ahorro de tiempo": 85,
            "Reproducibilidad": 95,
            "Análisis complejos": 90,
            "Automatización": 80,
            "Visualización avanzada": 85
        }
        
        fig = go.Figure([go.Bar(
            x=list(benefits.values()),
            y=list(benefits.keys()),
            orientation='h',
            marker=dict(
                color=['#2A9D8F', '#E9C46A', '#F4A261', '#E76F51', '#264653'],
                line=dict(color='rgba(0, 0, 0, 0.1)', width=1)
            )
        )])
        
        fig.update_layout(
