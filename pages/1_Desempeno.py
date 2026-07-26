import streamlit as st

st.set_page_config(page_title="Desempeño | Talent Intelligence", layout="wide", initial_sidebar_state="collapsed")

# 1. Inyección de CSS (KPIs, Insight Box y Matriz 9-Box)
st.markdown("""
<style>
    .top-navbar { display: flex; justify-content: space-between; align-items: center; padding-bottom: 1rem; border-bottom: 1px solid #2D3748; margin-bottom: 2rem; }
    .nav-breadcrumbs { color: #8F9BBA; font-size: 1.1rem; }
    .nav-breadcrumbs span { color: #ffffff; font-weight: 600; }
    
    /* Panel de KPIs */
    .kpi-container { display: flex; gap: 1rem; margin-bottom: 2rem; }
    .kpi-box { flex: 1; background-color: #161b26; border: 1px solid #2D3748; border-radius: 8px; padding: 1.5rem; text-align: center; transition: 0.3s; }
    .kpi-box:hover { border-color: #00E5FF; transform: translateY(-3px); }
    .kpi-value { color: #00E5FF; font-size: 2rem; font-weight: 700; margin-bottom: 0.3rem; }
    .kpi-label { color: #ffffff; font-size: 0.9rem; font-weight: 600; }
    
    /* Insight Box Inferior */
    .insight-box { background: linear-gradient(145deg, #161b26, #1a2233); border-left: 4px solid #00E5FF; padding: 1.5rem; border-radius: 8px; margin-top: 2rem; }
    .insight-title { color: #8F9BBA; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0.5rem; }
    .insight-text { color: #ffffff; font-size: 1.05rem; line-height: 1.5; }
    
    /* Matriz de Desempeño vs Potencial (9-box) */
    .matrix-wrapper { background-color: #161b26; border: 1px solid #2D3748; border-radius: 8px; padding: 1.5rem; }
    .matrix-title { color: #ffffff; font-size: 1.1rem; font-weight: 600; margin-bottom: 1.5rem; }
    .nine-box-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .box { display: flex; justify-content: center; align-items: center; height: 90px; border-radius: 6px; font-weight: 700; font-size: 1.2rem; color: #ffffff; border: 1px solid transparent; }
    
    /* Colores para la matriz (de menor a mayor impacto) */
    .box-high { background-color: rgba(0, 229, 255, 0.15); border-color: #00E5FF; color: #00E5FF; }
    .box-med { background-color: rgba(143, 155, 186, 0.1); border-color: #2D3748; }
    .box-low { background-color: rgba(255, 99, 132, 0.1); border-color: rgba(255, 99, 132, 0.3); }
    
    .axis-label { color: #8F9BBA; font-size: 0.85rem; font-weight: 600; margin-top: 10px; text-align: center;}
</style>
""", unsafe_allow_html=True)

# 2. Navegación Superior
st.markdown("""
<div class="top-navbar">
    <div class="nav-breadcrumbs">Talent Intelligence &nbsp; › &nbsp; <span>Desempeño</span></div>
    <div style="background-color: #00E5FF; color: #0b0f19; width: 35px; height: 35px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;">MJ</div>
</div>
""", unsafe_allow_html=True)

st.title("Vista de desempeño")

# 3. Pestañas de Filtros (Mockup)
st.tabs(["Por Área", "Por Gerencia", "Por División", "Por Cargo", "Por Empresa"])
st.markdown("<br>", unsafe_allow_html=True)

# 4. KPIs Superiores
st.markdown("""
<div class="kpi-container">
    <div class="kpi-box">
        <div class="kpi-value">3,8/5</div>
        <div class="kpi-label">Desempeño promedio</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value" style="color: #00C853;">24%</div>
        <div class="kpi-label">Alto desempeño</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value" style="color: #FF5252;">11%</div>
        <div class="kpi-label">En riesgo</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">+0,72</div>
        <div class="kpi-label">Correlación con skills</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Gráficos (Matriz 9-Box y Barras Simulado)
col_bars, col_matrix = st.columns([1.2, 1])

with col_bars:
    st.markdown("""
    <div class="matrix-wrapper" style="height: 100%;">
        <div class="matrix-title">Desempeño promedio por gerencia</div>
        <div style="color: #8F9BBA; font-size: 0.9rem; padding-top: 2rem;">
            <em>[Gráfico de barras interactivo generado por Plotly/Altair]</em><br><br>
            Transformación Digital: <strong>4,3</strong><br>
            Personas y Cultura: <strong>4,1</strong><br>
            Comercial: <strong>3,8</strong><br>
            Operaciones: <strong>3,2</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_matrix:
    st.markdown("""
    <div class="matrix-wrapper">
        <div class="matrix-title">Desempeño vs. potencial</div>
        <div class="nine-box-grid">
            <!-- Fila Superior (Alto Potencial) -->
            <div class="box box-med">4%</div>
            <div class="box box-med">9%</div>
            <div class="box box-high">12%</div>
            
            <!-- Fila Media (Medio Potencial) -->
            <div class="box box-low">7%</div>
            <div class="box box-med">21%</div>
            <div class="box box-high">15%</div>
            
            <!-- Fila Inferior (Bajo Potencial) -->
            <div class="box box-low">6%</div>
            <div class="box box-low">14%</div>
            <div class="box box-med">12%</div>
        </div>
        <div class="axis-label">Desempeño &rarr; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Potencial &uarr;</div>
    </div>
    """, unsafe_allow_html=True)

# 6. Panel de Insight
st.markdown("""
<div class="insight-box">
    <div class="insight-title">Patrón detectado</div>
    <div class="insight-text">Las unidades con mayor dominio de análisis de datos concentran el desempeño más alto: Transformación Digital lidera (4,3/5). Operaciones muestra la mayor brecha desempeño–potencial, foco prioritario de desarrollo.</div>
</div>
""", unsafe_allow_html=True)