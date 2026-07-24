import streamlit as st
import pandas as pd
import plotly.express as px
from modules.data_loader import load_data

st.set_page_config(page_title="Estrategia Organizacional", layout="wide")
st.title("📊 Estrategia Organizacional y KPIs")

df_desempeno, _, _ = load_data()

if not df_desempeno.empty:
    # 1. Configuración de columnas
    col_nota = 'Puntaje evaluación desempeño'
    col_gerencia = 'Gerencia' if 'Gerencia' in df_desempeno.columns else 'Area'
    
    # Limpieza de datos numéricos
    if df_desempeno[col_nota].dtype == object:
        df_desempeno[col_nota] = df_desempeno[col_nota].astype(str).str.replace(',', '.')
    df_desempeno[col_nota] = pd.to_numeric(df_desempeno[col_nota], errors='coerce')
    df_desempeno = df_desempeno.dropna(subset=[col_nota])
    
    # 2. KPIs Ejecutivos
    st.markdown("### 📈 Indicadores Clave de Rendimiento")
    kpi1, kpi2, kpi3 = st.columns(3)
    
    promedio_global = df_desempeno[col_nota].mean()
    umbral_top = df_desempeno[col_nota].quantile(0.80)
    top_performers_count = len(df_desempeno[df_desempeno[col_nota] >= umbral_top])
    
    with kpi1:
        st.metric(label="Total Evaluados", value=len(df_desempeno))
    with kpi2:
        st.metric(label="Promedio Organizacional", value=f"{promedio_global:.1f}")
    with kpi3:
        st.metric(label="Talentos Clave (Top 20%)", value=top_performers_count)
        
    st.divider()

    # 3. Análisis por Gerencia/Área
    st.markdown("### 🏢 Desempeño Promedio por Gerencia")
    st.caption("Visión estructural para la toma de decisiones estratégicas.")
    
    if col_gerencia in df_desempeno.columns:
        # Agrupar datos por gerencia
        df_agrupado = df_desempeno.groupby(col_gerencia)[col_nota].mean().reset_index()
        df_agrupado = df_agrupado.sort_values(by=col_nota, ascending=True)
        
        # Gráfico de barras horizontal interactivo
        fig = px.bar(df_agrupado, 
                     x=col_nota, 
                     y=col_gerencia, 
                     orientation='h',
                     text_auto='.1f',
                     labels={col_nota: "Puntaje Promedio", col_gerencia: "Gerencia / Área"},
                     template="plotly_white")
        
        fig.update_traces(marker_color='#2E86C1')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No se encontró una columna de 'Gerencia' o 'Area' para realizar la segmentación.")

else:
    st.warning("No hay datos de desempeño cargados para generar la vista estratégica.")