import streamlit as st
import pandas as pd
from modules.data_loader import load_data

st.set_page_config(page_title="Movilidad y Sucesión", layout="wide")
st.title("🚀 Mapa de Movilidad Interna")

_, df_perfil, df_consolidado = load_data()

if not df_consolidado.empty:
    st.markdown("### 🔎 Búsqueda de Sucesores")
    cargo_objetivo = st.selectbox("Seleccione el cargo a cubrir", df_perfil['Cargo'].dropna().unique())
    
    # Simulación de un motor de búsqueda interno para el MVP
    st.write(f"Evaluando talento interno para: **{cargo_objetivo}**...")
    
    # Creamos un DataFrame falso de candidatos para el MVP visual
    datos_candidatos = {
        "Colaborador": ["Juan Pérez", "María González", "Carlos Soto"],
        "Cargo Actual": ["Analista Jr", "Especialista", "Asistente"],
        "Match Competencias (%)": [88, 75, 60],
        "Desempeño Histórico": [4.8, 4.2, 3.9]
    }
    df_sucesores = pd.DataFrame(datos_candidatos)
    
    # Visualización de la tabla
    st.dataframe(df_sucesores, use_container_width=True, hide_index=True)
    
    # BOTÓN DE DESCARGA PARA GERENCIA
    csv = df_sucesores.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Exportar Lista de Sucesores (CSV)",
        data=csv,
        file_name=f'sucesores_{cargo_objetivo.replace(" ", "_")}.csv',
        mime='text/csv',
    )
    
    st.divider()
    st.markdown("### 📈 Planes de Desarrollo Individual")
    
    # FLUJO ORIENTADO A LA ACCIÓN
    for index, row in df_sucesores.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{row['Colaborador']}** - Match: {row['Match Competencias (%)']}%")
        with col2:
            # Botón único por cada candidato usando su índice
            if st.button(f"Ver Plan de Nivelación", key=f"btn_{index}"):
                with st.expander(f"Plan Formativo Estructurado: {row['Colaborador']}", expanded=True):
                    st.write("**1. Awareness (Conciencia):** Alinear al colaborador con la necesidad de cubrir el rol de", cargo_objetivo)
                    st.write("**2. Desire (Deseo):** Sesión de mentoring para motivar la transición al nuevo cargo.")
                    st.write("**3. Knowledge (Conocimiento):** Asignación de módulos teóricos sobre las funciones principales.")
                    st.write("**4. Ability (Habilidad):** 2 semanas de 'Shadowing' (sombra) con el titular actual del puesto.")
                    st.write("**5. Reinforcement (Refuerzo):** Evaluación a los 30 días y ajustes al plan.")
                    st.success("Plan enviado al sistema de gestión de capacitación.")

else:
    st.warning("Faltan datos para procesar la movilidad.")