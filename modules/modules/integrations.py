import requests
import logging
import json

class WorkflowOrchestrator:
    """
    Módulo de integración directa con plataformas empresariales (ej. Power Automate).
    """
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.headers = {'Content-Type': 'application/json'}

    def disparar_transicion_cargo(self, saliente, entrante, cargo):
        """
        Notifica automáticamente que Pedrito sale y Juan entra, 
        gatillando procesos de TI y Recursos Humanos en segundos.
        """
        payload = {
            "evento": "sucesion_automatica",
            "colaborador_saliente": saliente,
            "colaborador_entrante": entrante,
            "cargo_asignado": cargo,
            "accion_requerida": "actualizar_sistemas_e_iniciar_induccion"
        }
        
        try:
            # Se envía el paquete de datos en milisegundos sin intervención humana
            response = requests.post(
                self.webhook_url, 
                data=json.dumps(payload), 
                headers=self.headers
            )
            response.raise_for_status()
            logging.info(f"Éxito: Flujo de sucesión disparado para {entrante}")
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Falla de integración al orquestador: {e}")
            return False