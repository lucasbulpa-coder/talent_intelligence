import streamlit as st
col1, col2, col3 = st.columns(3)
col1.metric("Total Colaboradores", "1,250", "+15 este mes")
col2.metric("Top Performers", "20%", "Estable")
col3.metric("Brecha de Competencias Promedio", "12%", "-2% vs Q anterior")

st.set_page_config(
    page_title="Talent Intelligence Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("🏠 Inicio - Talent Intelligence Platform")
    
    st.markdown("""
    ### Proyecto RH Digital
    Plataforma interna para el análisis estratégico del talento, movilidad interna y planificación de capacidades.
    
    **Módulos Activos (Fase 1 - MVP):**
    * 📈 **Talento y Desempeño:** Distribución y Top Performers.
    * 🎯 **Perfiles Inteligentes:** Comparativa Perfil Teórico vs Real.
    * 🔄 **Movilidad y Sucesión:** Algoritmo de compatibilidad Persona-Cargo.
    
    > ⚠️ **Restricción de Uso:** Esta herramienta provee evidencia y patrones. Las decisiones finales siempre deben ser tomadas por Líderes o el equipo de Desarrollo Organizacional.
    """)

if __name__ == "__main__":
    main()