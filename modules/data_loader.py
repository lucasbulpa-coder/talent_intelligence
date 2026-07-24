import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    """Lee y cruza los archivos Excel de desempeño y perfiles, limpiando errores de tipeo."""
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    desempeno_path = os.path.join(project_root, "data", "Desempeño.xlsx")
    perfil_path = os.path.join(project_root, "data", "perfil de cargo.xlsx")
    
    try:
        df_desempeno = pd.read_excel(desempeno_path)
        df_perfil = pd.read_excel(perfil_path)
        
        # --- NUEVO: RENOMBRAR COLUMNAS CON ERRORES DEL EXCEL ---
        # Así evitamos que los errores de tipeo rompan el resto de tus dashboards
        df_desempeno = df_desempeno.rename(columns={
            'Comentario abierto de habilidades tecnica que detecta la jefarura': 'Feedback Jefatura Habilidades',
            'Cualiadidades que detecta la jefatura': 'Feedback Jefatura Cualidades',
            'Cualidades que detectan sus pares': 'Feedback Pares Cualidades',
            'Habilidades que detectan sus pares': 'Feedback Pares Habilidades'
        })
        
        # Estandarizar columnas de cruce
        if 'Código Cargo' in df_perfil.columns:
            df_perfil = df_perfil.rename(columns={"Código Cargo": "Id Cargo"})
            
        # Limpieza de IDs
        df_desempeno['Id Cargo'] = df_desempeno['Id Cargo'].astype(str).str.strip().str.upper()
        df_perfil['Id Cargo'] = df_perfil['Id Cargo'].astype(str).str.strip().str.upper()
        
        # Consolidado cruzando por Cargo
        df_consolidado = pd.merge(df_desempeno, df_perfil, on="Id Cargo", how="left")
        
        # Manejo de nulos en puntajes
        if 'Puntaje evaluación desempeño' in df_consolidado.columns:
            df_consolidado['Puntaje evaluación desempeño'] = pd.to_numeric(
                df_consolidado['Puntaje evaluación desempeño'], errors='coerce'
            ).fillna(0)
            
        return df_desempeno, df_perfil, df_consolidado
        
    except Exception as e:
        st.error(f"Error cargando datos. Detalle técnico: {e}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()