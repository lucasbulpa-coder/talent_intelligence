import streamlit as st
import pandas as pd
from modules.data_loader import load_data
from modules.analytics import get_top_performers, calculate_gaps

st.set_page_config(page_title="Brechas y Formación", layout="wide")
st.title("🎓 Brechas de Desarrollo y Formación")

_, _, df = load_data()

if not df.empty:
    st.markdown("""
    Aquí identificamos qué habilidades marcan la diferencia. 
    **Regla:** Comparamos las características del **Top 20% de desempeño** contra el resto del equipo.
    """)
    
    # Filtro para ver por Cargo o por Área
    tipo_filtro = st.radio("Analizar brechas a nivel de:", ["Por Cargo", "Por Área"], horizontal=True)
    
    if tipo_filtro == "Por Cargo":
        seleccion = st.selectbox("Seleccionar Cargo", df['Nombre Cargo'].dropna().unique())
        df_filtrado = df[df['Nombre Cargo'] == seleccion]
    else:
        seleccion = st.selectbox("Seleccionar Área", df['Area'].dropna().unique())
        df_filtrado = df[df['Area'] == seleccion]
        
    st.markdown("---")
    
    # Separar Top 20% del Resto
    top_df = get_top_performers(df_filtrado)
    # El resto son aquellos que no están en el top_df
    resto_df = df_filtrado.drop(top_df.index)
    
    if len(top_df) > 0 and len(resto_df) > 0:
        # Analizamos la columna de cualidades (puedes cambiarla según tu Excel)
        columna_analisis = 'Feedback Jefatura Cualidades' 
        if columna_analisis in df.columns:
            brechas = calculate_gaps(top_df, resto_df, columna_analisis)
            
            if not brechas.empty:
                st.markdown(f"### 🔍 Competencias Diferenciadoras para: {seleccion}")
                st.dataframe(brechas, use_container_width=True)
                
                # Módulo 4: Generación de plan sugerido basado en la mayor brecha
                st.markdown("### 📋 Plan de Formación Sugerido")
                competencia_prioritaria = brechas.index[0].title()
                
                st.info(f"""
                **Prioridad 1:** Capacitación en **{competencia_prioritaria}**
                
                *Justificación de la plataforma:* Esta competencia aparece un **{brechas.iloc[0]['Brecha (%)']}%** más en los Top Performers que en el resto de los colaboradores de este segmento. Desarrollarla en el 80% restante tendría el mayor impacto estadístico en el desempeño general.
                """)
            else:
                st.warning("No hay suficientes comentarios de texto para extraer conclusiones de brechas.")
        else:
            st.error(f"La columna '{columna_analisis}' no existe en el Excel.")
    else:
        st.warning("No hay suficientes colaboradores en este segmento para comparar un Top 20% con un Resto.")
else:
    st.warning("Datos no disponibles.")