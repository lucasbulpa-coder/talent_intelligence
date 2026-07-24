import streamlit as st
import pandas as pd
import re
import plotly.express as px
from collections import Counter
from modules.data_loader import load_data

st.set_page_config(page_title="Perfiles Inteligentes", layout="wide")
st.title("🎯 Comparativa: Perfil Teórico vs Real")

def extraer_patrones(lista_textos):
    if not lista_textos: return []
    texto_completo = " ".join(str(t) for t in lista_textos).lower()
    palabras = re.findall(r'\b[a-záéíóúñ]+\b', texto_completo)
    stopwords = {"que", "de", "la", "el", "en", "y", "a", "los", "las", "se", "con", "por", "para", "un", "una", "su", "es", "del", "lo", "como", "más", "tiene", "muy"}
    palabras_clave = [p for p in palabras if p not in stopwords and len(p) > 3]
    return Counter(palabras_clave).most_common(5)

_, _, df_consolidado = load_data()

if not df_consolidado.empty:
    cargo_seleccionado = st.selectbox("Seleccione un Cargo para analizar", df_consolidado['Nombre Cargo'].dropna().unique())
    df_cargo = df_consolidado[df_consolidado['Nombre Cargo'] == cargo_seleccionado]
    
    if not df_cargo.empty:
        # Extraer patrones
        textos_hab = df_cargo['Feedback Jefatura Habilidades'].dropna().tolist() if 'Feedback Jefatura Habilidades' in df_cargo.columns else []
        patrones = extraer_patrones(textos_hab)
        
        # Construir datos para el radar (simulando puntajes para el MVP)
        if patrones:
            conceptos = [p[0].capitalize() for p in patrones]
            frecuencias = [p[1] for p in patrones]
            nivel_esperado = [max(frecuencias) + 1] * len(conceptos) # El ideal siempre es un poco superior al máximo observado
            
            df_radar = pd.DataFrame({
                'Competencia': conceptos * 2,
                'Puntaje': frecuencias + nivel_esperado,
                'Tipo': ['Real Observado'] * len(conceptos) + ['Teórico Requerido'] * len(conceptos)
            })
            
            fig = px.line_polar(df_radar, r='Puntaje', theta='Competencia', color='Tipo', line_close=True,
                                template="plotly_white", title=f"Análisis de Brechas: {cargo_seleccionado}")
            fig.update_traces(fill='toself', opacity=0.5)
            
            st.plotly_chart(fig, use_container_width=True)
            
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📘 Perfil Teórico (Diseño)")
            st.info(f"**🧠 Conocimientos Técnicos:**\n\n{df_cargo['Conocimientos Técnicos'].iloc[0] if 'Conocimientos Técnicos' in df_cargo.columns else 'N/A'}")
            
        with col2:
            st.markdown("### 📊 Patrones de Feedback (Real)")
            if patrones:
                for palabra, frecuencia in patrones:
                    st.progress(min(frecuencia * 10, 100), text=f"{palabra.capitalize()} (Mencionado {frecuencia} veces)")
else:
    st.warning("Datos no disponibles.")