# modules/succession_engine.py

def analyze_skill_gaps(current_skills, required_skills):
    """Calcula las brechas entre las habilidades actuales y las requeridas para un cargo."""
    gaps = {}
    for skill, req_level in required_skills.items():
        curr_level = current_skills.get(skill, 0)
        if curr_level < req_level:
            gaps[skill] = req_level - curr_level
    return gaps

def generate_adkar_plan(employee_name, target_role, missing_skills):
    """
    Genera un plan de desarrollo estructurado en la metodología ADKAR 
    para cerrar brechas de competencias.
    """
    if not missing_skills:
        return {"status": "ready", "message": f"{employee_name} está listo para el rol de {target_role}."}

    skills_str = ", ".join(missing_skills.keys())
    
    adkar_plan = {
        "colaborador": employee_name,
        "rol_objetivo": target_role,
        "fases": {
            "1_Awareness": f"Comunicar a {employee_name} la necesidad del negocio de fortalecer {skills_str} para asumir {target_role}.",
            "2_Desire": "Alinear los objetivos personales del colaborador con los incentivos de movilidad interna y compensación del nuevo rol.",
            "3_Knowledge": f"Asignar módulos técnicos específicos sobre {skills_str} a través del centro de aprendizaje digital.",
            "4_Ability": f"Asignar un proyecto práctico supervisado donde {employee_name} aplique {skills_str} en un entorno controlado.",
            "5_Reinforcement": "Establecer revisiones quincenales 360° y validación de adopción de las nuevas competencias."
        }
    }
    
    return adkar_plan