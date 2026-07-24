import streamlit as st
import pandas as pd
import re
from collections import Counter
from modules.data_loader import load_data

st.set_page_config(page_title="Perfiles Inteligentes", layout="wide")
st.title("🎯 Comparativa: Perfil Teórico vs Patrones Reales")

def extraer_patrones(lista_textos):
    """Extrae y cuenta las palabras/conceptos clave más repetidos en los comentarios."""
    if not lista_textos: return []
    
    # Unir todo el texto y pasar a minúsculas
    texto_completo = " ".join(str(t) for t in lista_textos).lower()
    
    # Extraer solo palabras (sin signos de puntuación)
    palabras = re.findall(r'\b[a-záéíóúñ]+\b', texto_completo)
    
    # Palabras comunes que no aportan valor al patrón (Stopwords)
    stopwords = {"que", "de", "la", "el", "en", "y", "a", "los", "las", "se", "con", 
                 "por", "para", "un", "una", "su", "es", "del", "lo", "como", "más", "tiene", "muy"}
    
    # Filtrar palabras clave de más de 3 letras
    palabras_clave = [p for p in palabras if p not in stopwords and len(p) > 3]
    
    # Contar las frecuencias
    return Counter(palabras_clave).most_common(5) # Devuelve los 5 patrones principales

_, _, df_consolidado = load_data()

if not df_consolidado.empty:
    cargo_seleccionado = st.selectbox("Seleccione un Cargo para analizar", df_consolidado['Nombre Cargo'].dropna().unique())
    df_cargo = df_consolidado[df_consolidado['Nombre Cargo'] == cargo_seleccionado]
    
    if not df_cargo.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📘 Perfil Teórico (Diseño)")
            conocimientos = df_cargo['Conocimientos Técnicos'].iloc[0] if 'Conocimientos Técnicos' in df_cargo.columns else "No definido"
            competencias = df_cargo['Competencias Blandas'].iloc[0] if 'Competencias Blandas' in df_cargo.columns else "No definido"
            
            st.info(f"**🧠 Conocimientos Técnicos:**\n\n{conocimientos}")
            st.info(f"**🤝 Competencias Blandas:**\n\n{competencias}")
            
        with col2:
            st.markdown("### 📊 Patrones de Feedback (Real)")
            st.write("Tendencias principales detectadas en las evaluaciones de este cargo:")
            
            # Análisis de Habilidades (Jefatura)
            if 'Feedback Jefatura Habilidades' in df_cargo.columns:
                textos = df_cargo['Feedback Jefatura Habilidades'].dropna().tolist()
                patrones = extraer_patrones(textos)
                if patrones:
                    st.success("**Conceptos técnicos más repetidos:**")
                    for palabra, frecuencia in patrones:
                        st.progress(min(frecuencia * 10, 100), text=f"{palabra.capitalize()} (Mencionado {frecuencia} veces)")
            
            # Análisis de Cualidades (Pares)
            if 'Feedback Pares Cualidades' in df_cargo.columns:
                textos_pares = df_cargo['Feedback Pares Cualidades'].dropna().tolist()
                patrones_pares = extraer_patrones(textos_pares)
                if patrones_pares:
                    st.info("**Cualidades blandas más destacadas por pares:**")
                    for palabra, frecuencia in patrones_pares:
                        st.progress(min(frecuencia * 10, 100), text=f"{palabra.capitalize()} (Mencionado {frecuencia} veces)")
else:
    st.warning("Datos no disponibles.")