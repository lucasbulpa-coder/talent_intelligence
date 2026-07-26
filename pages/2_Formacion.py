import streamlit as st

st.set_page_config(page_title="Formación | Talent Intelligence", layout="wide", initial_sidebar_state="collapsed")

# CSS Específico para la vista de Formación (Barras de progreso y Cajas de Insight)
st.markdown("""
<style>
    .top-navbar { display: flex; justify-content: space-between; align-items: center; padding-bottom: 1rem; border-bottom: 1px solid #2D3748; margin-bottom: 2rem; }
    .nav-breadcrumbs { color: #8F9BBA; font-size: 1.1rem; }
    .nav-breadcrumbs span { color: #ffffff; font-weight: 600; }
    .insight-box { background: linear-gradient(145deg, #161b26, #1a2233); border-left: 4px solid #00E5FF; padding: 1.5rem; border-radius: 8px; margin-top: 1rem; }
    .insight-title { color: #8F9BBA; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0.5rem; }
    .insight-text { color: #ffffff; font-size: 1.1rem; line-height: 1.4; }
    
    /* Barras de progreso CSS puras */
    .skill-container { margin-bottom: 1rem; }
    .skill-header { display: flex; justify-content: space-between; color: #ffffff; font-size: 0.9rem; margin-bottom: 0.3rem; }
    .progress-bar-bg { background-color: #2D3748; border-radius: 4px; height: 8px; width: 100%; overflow: hidden; }
    .progress-bar-fill { background-color: #00E5FF; height: 100%; border-radius: 4px; }
    .progress-bar-fill.potential { background-color: #8F9BBA; }
</style>
""", unsafe_allow_html=True)

# Navegación Superior
st.markdown("""
<div class="top-navbar">
    <div class="nav-breadcrumbs">Talent Intelligence &nbsp; › &nbsp; <span>Formación</span></div>
    <div style="background-color: #00E5FF; color: #0b0f19; width: 35px; height: 35px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;">MJ</div>
</div>
""", unsafe_allow_html=True)

st.title("Mapa de habilidades")

# Pestañas Superiores (Mockup)
tab1, tab2, tab3 = st.tabs(["Por Cargo", "Por Skill", "Por Colaborador"])

with tab1:
    col_filters, col_data, col_kpi = st.columns([1, 2, 1.2])
    
    with col_filters:
        st.markdown("<h4 style='color:#ffffff; font-size:1rem;'>Filtros</h4>", unsafe_allow_html=True)
        st.selectbox("Empresa", ["Todas", "Banco BICE", "Factoring", "BICECORP"])
        st.selectbox("Gerencia", ["Todas", "Personas", "Digital", "Operaciones"])
        st.selectbox("Cargo", ["Todos", "Analista de Datos", "QA Líder"])

    with col_data:
        st.markdown("<h4 style='color:#8F9BBA; font-size:0.8rem; letter-spacing:1px;'>HABILIDADES PROMEDIO</h4>", unsafe_allow_html=True)
        
        # Generador de barras de progreso HTML para igualar el mockup
        def draw_skill(name, pct, is_potential=False):
            color_class = "potential" if is_potential else ""
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-header"><span>{name}</span><span>{pct}%</span></div>
                <div class="progress-bar-bg"><div class="progress-bar-fill {color_class}" style="width: {pct}%;"></div></div>
            </div>
            """, unsafe_allow_html=True)

        draw_skill("Trabajo en equipo", 82)
        draw_skill("Involucramiento", 76)
        draw_skill("Manejo de SQL", 64)
        draw_skill("Presentación efectiva", 58)
        draw_skill("Programación en Python", 51)
        
        st.markdown("<br><h4 style='color:#8F9BBA; font-size:0.8rem; letter-spacing:1px;'>HABILIDADES POTENCIALES</h4>", unsafe_allow_html=True)
        draw_skill("Análisis de datos", 60, True)
        draw_skill("Manejo de SQL", 55, True)
        draw_skill("Presentación efectiva", 48, True)

    with col_kpi:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <div style="font-size: 4.5rem; font-weight: 700; color: #00E5FF; line-height: 1;">67%</div>
            <div style="color: #ffffff; font-size: 1.1rem; font-weight: 600;">Cobertura global</div>
            <div style="color: #8F9BBA; font-size: 0.9rem;">de skills requeridos cubiertos</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">Insight clave</div>
            <div class="insight-text">El 60% de los colaboradores de mejor desempeño domina el análisis de datos para la toma de decisiones.</div>
        </div>
        """, unsafe_allow_html=True)