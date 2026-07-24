import streamlit as st
from modules.data_loader import load_data
from modules.analytics import get_top_performers, extract_keywords

st.set_page_config(page_title="Estrategia Organizacional", layout="wide")
st.title("📊 Estrategia Organizacional")

_, _, df = load_data()

if not df.empty:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧬 ADN de Talento (Toda la Empresa)")
        st.write("Características que más se repiten en el Top 20% de toda la organización.")
        
        top_global = get_top_performers(df)
        if 'Cualidades detectadas por jefatura' in top_global.columns:
            adn_kw = extract_keywords(top_global['Cualidades detectadas por jefatura'])
            if not adn_kw.empty:
                # Mostramos los 5 conceptos más fuertes
                for palabra, frecuencia in adn_kw.head(5).items():
                    st.success(f"**{palabra.title()}** (Mencionada {frecuencia} veces en Top Performers)")
                    
    with col2:
        st.markdown("### 🚀 Competencias Emergentes")
        st.write("Términos muy repetidos en las evaluaciones, pero que no están escritos formalmente en los perfiles de cargo.")
        
        if 'Cualidades detectadas por jefatura' in df.columns and 'Competencias Blandas' in df.columns:
            kw_observadas = set(extract_keywords(df['Cualidades detectadas por jefatura']).head(20).index)
            
            # Texto consolidado de todos los perfiles de cargo
            texto_perfiles = " ".join(df['Competencias Blandas'].dropna().astype(str)).lower()
            
            competencias_emergentes = []
            for kw in kw_observadas:
                if kw not in texto_perfiles:
                    competencias_emergentes.append(kw)
                    
            if competencias_emergentes:
                for comp in competencias_emergentes[:5]:
                    st.warning(f"💡 **{comp.title()}**")
                st.caption("Considerar actualizar los perfiles de cargo con estas habilidades.")
            else:
                st.info("El perfil teórico y el práctico están altamente alineados.")
else:
    st.warning("Datos no disponibles.")