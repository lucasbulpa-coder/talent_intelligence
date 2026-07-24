import pandas as pd
import logging

# Configuración de logs para trazabilidad corporativa
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TalentDataPipeline:
    """
    Motor de ingesta de datos. Aísla la interfaz gráfica de los errores del Excel.
    """
    def __init__(self, excel_desempeno, excel_perfiles):
        self.path_desempeno = excel_desempeno
        self.path_perfiles = excel_perfiles
        
        # Diccionario de mapeo: Traduce los nombres inestables del Excel a variables internas fijas.
        # Si RRHH cambia el nombre de la columna mañana, solo actualizamos este diccionario, no toda la app.
        self.schema_desempeno = {
            'ID Colaborador': 'id_colaborador',
            'Nombre Completo': 'nombre_completo',
            'Nombre Cargo': 'cargo',
            'Area': 'area',
            'Puntaje evaluación desempeño': 'desempeno_global',
            'Comentario abierto de habilidades tecnica que detecta la jefarura': 'feedback_tecnico'
        }

    def procesar_desempeno(self):
        try:
            df = pd.read_excel(self.path_desempeno)
            
            # 1. Estandarización de columnas (Ignora las que no nos importan)
            columnas_presentes = {k: v for k, v in self.schema_desempeno.items() if k in df.columns}
            df = df.rename(columns=columnas_presentes)
            
            # 2. Limpieza estricta de métricas (Adiós al error de str vs float)
            if 'desempeno_global' in df.columns:
                if df['desempeno_global'].dtype == object:
                    df['desempeno_global'] = df['desempeno_global'].astype(str).str.replace(',', '.')
                df['desempeno_global'] = pd.to_numeric(df['desempeno_global'], errors='coerce')
                
                # Manejo de nulos: llenar con el promedio o 0 según la regla de negocio
                df['desempeno_global'] = df['desempeno_global'].fillna(0)
            
            # 3. Preparación para datos continuos (ej. feedback 360)
            # Aseguramos que los campos de texto siempre sean string para que scikit-learn no falle
            if 'feedback_tecnico' in df.columns:
                df['feedback_tecnico'] = df['feedback_tecnico'].astype(str).fillna("Sin comentarios")
                
            logging.info(f"Pipeline ejecutado con éxito. {len(df)} registros procesados.")
            return df
            
        except Exception as e:
            logging.error(f"Falla crítica en la ingesta de datos de desempeño: {str(e)}")
            return pd.DataFrame() # Retorna un DataFrame vacío controlado, la app no se cae.