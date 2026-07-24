import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
from modules.data_loader import load_data

st.set_page_config(page_title="Brechas y Formación", layout="wide")
st.title("🎓 Plan de Desarrollo Individual (PDI) Automatizado")
st.markdown("Identificación de brechas de competencia y orquestación directa con el Centro de Aprendizaje (LMS).")

# 1. Carga y Estandarización de Datos
df_desempeno, df_perfiles, df_consolidado = load_data()

if not df_desempeno.empty and not df_perfiles.empty:
    col_nombre = 'Nombre Completo'
    col_cargo = 'Nombre Cargo'
    col_nota = 'Puntaje evaluación desempeño'
    col_feedback = 'Comentario abierto de habilidades tecnica que detecta la jefarura'
    
    if df_desempeno[col_nota].dtype == object:
        df_desempeno[col_nota] = df_desempeno[col_nota].astype(str).str.replace(',', '.')
    df_desempeno[col_nota] = pd.to_numeric(df_desempeno[col_nota], errors='coerce').fillna(0)
    
    # 2. Selector de Colaborador
    colab = st.selectbox("👤 Seleccione un colaborador para trazar su PDI:", df_desempeno[col_nombre].dropna().unique())
    
    # Extraer datos del colaborador
    datos_colab = df_desempeno[df_desempeno[col_nombre] == colab].iloc[0]
    cargo_colab = datos_colab[col_cargo]
    nota_actual = datos_colab[col_nota]
    
    st.divider()
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown(f"### Análisis de Brechas: {cargo_colab}")
        
        if cargo_colab in df_perfiles['Cargo'].values:
            perfil_teorico = df_perfiles[df_perfiles['Cargo'] == cargo_colab].iloc[0]
            
            st.info(f"**Requisitos Técnicos del Cargo:**\n{perfil_teorico.get('Conocimientos Técnicos', 'No definidos')}")
            st.warning(f"**Feedback Técnico de Jefatura (Realidad):**\n{datos_colab.get(col_feedback, 'Sin comentarios')}")
            
            # Simulación de Brecha Cuantitativa (Ideal vs Real) para el Gráfico
            # En producción, esto se calcularía con NLP comparando el feedback vs requisitos
            fig = go.Figure()
            categorias = ['Conocimiento Técnico', 'Autonomía', 'Resolución de Problemas', 'Trabajo en Equipo', 'Liderazgo']
            
            fig.add_trace(go.Scatterpolar(
                r=[5, 5, 5, 5, 5],
                theta=categorias,
                fill='toself',
                name='Nivel Esperado (Perfil)',
                line_color='rgba(0, 71, 171, 0.5)'
            ))
            
            # Puntuación simulada basada en el desempeño global (escalado de 90-115 a 1-5)
            nivel_real = max(1, min(5, (nota_actual - 90) / 5))
            fig.add_trace(go.Scatterpolar(
                r=[nivel_real, nivel_real*0.9, nivel_real*1.1, 4, 3], 
                theta=categorias,
                fill='toself',
                name='Nivel Actual (Evaluación)',
                line_color='rgba(255, 127, 80, 0.8)'
            ))
            
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True, margin=dict(t=20, b=20))
            st.plotly_chart(fig, use_container_width=True)
            
        else:
            st.error("No se encontró el perfil teórico asociado a este cargo.")

    with col2:
        st.markdown("### 🛠️ Configuración del Plan de Acción")
        
        # Integración de Metodología de Cambio (ADKAR)
        st.markdown("**Evaluación de Disposición (ADKAR)**")
        awareness = st.checkbox("¿El colaborador está consciente de su brecha? (Awareness)", value=True)
        desire = st.checkbox("¿Muestra disposición para capacitarse? (Desire)", value=False)
        
        st.markdown("**Módulos Digitales a Asignar**")
        cursos = st.multiselect(
            "Seleccione las rutas de aprendizaje:",
            ["Inducción Corporativa Nivel 2", "Reforzamiento Técnico Específico", "Habilidades Ágiles", "Liderazgo y Feedback"]
        )
        
        if not (awareness and desire):
            st.warning("⚠️ Sin 'Awareness' y 'Desire', la capacitación tiene alto riesgo de fracaso. Se sugiere una sesión de alineación de expectativas antes de matricular.")
        
        st.divider()
        
        # Generación de Payload para el LMS
        if st.button("🚀 Generar Matrícula LMS", type="primary"):
            if cursos:
                payload_lms = {
                    "accion": "matricula_automatica",
                    "colaborador": {
                        "nombre": colab,
                        "cargo": cargo_colab,
                        "id_empleado": str(datos_colab.get('ID Colaborador', '0000'))
                    },
                    "modulos_asignados": cursos,
                    "estado_adkar_previo": {
                        "awareness": awareness,
                        "desire": desire
                    },
                    "metodo_notificacion": "power_automate_email"
                }
                
                json_lms = json.dumps(payload_lms, indent=4, ensure_ascii=False).encode('utf-8')
                st.success("Plan estructurado correctamente.")
                st.download_button(
                    label="📥 Descargar Archivo de Integración (JSON)",
                    data=json_lms,
                    file_name=f"lms_enroll_{colab.replace(' ', '_')}.json",
                    mime="application/json"
                )
            else:
                st.error("Debe seleccionar al menos un módulo de capacitación.")

else:
    st.error("Faltan datos de desempeño o perfiles para ejecutar el motor de formación.")