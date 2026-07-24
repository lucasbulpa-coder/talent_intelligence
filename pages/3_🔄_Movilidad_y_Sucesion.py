import streamlit as st
import pandas as pd
import json
from modules.data_loader import load_data

st.set_page_config(page_title="Movilidad y Sucesión", layout="wide")
st.title("🔄 Matriz Automática de Movilidad y Sucesión")
st.markdown("""
Esta herramienta simula escenarios de rotación. Al liberar una posición estratégica, el motor de inteligencia 
identifica automáticamente a los sucesores internos más preparados, reduciendo los tiempos de vacancia.
""")

# 1. Carga de Datos
df_desempeno, df_perfiles, df_consolidado = load_data()

if not df_desempeno.empty:
    # 2. Pipeline de Limpieza Estricta (Blindaje contra errores de Excel)
    col_nota = 'Puntaje evaluación desempeño'
    col_nombre = 'Nombre Completo'
    col_cargo = 'Nombre Cargo'
    col_area = 'Area' if 'Area' in df_desempeno.columns else 'Gerencia'
    
    # Estandarización de la columna de desempeño a numérica
    if df_desempeno[col_nota].dtype == object:
        df_desempeno[col_nota] = df_desempeno[col_nota].astype(str).str.replace(',', '.')
    df_desempeno[col_nota] = pd.to_numeric(df_desempeno[col_nota], errors='coerce').fillna(0)
    
    st.divider()

    # 3. Interfaz de Simulación de Vacancia
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🏢 Escenario de Rotación")
        cargo_vacante = st.selectbox(
            "Seleccione el cargo que quedará vacante:", 
            df_desempeno[col_cargo].dropna().unique()
        )
        
        # Determinar el área del cargo vacante (para dar prioridad a candidatos de la misma área)
        area_vacante = df_desempeno[df_desempeno[col_cargo] == cargo_vacante][col_area].iloc[0] if col_area in df_desempeno.columns else "General"
        
        st.info(f"**Área de la vacante:** {area_vacante}")

    # 4. Motor Algorítmico de Sucesión
    # Filtramos a los candidatos: excluimos a los que ya tienen ese cargo exacto
    candidatos = df_desempeno[df_desempeno[col_cargo] != cargo_vacante].copy()
    
    if not candidatos.empty:
        # Calcular el "Fit Score" (Puntaje de Idoneidad)
        # Regla de negocio: El desempeño base pesa un 100%, pero si son de la misma área tienen un bonus del 5%
        candidatos['bonus_area'] = candidatos[col_area].apply(lambda x: 1.05 if x == area_vacante else 1.0)
        candidatos['fit_score'] = candidatos[col_nota] * candidatos['bonus_area']
        
        # Ordenar a los mejores 3 perfiles
        sucesores = candidatos.sort_values(by='fit_score', ascending=False).head(3)
        
        with col2:
            st.markdown(f"### 🥇 Sucesores Recomendados")
            
            # Formatear la tabla visual
            tabla_mostrar = sucesores[[col_nombre, col_cargo, col_area, col_nota]].copy()
            tabla_mostrar.columns = ['Candidato', 'Cargo Actual', 'Área Actual', 'Desempeño Histórico']
            
            st.dataframe(tabla_mostrar, use_container_width=True, hide_index=True)
            
            # 5. Integración Corporativa (Payload para flujos automatizados)
            st.markdown("#### ⚡ Integración Operativa")
            st.caption("Exporte los resultados para iniciar procesos de inducción y actualización de perfiles en el sistema.")
            
            # Preparamos los datos estructurados
            payload_data = {
                "evento_rotacion": {
                    "cargo_liberado": cargo_vacante,
                    "area_afectada": area_vacante
                },
                "asignacion_automatica": sucesores[[col_nombre, col_cargo, 'fit_score']].to_dict(orient='records')
            }
            
            json_payload = json.dumps(payload_data, indent=4, ensure_ascii=False).encode('utf-8')
            
            st.download_button(
                label="⚙️ Descargar Payload JSON para Power Automate",
                data=json_payload,
                file_name=f"trigger_sucesion_{cargo_vacante.replace(' ', '_')}.json",
                mime="application/json",
                type="primary"
            )
    else:
        st.warning("No hay suficientes datos de otros colaboradores para calcular la sucesión.")

else:
    st.error("No se han cargado los datos de desempeño. Verifique la ingesta de archivos.")