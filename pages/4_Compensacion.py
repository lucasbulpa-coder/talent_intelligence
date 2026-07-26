import streamlit as st

st.set_page_config(page_title="Compensación | Talent Intelligence", layout="wide", initial_sidebar_state="collapsed")

# 1. Inyección de CSS (Estilo Dark Mode UI y Tabla Personalizada)
st.markdown("""
<style>
    .top-navbar { display: flex; justify-content: space-between; align-items: center; padding-bottom: 1rem; border-bottom: 1px solid #2D3748; margin-bottom: 2rem; }
    .nav-breadcrumbs { color: #8F9BBA; font-size: 1.1rem; }
    .nav-breadcrumbs span { color: #ffffff; font-weight: 600; }
    
    /* Tarjetas KPI */
    .kpi-container { display: flex; gap: 1rem; margin-bottom: 2rem; }
    .kpi-box { flex: 1; background-color: #161b26; border: 1px solid #2D3748; border-radius: 8px; padding: 1.5rem; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; }
    .kpi-value { color: #00E5FF; font-size: 2.2rem; font-weight: 700; line-height: 1.2; margin-bottom: 0.2rem; }
    .kpi-label { color: #ffffff; font-size: 1rem; font-weight: 600; }
    
    /* Tabla Corporativa Personalizada */
    .custom-table-wrapper { background-color: #161b26; border: 1px solid #2D3748; border-radius: 8px; padding: 1rem; overflow-x: auto; }
    .custom-table { width: 100%; border-collapse: collapse; text-align: left; }
    .custom-table th { color: #8F9BBA; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; padding: 1rem; border-bottom: 1px solid #2D3748; }
    .custom-table td { color: #ffffff; font-size: 0.95rem; padding: 1rem; border-bottom: 1px solid #1a2233; }
    .custom-table tr:hover { background-color: #1a2233; }
    .custom-table tr:last-child td { border-bottom: none; }
    
    /* Elementos específicos de la tabla */
    .cell-company { color: #8F9BBA; }
    .cell-increase { color: #00C853; font-weight: 600; display: flex; align-items: center; gap: 5px; } /* Verde para alzas */
</style>
""", unsafe_allow_html=True)

# 2. Navegación Superior
st.markdown("""
<div class="top-navbar">
    <div class="nav-breadcrumbs">Talent Intelligence &nbsp; › &nbsp; <span>Compensación</span></div>
    <div style="background-color: #00E5FF; color: #0b0f19; width: 35px; height: 35px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;">MJ</div>
</div>
""", unsafe_allow_html=True)

st.title("Ajustes de renta sugeridos")

# 3. Filtros superiores (Mockup)
col_f1, col_f2, col_f3 = st.columns([1, 1, 3])
with col_f1:
    st.selectbox("Posiciones", ["Vacantes", "Ocupadas", "Todas"])
with col_f2:
    st.selectbox("Perfiles de cargo", ["Todos", "Analistas", "Líderes"])

st.markdown("<br>", unsafe_allow_html=True)

# 4. Panel de KPIs
st.markdown("""
<div class="kpi-container">
    <div class="kpi-box">
        <div class="kpi-value">8</div>
        <div class="kpi-label">Ajustes propuestos</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">+9,4%</div>
        <div class="kpi-label">Alza promedio</div>
    </div>
    <div class="kpi-box">
        <div class="kpi-value">$14,2M</div>
        <div class="kpi-label">Impacto anual</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Tabla de Datos Financieros Personalizada
# Recreamos la tabla exacta de la presentación usando HTML para un control visual total
st.markdown("""
<div class="custom-table-wrapper">
    <table class="custom-table">
        <thead>
            <tr>
                <th>Cargo</th>
                <th>Empresa</th>
                <th>Renta actual</th>
                <th>Renta sugerida</th>
                <th>Ajuste</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Analista de Datos</strong></td>
                <td class="cell-company">Banco BICE</td>
                <td>$1.850.000</td>
                <td>$2.050.000</td>
                <td><span class="cell-increase">▲ +10,8%</span></td>
            </tr>
            <tr>
                <td><strong>Analista Formación</strong></td>
                <td class="cell-company">BICECORP</td>
                <td>$1.620.000</td>
                <td>$1.760.000</td>
                <td><span class="cell-increase">▲ +8,6%</span></td>
            </tr>
            <tr>
                <td><strong>QA Líder</strong></td>
                <td class="cell-company">Factoring</td>
                <td>$2.100.000</td>
                <td>$2.310.000</td>
                <td><span class="cell-increase">▲ +10,0%</span></td>
            </tr>
            <tr>
                <td><strong>Asistente Capacit.</strong></td>
                <td class="cell-company">Factoring</td>
                <td>$1.180.000</td>
                <td>$1.240.000</td>
                <td><span class="cell-increase">▲ +5,1%</span></td>
            </tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)