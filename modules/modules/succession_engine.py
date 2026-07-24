import pandas as pd

class SuccessionEngine:
    """
    Algoritmo de movilidad interna y planes de sucesión.
    """
    def __init__(self, df_talento, df_perfiles):
        self.talento = df_talento
        self.perfiles = df_perfiles

    def calcular_reemplazo_automatico(self, cargo_vacante, top_n=3):
        """
        Si un colaborador sale de la organización, identifica automáticamente
        a los sucesores internos basándose en desempeño y proximidad de cargo.
        """
        if self.talento.empty:
            return None
            
        # 1. Excluir a los que ya tienen el cargo
        candidatos = self.talento[self.talento['cargo'] != cargo_vacante].copy()
        
        # 2. Algoritmo de "Fit Score" (Simulación de idoneidad)
        # En una fase avanzada, aquí inyectamos NLP para cruzar el 'feedback_tecnico' con el perfil.
        # Por ahora, usamos el desempeño global histórico como base ponderada.
        candidatos['fit_score'] = candidatos['desempeno_global'] * 1.15 
        
        # 3. Penalización o bonificación por Área (es más fácil mover a alguien de la misma área)
        # Asumimos que conocemos el área del cargo vacante consultando los perfiles (omito esa búsqueda por brevedad)
        
        sucesores = candidatos.sort_values(by='fit_score', ascending=False).head(top_n)
        
        return sucesores[['nombre_completo', 'cargo', 'area', 'fit_score', 'desempeno_global']]