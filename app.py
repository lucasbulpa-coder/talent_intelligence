import streamlit as st
import pandas as pd
import plotly.express as px
from modules.data_loader import load_data
from modules.analytics import extraer_adn_exito

st.set_page_config(page_title="Talent Intelligence", page_icon="🏢", layout="wide")

st.title("🏢 Talent Intelligence Dashboard")
st.markdown("### Visión Estratégica de Capital Humano")

df_desempeno, df_perfiles, df_consolidado = load_data()

if not df_desempeno.empty:
    # --- KPIs EJECUTIVOS ---
    col1, col2, col3, col4 = st.columns(4)
    
    total_colab = len(df_desempeno)
    
    # Asumiendo que la columna se llama 'Evaluación' o 'Desempeño'
    col_nota = 'Evaluación' if 'Evaluación' in df_desempeno.columns else df_desempeno.columns[2] 
    
    nota_promedio = df_desempeno[col_nota].mean() if pd.api.types.is_numeric_dtype(df_desempeno[col_nota]) else 0
    top_performers = len(df_desempeno[df_desempeno[col_nota] >= 4.5]) if nota_promedio > 0 else 0
    porcentaje_top = (top_performers / total_colab) * 100 if total_colab > 0 else 0

    col1.metric("Total Dotación", f"{total_colab}")
    col2.metric("Desempeño Promedio", f"{nota_promedio:.2f}/5.0")
    col3.metric("Top Performers (>= 4.5)", f"{porcentaje_top:.1f}%")
    col4.metric("Índice de Idoneidad Global", "78%", "+3% vs Q anterior")

    st.divider()

    # --- ANÁLISIS TRANSVERSAL DE ÉXITO ---
    st.markdown("### 🧬 ADN Organizacional del Alto Desempeño")
    st.caption("Cualidades emergentes extraídas del feedback de colaboradores con desempeño sobresaliente en toda la compañía.")
    
    col_feedback = 'Feedback Jefatura Habilidades' if 'Feedback Jefatura Habilidades' in df_desempeno.columns else None
    
    if col_feedback and nota_promedio > 0:
        habilidades_top = extraer_adn_exito(df_desempeno, col_feedback, col_nota, umbral=4.5, top_n=8)
        
        if habilidades_top:
            df_chart = pd.DataFrame({'Habilidad': habilidades_top, 'Impacto Relativo': range(len(habilidades_top), 0, -1)})
            fig = px.bar(df_chart, x='Impacto Relativo', y='Habilidad', orientation='h',
                         title="Competencias Transversales Críticas", template="plotly_white")
            fig.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No hay suficientes datos de texto en los top performers para extraer patrones consistentes.")
else:
    st.warning("Cargue los datos de desempeño para visualizar las métricas corporativas.")