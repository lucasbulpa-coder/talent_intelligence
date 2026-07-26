import streamlit as st

st.set_page_config(page_title="Dashboard | Talent Intelligence", layout="wide", initial_sidebar_state="collapsed")

# 1. Inyección de CSS (KPIs, Cajas de Gráficos e Insight)
st.markdown("""
<style>
    .top-navbar { display: flex; justify-content: space-between; align-items: center; padding-bottom: 1rem; border-bottom: 1px solid #2D3748; margin-bottom: 2rem; }
    .nav-breadcrumbs { color: #8F9BBA; font-size: 1.1rem; }
    .nav-breadcrumbs span { color: #ffffff; font-weight: 600; }
    
    /* Contenedor de KPIs */
    .kpi-container { display: flex; gap: 1rem; margin-bottom: 2rem; }
    .kpi-box { flex: 1; background-color: #161b26; border: 1px solid #2D3748; border-radius: 8px; padding: 1.5rem; text-align: center; transition: all 0.3s ease; }
    .kpi-box:hover { border-color: #00E5FF; transform: translateY(-3px); box-shadow: 0 4px 15px rgba(0, 229, 255, 0.05); }
    .kpi-value { color: #00E5FF; font-size: 2.2rem; font-weight: 700; margin-bottom: 0.3rem; }
    .kpi-label { color: #ffffff; font-size: 0.95rem; font-weight: 600; }
    
    /* Contenedor de Gráficos Modulares */
    .chart-container { display: flex; gap: 1rem; margin-bottom: 2rem; }
    .chart-box { flex: 1; background-color: #161b26; border: 1px solid #2D3748; border-radius: 8px; padding: 1.5rem; height: 260px; display:flex; flex-direction: column; justify-content: space-between; }
    .chart-title { color: #8F9BBA; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; margin-bottom: 1rem; letter-spacing: 1px; }
    .chart-placeholder { color: #2D3748; text-align: center; font-size: 0.95rem; margin: auto; font-style: italic; }
    
    /* Caja de Plusvalía Estratégica */
    .insight-box { background: linear-gradient(145deg, #161b26, #1a2233); border-left: 4px solid #00E5FF; padding: 1.8rem; border-radius: 8px; }
    .insight-title { color: #00E5FF; font-size: 0.95rem; font-weight: 700; text-transform: uppercase; margin-bottom: 0.8rem; letter-spacing: 1px;}
    .insight-text { color: #ffffff; font-size: 1.1rem; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# 2. Navegación Superior
st.markdown("""
<div class="top-navbar">
    <div class="nav-breadcrumbs">Talent Intelligence &nbsp; › &nbsp; <span>Dashboard</span></div>
    <div style="background-color: #00E5FF; color: #0b0f19; width: 35px; height: 35px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;">MJ</div>
</div>
""", unsafe_allow_html=True)

st.title("Panel ejecutivo de talento")

# 3. KPIs Superiores (Resumen Ejecutivo)
st.markdown("""
<div class="kpi-container">
    <div class="kpi-box">
        <div class="kpi-value">1.248</div>
        <div class="kpi-label">Colaboradores</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">67%</div>
        <div class="kpi-label">Cobertura skills</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">12</div>
        <div class="kpi-label">Vacantes abiertas</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">8</div>
        <div class="kpi-label">Ajustes de renta</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Estructura de Gráficos (Placeholders listos para Plotly/Altair)
st.markdown("""
<div class="chart-container">
    <div class="chart-box">
        <div class="chart-title">Brecha de habilidades</div>
        <div class="chart-placeholder">[Espacio para Gráfico Radar / Spider Chart]</div>
    </div>
    <div class="chart-box">
        <div class="chart-title">Pipeline de talento</div>
        <div class="chart-placeholder">[Espacio para Gráfico de Embudo / Funnel]</div>
    </div>
    <div class="chart-box">
        <div class="chart-title">Movilidad interna</div>
        <div class="chart-placeholder">[Espacio para Gráfico de Flujo / Sankey]</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Plusvalía y Conclusión Estratégica
st.markdown("""
<div class="insight-box">
    <div class="insight-title">Plusvalía</div>
    <div class="insight-text">La plataforma conecta habilidades, movilidad y compensación: 67% de cobertura de skills y 12 vacantes cubiertas internamente este semestre, reduciendo costos de reclutamiento externo.</div>
</div>
""", unsafe_allow_html=True)