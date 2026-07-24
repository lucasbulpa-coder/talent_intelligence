import pandas as pd
import streamlit as st
import os
import logging

# Configuración de logs para trazabilidad
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Rutas relativas a los archivos (Asegura que la carpeta 'data' exista)
PATH_DESEMPENO = "data/Desempeño.xlsx"
PATH_PERFILES = "data/perfil de cargo.xlsx"

@st.cache_data(ttl="2h", show_spinner=False)
def load_data():
    """
    Motor central de ingesta y validación de datos.
    Utiliza caché para no saturar la memoria del servidor en cada recarga de página.
    Retorna: df_desempeno, df_perfiles, df_consolidado
    """
    df_desempeno = pd.DataFrame()
    df_perfiles = pd.DataFrame()
    df_consolidado = pd.DataFrame()

    # --- 1. INGESTA Y VALIDACIÓN DE DESEMPEÑO ---
    if os.path.exists(PATH_DESEMPENO):
        try:
            df_desempeno = pd.read_excel(PATH_DESEMPENO)
            
            # Validación de "Data Contract" (Columnas mínimas requeridas)
            columnas_criticas = ['Nombre Completo', 'Nombre Cargo', 'Puntaje evaluación desempeño']
            faltantes = [col for col in columnas_criticas if col not in df_desempeno.columns]
            
            if faltantes:
                st.error(f"🚨 Archivo Desempeño inválido. Faltan las columnas: {', '.join(faltantes)}")
                return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

            # Limpieza Centralizada: Arreglo del problema str vs float para toda la app
            col_nota = 'Puntaje evaluación desempeño'
            if df_desempeno[col_nota].dtype == object:
                df_desempeno[col_nota] = df_desempeno[col_nota].astype(str).str.replace(',', '.')
            
            df_desempeno[col_nota] = pd.to_numeric(df_desempeno[col_nota], errors='coerce').fillna(0)
            
            # Limpieza de textos (Evita errores de scikit-learn con valores nulos)
            col_feedback = 'Comentario abierto de habilidades tecnica que detecta la jefarura'
            if col_feedback in df_desempeno.columns:
                df_desempeno[col_feedback] = df_desempeno[col_feedback].astype(str).fillna("Sin comentarios")
                
            logging.info("Datos de desempeño cargados y limpiados exitosamente.")
            
        except Exception as e:
            st.error(f"Falla crítica al leer {PATH_DESEMPENO}: {str(e)}")
            logging.error(f"Error en ingesta de desempeño: {str(e)}")
    else:
        st.warning(f"No se encontró la base de datos de talento en: {PATH_DESEMPENO}")

    # --- 2. INGESTA Y VALIDACIÓN DE PERFILES DE CARGO ---
    if os.path.exists(PATH_PERFILES):
        try:
            df_perfiles = pd.read_excel(PATH_PERFILES)
            
            if 'Cargo' not in df_perfiles.columns:
                st.error("🚨 Archivo de Perfiles inválido. Falta la columna 'Cargo'.")
            else:
                logging.info("Datos de perfiles de cargo cargados exitosamente.")
                
        except Exception as e:
            st.error(f"Falla crítica al leer {PATH_PERFILES}: {str(e)}")
            logging.error(f"Error en ingesta de perfiles: {str(e)}")
    else:
        st.warning(f"No se encontró el diccionario de cargos en: {PATH_PERFILES}")

    # --- 3. CONSOLIDACIÓN ESTRUCTURAL ---
    # Si ambos archivos existen, creamos una vista consolidada para el motor de Inteligencia
    if not df_desempeno.empty and not df_perfiles.empty:
        try:
            # Hacemos un cruce (Left Join) para tener a la persona y su perfil teórico en una sola tabla
            df_consolidado = pd.merge(
                df_desempeno, 
                df_perfiles, 
                left_on='Nombre Cargo', 
                right_on='Cargo', 
                how='left'
            )
            logging.info("Cruce de datos (Talento + Perfiles) realizado con éxito.")
        except Exception as e:
            st.error(f"Error al consolidar las bases de datos: {str(e)}")

    return df_desempeno, df_perfiles, df_consolidado