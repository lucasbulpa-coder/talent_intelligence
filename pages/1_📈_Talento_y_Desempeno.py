import streamlit as st
import pandas as pd
import plotly.express as px
from modules.data_loader import load_data

st.set_page_config(page_title="Talento y Desempeño", layout="wide")
st.title("📈 Análisis de Talento y Desempeño")

df_desempeno, _, _ = load_data()

if not df_desempeno.empty:
    # 1. Usar el nombre exacto de TU columna de Excel
    col_nota = 'Puntaje evaluación desempeño'
    
    # Validación por si el Excel viene con comas en lugar de puntos (esto evita el TypeError)
    if df_desempeno[col_nota].dtype == object:
        df_desempeno[col_nota] = df_desempeno[col_nota].astype(str).str.replace(',', '.')
    
    # Forzar numérico
    df_desempeno[col_nota] = pd.to_numeric(df_desempeno[col_nota], errors='coerce')
    df_desempeno = df_desempeno.dropna(subset=[col_nota])
    
    st.markdown("### 📊 Distribución del Desempeño Organizacional")
    st.caption("Visualización de la curva de rendimiento de la compañía basada en cumplimiento.")
    
    # Histograma usando tus datos (de 90 a 115 aprox)
    fig = px.histogram(df_desempeno, x=col_nota, nbins=15, 
                       labels={col_nota: "Puntaje de Evaluación"},
                       template="plotly_white")
    
    fig.update_traces(marker_color='#0047AB') 
    fig.update_layout(yaxis_title="Cantidad de Colaboradores")
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.markdown("### 🏆 Segmentación de Top Performers")
    st.caption("Identificación de talento clave según el umbral de sobrecumplimiento.")
    
    # 2. Control dinámico para la gerencia
    umbral_defecto = float(df_desempeno[col_nota].quantile(0.80)) # Por defecto, el top 20%
    umbral = st.slider("Defina el puntaje mínimo para considerar a un Top Performer:", 
                       min_value=float(df_desempeno[col_nota].min()), 
                       max_value=float(df_desempeno[col_nota].max()), 
                       value=umbral_defecto)
    
    # Filtro usando la variable del slider
    df_top = df_desempeno[df_desempeno[col_nota] >= umbral].sort_values(by=col_nota, ascending=False)
    
    if not df_top.empty:
        # Mostrar las columnas que tienes realmente en tu Excel
        cols_mostrar = ['Nombre Completo', 'Nombre Cargo', 'Area', col_nota]
        
        # Filtramos por las que existan para no romper el código si falta alguna
        cols_existentes = [col for col in cols_mostrar if col in df_top.columns]
        
        st.write(f"**Total de talentos identificados:** {len(df_top)} colaboradores.")
        st.dataframe(df_top[cols_existentes], use_container_width=True, hide_index=True)
        
        csv = df_top.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Exportar Lista de Talentos (CSV)",
            data=csv,
            file_name='top_performers_organizacional.csv',
            mime='text/csv',
        )
    else:
        st.info("No hay colaboradores que superen este umbral de evaluación.")
        
else:
    st.warning("No hay datos de desempeño cargados. Verifique el archivo fuente.")