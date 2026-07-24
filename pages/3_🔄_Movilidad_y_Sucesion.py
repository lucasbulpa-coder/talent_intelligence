import streamlit as st
import pandas as pd
from modules.data_loader import load_data

st.set_page_config(page_title="Movilidad Interna", layout="wide")
st.title("🚀 Mapa de Movilidad Interna")

_, df_perfil, df_consolidado = load_data()

if not df_consolidado.empty:
    # Creamos las dos vistas usando Tabs
    tab1, tab2 = st.tabs(["👤 Proyección por Colaborador", "🎯 Búsqueda de Candidatos por Cargo"])
    
    with tab1:
        st.markdown("### ¿Hacia dónde puede crecer un colaborador?")
        colaborador = st.selectbox("Seleccione un colaborador", df_consolidado['Nombre Completo'].dropna().unique(), key="colab_select")
        
        # Aquí irá tu lógica analítica:
        # 1. Obtener el cargo actual y puntaje del colaborador.
        # 2. Comparar sus patrones de habilidades con los perfiles teóricos de cargos superiores.
        # 3. Mostrar un ranking de los 3 cargos con mayor porcentaje de compatibilidad ("Match").
        st.write(f"Calculando rutas de carrera para: **{colaborador}**...")
        st.info("Próximo paso: Integrar Scikit-Learn para medir la similitud entre las habilidades actuales y los cargos objetivo.")

    with tab2:
        st.markdown("### ¿Quiénes son los mejores candidatos para un rol?")
        cargo_objetivo = st.selectbox("Seleccione el cargo a cubrir", df_perfil['Cargo'].dropna().unique(), key="cargo_select")
        
        # Aquí irá tu lógica analítica:
        # 1. Filtrar a los "Top Performers" (el 20% con mejor nota de desempeño).
        # 2. Cruzar las habilidades requeridas del cargo seleccionado con el feedback real de los colaboradores.
        # 3. Mostrar una tabla con los colaboradores ordenados por nivel de preparación.
        st.write(f"Buscando talento interno para asumir como: **{cargo_objetivo}**...")
        st.success("Próximo paso: Generar el ranking cruzando notas de desempeño + coincidencia de habilidades clave.")

else:
    st.warning("Faltan datos para procesar la movilidad.")