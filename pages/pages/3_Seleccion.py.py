import streamlit as st
import pandas as pd

st.set_page_config(page_title="Selección | Talent Intelligence", layout="wide", initial_sidebar_state="collapsed")

# 1. Inyección de CSS (Estilo Dark Mode UI)
st.markdown("""
<style>
    .top-navbar { display: flex; justify-content: space-between; align-items: center; padding-bottom: 1rem; border-bottom: 1px solid #2D3748; margin-bottom: 2rem; }
    .nav-breadcrumbs { color: #8F9BBA; font-size: 1.1rem; }
    .nav-breadcrumbs span { color: #ffffff; font-weight: 600; }
    
    /* Panel de Vacantes */
    .vacancy-box { background-color: #161b26; border: 1px solid #2D3748; border-radius: 8px; padding: 1.5rem; margin-bottom: 1rem; cursor: pointer; transition: 0.3s; border-left: 4px solid transparent;}
    .vacancy-box.active { border-left-color: #00E5FF; background-color: #1a2233; }
    .vacancy-title { color: #ffffff; font-size: 1.1rem; font-weight: 600; margin-bottom: 0.3rem; }
    .vacancy-dept { color: #8F9BBA; font-size: 0.85rem; margin-bottom: 0.8rem; }
    .vacancy-count { display: inline-block; background: rgba(0, 229, 255, 0.1); color: #00E5FF; padding: 0.2rem 0.8rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; }
    
    /* Tarjetas de Candidatos (Match) */
    .candidate-row { display: flex; align-items: center; justify-content: space-between; background: #161b26; padding: 1.2rem; border-radius: 8px; margin-bottom: 0.8rem; border: 1px solid #2D3748; transition: 0.3s;}
    .candidate-row:hover { border-color: #00E5FF; }
    .candidate-info { display: flex; align-items: center; gap: 15px; }
    .candidate-avatar { background: #2D3748; color: #ffffff; width: 45px; height: 45px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: 700; letter-spacing: 1px; font-size: 0.9rem;}
    .candidate-details { display: flex; flex-direction: column; }
    .candidate-name { color: #ffffff; font-weight: 600; font-size: 1.05rem; }
    .candidate-role { color: #8F9BBA; font-size: 0.85rem; }
    .candidate-match { display: flex; align-items: baseline; gap: 5px; }
    .match-label { color: #8F9BBA; font-size: 0.85rem; }
    .match-value { color: #00E5FF; font-weight: 700; font-size: 1.3rem; }
    
    .section-title { color: #8F9BBA; font-size: 0.85rem; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 1.5rem; }
</style>
""", unsafe_allow_html=True)

# 2. Navegación Superior
st.markdown("""
<div class="top-navbar">
    <div class="nav-breadcrumbs">Talent Intelligence &nbsp; › &nbsp; <span>Selección</span></div>
    <div style="background-color: #00E5FF; color: #0b0f19; width: 35px; height: 35px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: bold;">MJ</div>
</div>
""", unsafe_allow_html=True)

st.title("Vacantes y talento potencial")

# 3. Pestañas (Mockup)
tab1, tab2, tab3 = st.tabs(["Cargos Vacantes", "Talento Potencial", "Perfiles de cargo"])

with tab1:
    # Filtros
    col_f1, col_f2, col_f3 = st.columns([1, 1, 2])
    with col_f1:
        st.selectbox("Empresa", ["Sí", "Todas las vacantes del grupo", "Banco BICE", "Factoring"])
    with col_f2:
        st.selectbox("Cargo", ["Todos", "Analista", "QA", "Asistente"])
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Layout de Vacantes y Candidatos
    col_vacantes, col_candidatos = st.columns([1, 1.2])
    
    with col_vacantes:
        st.markdown("<div class='section-title'>12 vacantes abiertas</div>", unsafe_allow_html=True)
        
        # Vacante 1 (Activa)
        st.markdown("""
        <div class="vacancy-box active">
            <div class="vacancy-title">Analista de Formación</div>
            <div class="vacancy-dept">BICECORP · Personas y Cultura · Talento y Desarrollo organizacional</div>
            <div class="vacancy-count">1 vacante</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Vacante 2
        st.markdown("""
        <div class="vacancy-box">
            <div class="vacancy-title">QA Líder</div>
            <div class="vacancy-dept">Factoring BICE · Transformación Digital</div>
            <div class="vacancy-count">2 vacantes</div>
        </div>
        """, unsafe_allow_html=True)

    with col_candidatos:
        st.markdown("<div class='section-title'>CANDIDATOS POTENCIALES</div>", unsafe_allow_html=True)
        
        # Candidato 1
        st.markdown("""
        <div class="candidate-row">
            <div class="candidate-info">
                <div class="candidate-avatar">PC</div>
                <div class="candidate-details">
                    <div class="candidate-name">Pedro Carcuro</div>
                    <div class="candidate-role">Analista Selección · Banco BICE</div>
                </div>
            </div>
            <div class="candidate-match">
                <span class="match-label">match</span>
                <span class="match-value">92%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Candidato 2
        st.markdown("""
        <div class="candidate-row">
            <div class="candidate-info">
                <div class="candidate-avatar">VC</div>
                <div class="candidate-details">
                    <div class="candidate-name">Vito Corleone</div>
                    <div class="candidate-role">Asistente Capacitación · Factoring BICE</div>
                </div>
            </div>
            <div class="candidate-match">
                <span class="match-label">match</span>
                <span class="match-value">78%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)