# modules/integrations.py
import requests
import json
from datetime import datetime

def trigger_administrative_workflow(employee_email, action_type, payload, webhook_url):
    """
    Envía un payload estructurado a un webhook externo (ej. Power Automate) 
    para orquestar flujos administrativos y notificaciones de cumplimiento.
    """
    headers = {'Content-Type': 'application/json'}
    
    data = {
        "timestamp": datetime.now().isoformat(),
        "employee_email": employee_email,
        "action_type": action_type,  # Ej: 'NUEVO_PLAN_FORMACION', 'CANDIDATO_SUCESION'
        "details": payload
    }
    
    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        return True, "Flujo automatizado detonado con éxito."
    except requests.exceptions.RequestException as e:
        return False, f"Error al conectar con el orquestador: {str(e)}"