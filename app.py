import streamlit as st
import pandas as pd
from modules.data_loader import load_data

# 1. Configuración Global de la Aplicación (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="Talent Intelligence Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Precarga Silenciosa de Datos en Caché
# Llamamos al DataLoader aquí para que los datos suban a la memoria RAM 
# apenas el usuario abre la app, haciendo que la navegación entre páginas sea instantánea.
df_desempeno, df_perfiles, df_consolidado = load_data()

# 3. Interfaz del Centro de Mando
st.title("🧠 Talent Intelligence Platform")
st.subheader("Sistema de Diagnóstico Organizacional, Sucesión y Desarrollo Estratégico")

st.markdown("---")

# 4. Resumen Ejecutivo para Stakeholders
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Bienvenido al centro de mando de Talento Organizacional. 
    
    Esta plataforma transforma los datos aislados de desempeño y estructuras teóricas de cargo en inteligencia procesable, permitiendo a las gerencias tomar decisiones ágiles sobre movilidad interna y planes de capacitación.
    
    ### ⚙️ Arquitectura y Capacidades del Sistema:
    
    *   📊 **Dashboard Directivo:** Indicadores clave de rendimiento, distribución de talento y evaluación del desempeño global por áreas operativas.
    *   🧬 **ADN del Éxito:** Algoritmos de detección de patrones en los *Top Performers* para identificar las competencias que realmente impulsan el negocio.
    *   🔄 **Sucesión Dinámica:** Motor analítico que simula escenarios de vacancia e identifica automáticamente a los candidatos internos más idóneos basándose en proximidad estructural y desempeño histórico.
    *   🎓 **Gestión del Desarrollo (PDI):** Orquestación de rutas de aprendizaje estructuradas. Evalúa la disposición al cambio mediante la **metodología ADKAR** antes de realizar asignaciones.
    """)

with col2:
    st.info("### 📡 Ecosistema Conectado")
    st.markdown("""
    El sistema está diseñado para generar *Payloads* (archivos JSON estructurados) listos para integrarse con:
    
    *   **Orquestadores de Flujo:** Activación de notificaciones y alertas automáticas.
    *   **Learning Management System (LMS):** Enrolamiento directo en módulos digitales de inducción y reforzamiento técnico.
    """)

st.markdown("---")

# 5. Panel de Estado de los Datos (Data Health)
st.markdown("### 🗄️ Estado de la Ingesta de Datos")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    if not df_desempeno.empty:
        st.success(f"✅ Evaluación de Desempeño: {len(df_desempeno)} registros cargados.")
    else:
        st.error("🚨 Evaluación de Desempeño: Faltan datos o archivo corrupto.")

with metric2:
    if not df_perfiles.empty:
        st.success(f"✅ Perfiles de Cargo: {len(df_perfiles)} perfiles teóricos mapeados.")
    else:
        st.error("🚨 Perfiles de Cargo: Faltan datos o archivo corrupto.")

with metric3:
    if not df_consolidado.empty:
        st.info(f"🔗 Motor de Cruce Operativo: {len(df_consolidado)} perfiles validados.")
    else:
        st.warning("⚠️ Motor de Cruce: Pendiente de validación conjunta.")

# 6. Instrucciones de Navegación
st.markdown("<br>", unsafe_allow_html=True)
st.caption("👈 Utilice el menú lateral para navegar por los módulos operativos específicos.")