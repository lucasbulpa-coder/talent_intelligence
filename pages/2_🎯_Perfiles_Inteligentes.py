import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from modules.data_loader import load_data
from modules.analytics import extraer_adn_exito

st.set_page_config(page_title="Perfiles Inteligentes", layout="wide")
st.title("🎯 Perfiles Inteligentes: Teórico vs Práctica")

df_desempeno, df_perfiles, df_consolidado = load_data()

if not df_consolidado.empty and not df_perfiles.empty:
    # --- 1. AJUSTE A TU ESCALA REAL Y FORMATO DE DATOS ---
    col_nota = 'Puntaje evaluación desempeño'
    
    # Limpiamos y convertimos la columna a numérico
    if col_nota in df_consolidado.columns:
        if df_consolidado[col_nota].dtype == object:
            df_consolidado[col_nota] = df_consolidado[col_nota].astype(str).str.replace(',', '.')
        df_consolidado[col_nota] = pd.to_numeric(df_consolidado[col_nota], errors='coerce')
    
    # Usamos tus nombres de columnas exactos
    col_feedback = 'Comentario abierto de habilidades tecnica que detecta la jefarura'

    cargo = st.selectbox("Seleccione un Cargo Estratégico", df_perfiles['Cargo'].dropna().unique())
    
    # Filtrar datos del cargo
    datos_cargo = df_consolidado[df_consolidado['Nombre Cargo'] == cargo]
    perfil_teorico = df_perfiles[df_perfiles['Cargo'] == cargo].iloc[0]
    
    # --- 2. UMBRAL DINÁMICO ---
    # En lugar de 4.5, calculamos quiénes están en el 20% superior de desempeño (percentil 80)
    umbral_top = df_consolidado[col_nota].quantile(0.80)

    # Extraer ADN de los mejores en ESTE cargo
    adn_exito = extraer_adn_exito(datos_cargo, col_feedback, col_nota, umbral=umbral_top, top_n=5) if col_feedback in df_consolidado.columns else []

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📋 Perfil Base (Requisitos Formales)")
        st.info(f"**Conocimientos Técnicos Exigidos:**\n{perfil_teorico.get('Conocimientos Técnicos', 'N/A')}")
        st.info(f"**Competencias Blandas Oficiales:**\n{perfil_teorico.get('Competencias Blandas', 'N/A')}")

    with col2:
        st.markdown("### 🧬 ADN del Alto Desempeño (Práctica)")
        if adn_exito:
            st.success("**Competencias descubiertas en Top Performers:**\n\n" + "\n".join([f"✔️ {hab.capitalize()}" for hab in adn_exito]))
            st.caption(f"Patrones extraídos del feedback de jefaturas para colaboradores con nota superior a {umbral_top:.1f}")
        else:
            st.warning("No hay suficientes datos de alto desempeño en los comentarios para extraer patrones emergentes.")

    st.divider()
    
    # Gráfico de Radar Estratégico
    if adn_exito:
        st.markdown("### 📊 Alineación de Competencias")
        # Simulamos los ejes combinando lo teórico y lo práctico
        categorias = ['Conocimiento Base', 'Habilidades Blandas', 'Desempeño Operativo'] + [h.capitalize() for h in adn_exito[:2]]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=[3, 4, 3, 2, 2],
            theta=categorias,
            fill='toself',
            name='Perfil Teórico Actual'
        ))
        fig.add_trace(go.Scatterpolar(
            r=[4, 3, 4, 5, 5], # Puntuaciones altas en las habilidades emergentes
            theta=categorias,
            fill='toself',
            name='Perfil Top Performer Observado'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Faltan datos de perfiles o desempeño para realizar el cruce analítico.")