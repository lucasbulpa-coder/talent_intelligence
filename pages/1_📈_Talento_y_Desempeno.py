import streamlit as st
import plotly.express as px
from modules.data_loader import load_data
from modules.analytics import get_top_performers

st.set_page_config(page_title="Talento y Desempeño", layout="wide")
st.title("📈 Dashboard de Talento y Desempeño")

_, _, df = load_data()

if not df.empty:
    col1, col2, col3 = st.columns(3)
    
    # Filtros
    area_filter = col1.selectbox("Filtrar por Área", ["Todas"] + list(df['Area'].dropna().unique()))
    
    df_filtered = df if area_filter == "Todas" else df[df['Area'] == area_filter]
    
    # KPIs Generales
    st.markdown("### Métricas Clave")
    k1, k2, k3 = st.columns(3)
    k1.metric("Total Colaboradores", len(df_filtered))
    k2.metric("Promedio Desempeño", round(df_filtered['Puntaje evaluación desempeño'].mean(), 1))
    
    top_df = get_top_performers(df_filtered)
    k3.metric("Top Performers (20%)", len(top_df))
    
    # Gráficos
    st.markdown("---")
    st.markdown("### Distribución de Desempeño")
    fig = px.histogram(df_filtered, x='Puntaje evaluación desempeño', nbins=10, 
                       color_discrete_sequence=['#2E86C1'], template='plotly_white')
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla Top Performers
    st.markdown("### Listado Top Performers")
    st.dataframe(top_df[['Nombre Completo', 'Nombre Cargo', 'Area', 'Puntaje evaluación desempeño']])
else:
    st.warning("No hay datos cargados. Verifica los archivos Excel.")