import pandas as pd

def get_top_performers(df, column_score='Puntaje evaluación desempeño', top_percent=0.20):
    """Filtra el dataframe para obtener el Top 20% de la organización."""
    if df.empty or column_score not in df.columns:
        return df
    
    umbral = df[column_score].quantile(1 - top_percent)
    top_df = df[df[column_score] >= umbral].copy()
    return top_df

def calculate_match(persona_skills, cargo_skills):
    """Calcula el % de coincidencia entre texto observado y perfil (MVP: coincidencias exactas/parciales)."""
    if pd.isna(persona_skills) or pd.isna(cargo_skills):
        return 0
    
    persona_words = set(str(persona_skills).lower().replace(',', ' ').split())
    cargo_words = set(str(cargo_skills).lower().replace(',', ' ').split())
    
    if not cargo_words:
        return 0
        
    coincidencias = persona_words.intersection(cargo_words)
    match_score = (len(coincidencias) / len(cargo_words)) * 100
    
    return round(min(match_score, 100.0), 1)
# --- AGREGA ESTO AL FINAL DE TU ARCHIVO modules/analytics.py ---

def extract_keywords(text_series):
    """Extrae las palabras más frecuentes de una columna de texto (MVP sin IA avanzada)."""
    text = " ".join(text_series.dropna().astype(str)).lower()
    # Filtramos conectores básicos (Stopwords manuales)
    stopwords = {"para", "como", "pero", "este", "esta", "todo", "tiene", "sobre", "entre", "cuando", "desde"}
    
    # Limpiamos puntuación y separamos palabras
    words = text.replace(",", " ").replace(".", " ").split()
    # Nos quedamos con palabras relevantes (más de 4 letras y que no sean stopwords)
    relevant_words = [w for w in words if len(w) > 4 and w not in stopwords]
    
    # Contamos frecuencias
    return pd.Series(relevant_words).value_counts()

def calculate_gaps(df_top, df_resto, text_column):
    """Calcula la brecha (Gap) de competencias entre el Top 20% y el Resto."""
    if df_top.empty or df_resto.empty:
        return pd.DataFrame()

    top_kw = extract_keywords(df_top[text_column])
    resto_kw = extract_keywords(df_resto[text_column])

    # Convertir a porcentajes relativos (frecuencia / cantidad de personas)
    top_pct = (top_kw / len(df_top) * 100).round(1)
    resto_pct = (resto_kw / len(df_resto) * 100).round(1)

    # Unir ambos resultados
    df_brechas = pd.DataFrame({
        'Presencia Top Performers (%)': top_pct,
        'Presencia Resto (%)': resto_pct
    }).fillna(0)

    # Calcular la brecha matemática
    df_brechas['Brecha (%)'] = df_brechas['Presencia Top Performers (%)'] - df_brechas['Presencia Resto (%)']
    
    # Ordenar por las competencias que más diferencian al Top 20%
    df_brechas = df_brechas.sort_values(by='Brecha (%)', ascending=False)
    
    return df_brechas.head(10) # Devolver el Top 10 de brechas