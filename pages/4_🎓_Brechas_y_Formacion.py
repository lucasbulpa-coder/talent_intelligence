import streamlit as st
import pandas as pd
from modules.data_loader import load_data

st.set_page_config(page_title="Brechas y Formación", layout="wide")
st.title("🎓 Análisis de Brechas y Plan de Formación (PDI)")

df_desempeno, df_perfiles, df_consolidado = load_data()

if not df_desempeno.empty and not df_perfiles.empty:
    
    # 1. Definir los nombres exactos de TUS columnas
    col_nombre = 'Nombre Completo'
    col_cargo = 'Nombre Cargo'
    col_nota = 'Puntaje evaluación desempeño'
    
    # Selector de colaborador corregido
    colab = st.selectbox("Seleccione un colaborador para análisis de brechas", df_desempeno[col_nombre].dropna().unique())
    
    # Filtrar los datos del colaborador seleccionado
    datos_colab = df_desempeno[df_desempeno[col_nombre] == colab].iloc[0]
    cargo_colab = datos_colab[col_cargo]
    
    st.markdown(f"### 👤 Colaborador: {colab}")
    st.caption(f"Cargo Actual: {cargo_colab} | Evaluación: {datos_colab[col_nota]}")
    
    st.divider()
    
    # Buscar el perfil teórico de ese cargo
    if cargo_colab in df_perfiles['Cargo'].values:
        perfil_teorico = df_perfiles[df_perfiles['Cargo'] == cargo_colab].iloc[0]
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Conocimientos Exigidos por el Perfil:**\n{perfil_teorico.get('Conocimientos Técnicos', 'No definidos')}")
        with col2:
            st.warning(f"**Feedback Técnico de Jefatura:**\n{datos_colab.get('Comentario abierto de habilidades tecnica que detecta la jefarura', 'Sin comentarios')}")
            
    else:
        st.warning("No se encontró el perfil de cargo teórico para realizar la comparación de brechas.")

else:
    st.error("Faltan datos de desempeño o perfiles para ejecutar esta página.")