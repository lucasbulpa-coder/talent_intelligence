import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def limpiar_texto(texto):
    if not isinstance(texto, str): return ""
    texto = texto.lower()
    texto = re.sub(r'[^a-záéíóúñ\s]', '', texto)
    return texto

def extraer_adn_exito(df, columna_texto, columna_desempeno, umbral=4.5, top_n=5):
    """
    Extrae las competencias clave aislando solo a los top performers.
    """
    if df.empty or columna_texto not in df.columns or columna_desempeno not in df.columns:
        return []

    # Filtrar solo a los de alto desempeño
    df_top = df[df[columna_desempeno] >= umbral].copy()
    if df_top.empty: return []

    textos = df_top[columna_texto].apply(limpiar_texto).tolist()
    textos = [t for t in textos if t.strip() != ""]
    
    if not textos: return []

    # Stopwords en español ampliadas
    stopwords_es = ["que", "de", "la", "el", "en", "y", "a", "los", "las", "se", "con", "por", "para", "un", "una", "su", "es", "del", "lo", "como", "más", "tiene", "muy", "pero", "este", "ha", "su", "sus", "sobre"]

    try:
        vectorizer = TfidfVectorizer(stop_words=stopwords_es, max_features=20, ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform(textos)
        
        # Sumar los scores TF-IDF para encontrar los términos más relevantes
        scores = tfidf_matrix.sum(axis=0).A1
        palabras = vectorizer.get_feature_names_out()
        
        # Crear un dataframe con los resultados y ordenar
        df_scores = pd.DataFrame({'Competencia': palabras, 'Score': scores})
        df_scores = df_scores.sort_values(by='Score', ascending=False).head(top_n)
        
        return df_scores['Competencia'].tolist()
    except Exception as e:
        return []