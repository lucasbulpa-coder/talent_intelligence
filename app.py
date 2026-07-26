import streamlit as st
from modules.data_loader import load_data

st.set_page_config(page_title="Talent Intelligence | Inicio", layout="wide", initial_sidebar_state="collapsed")

# 1. Inyección de CSS de Nivel Empresarial (Estilo Mockup)
st.markdown("""
<style>
    /* Ocultar elementos nativos de Streamlit para un look limpio */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem; max-width: 95%;}
    
    /* Barra Superior Personalizada */
    .top-navbar {
        display: flex; justify-content: space-between; align-items: center;
        padding-bottom: 1.5rem; border-bottom: 1px solid #2D3748; margin-bottom: 3rem;
    }
    .brand { font-size: 1.4rem; font-weight: 500; color: #ffffff; }
    .brand span { color: #00E5FF; font-weight: 700; margin-right: 5px; }
    .user-profile { display: flex; align-items: center; gap: 15px; }
    .user-info { text-align: right; line-height: 1.2; }
    .user-name { color: #ffffff; font-weight: 600; font-size: 0.95rem; }
    .user-role { color: #8F9BBA; font-size: 0.8rem; }
    .avatar { 
        background-color: #00E5FF; color: #0b0f19; width: 40px; height: 40px; 
        border-radius: 50%; display: flex; justify-content: center; align-items: center; 
        font-weight: 700; font-size: 1.1rem; 
    }

    /* Hero Section */
    .hero-title { font-size: 3.5rem; font-weight: 700; line-height: 1.1; margin-bottom: 1rem; color: #ffffff; }
    .hero-subtitle { font-size: 1.2rem; color: #8F9BBA; margin-bottom: 2.5rem; }
    
    /* Tarjetas de Módulos (Cards) */
    .module-card {
        background-color: #161b26; border: 1px solid #2D3748; border-radius: 12px;
        padding: 1.8rem; height: 100%; transition: all 0.3s ease;
    }
    .module-card:hover { border-color: #00E5FF; transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,229,255,0.1); }
    .card-title { color: #ffffff; font-size: 1.5rem; font-weight: 600; margin-bottom: 0.8rem; }
    .card-desc { color: #8F9BBA; font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.5; min-height: 45px;}
    .card-action { color: #00E5FF; font-weight: 600; font-size: 1rem; display: flex; align-items: center; gap: 5px;}
    
    /* Botón nativo modificado */
    div.stButton > button { background-color: #00E5FF; color: #0b0f19; font-weight: 600; border-radius: 8px; border: none; padding: 0.5rem 2rem; }
    div.stButton > button:hover { background-color: #ffffff; color: #0b0f19; }
</style>
""", unsafe_allow_html=True)

# 2. Barra Superior Simulada (Mockup UI)
st.markdown("""
<div class="top-navbar">
    <div class="brand"><span>TI</span> Talent Intelligence</div>
    <div class="user-profile">
        <div class="user-info">
            <div class="user-name">María Jiménez</div>
            <div class="user-role">RR.HH. · BICECORP</div>
        </div>
        <div class="avatar">MJ</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. Hero Section
col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown('<div class="hero-title">Gestiona el talento con datos, no con intuición</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Habilidades, movilidad interna y compensación en una plataforma para BICECORP.</div>', unsafe_allow_html=True)
    st.button("Explorar módulos")

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #8F9BBA; font-size: 0.9rem; letter-spacing: 2px;'>MÓDULOS</h4>", unsafe_allow_html=True)

# 4. Tarjetas Interactivas (Formación, Selección, Compensación)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="module-card">
        <div class="card-title">Formación</div>
        <div class="card-desc">Brechas de habilidades y planes de desarrollo por colaborador.</div>
        <div class="card-action">3 vistas &rarr;</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="module-card">
        <div class="card-title">Selección</div>
        <div class="card-desc">Cruce de vacantes con talento interno potencial.</div>
        <div class="card-action">12 vacantes &rarr;</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="module-card">
        <div class="card-title">Compensación</div>
        <div class="card-desc">Ajustes de renta sugeridos según perfil y mercado.</div>
        <div class="card-action">8 ajustes &rarr;</div>
    </div>
    """, unsafe_allow_html=True)

# Pre-carga de datos silenciosa
df_desempeno, df_perfiles, df_consolidado = load_data()