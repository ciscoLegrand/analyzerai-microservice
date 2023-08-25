from flask import jsonify
from app.utils.logger import log_warning, log_error

def handle_400_error(error):
    log_warning("🟡 [Bad Request] Solicitud con sintaxis inválida detectada.")
    return jsonify(error="Bad Request: La solicitud no pudo ser entendida debido a una sintaxis inválida."), 400

def handle_405_error(error):
    log_warning("🟡 [Method Not Allowed] Método de solicitud no permitido.")
    return jsonify(error="Method Not Allowed: El método de solicitud no está permitido para el recurso solicitado."), 405

def handle_408_error(error):
    log_warning("🟡 [Request Timeout] Tiempo de espera de la solicitud agotado.")
    return jsonify(error="Request Timeout: El servidor no recibió una solicitud completa en el tiempo esperado."), 408

def handle_401_error(error):
    log_warning("🔴 [Unauthorized] Intento de acceso no autorizado detectado.")
    return jsonify(error="Unauthorized: Acceso no autorizado. Por favor, verifica tus credenciales."), 401

def handle_403_error(error):
    log_warning("🔴 [Forbidden] Intento de acceso a un recurso prohibido detectado.")
    return jsonify(error="Forbidden: No tienes permiso para acceder a este recurso."), 403

def handle_404_error(error):
    log_warning("🟠 [Not Found] Se solicitó un recurso no encontrado.")
    return jsonify(error="Not Found: El recurso solicitado no existe."), 404

def handle_500_error(error):
    log_error("🔥 [Internal Server Error] Se produjo un error interno del servidor.")
    return jsonify(error="Internal Server Error: Se produjo un error mientras se procesaba tu solicitud. Nuestro equipo ha sido notificado."), 500

