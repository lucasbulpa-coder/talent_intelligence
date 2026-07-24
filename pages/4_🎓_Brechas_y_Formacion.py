import streamlit as st
import pandas as pd
import plotly.express as px
from modules.data_loader import load_data

st.set_page_config(page_title="Brechas y Formación", layout="wide")
st.title("📚 Detección de Brechas Formativas")

desempeno, _, _ = load_data()

if not desempeno.empty:
    st.markdown("### 📉 Áreas Críticas de Capacitación")
    
    # Simulamos el conteo de brechas agrupando por área para el MVP
    if 'Area' in desempeno.columns:
        brechas_area = desempeno.groupby('Area').size().reset_index(name='Necesidades Detectadas')
        
        # Gráfico de barras de Plotly
        fig = px.bar(brechas_area, x='Area', y='Necesidades Detectadas', 
                     title="Volumen de Brechas por Área", text_auto=True, template="plotly_white")
        fig.update_traces(marker_color='#0047AB') # Color corporativo
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 📋 Detalle Operativo para Malla de Entrenamiento")
        st.dataframe(brechas_area, use_container_width=True, hide_index=True)
        
        # BOTÓN DE DESCARGA
        csv_brechas = brechas_area.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Exportar Reporte de Brechas (CSV)",
            data=csv_brechas,
            file_name='reporte_brechas_areas.csv',
            mime='text/csv',
        )
    else:
        st.info("La columna 'Area' no está disponible en los datos para graficar.")
else:
    st.warning("No hay datos suficientes para el análisis de brechas.")