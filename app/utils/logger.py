import logging
import os
from logging.handlers import RotatingFileHandler

log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'logs')

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger = logging.getLogger(__name__)

def initialize_logger():
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Configurar StreamHandler (consola)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    # Configurar RotatingFileHandler (archivo)
    environment = os.getenv("ENVIRONMENT", "development")

    fh = RotatingFileHandler(os.path.join(log_directory, f"{environment}.log"), maxBytes=10*1024*1024, backupCount=5)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

def log_info(message):
    detailed_message = f"🔵 [INFO] {message}"
    logger.info(detailed_message)

def log_error(message):
    detailed_message = f"🔴 [ERROR] {message}"
    logger.error(detailed_message)

def log_warning(message):
    detailed_message = f"🟠 [WARNING] {message}"
    logger.warning(detailed_message)

def log_debug(message):
    detailed_message = f"🟣 [DEBUG] {message}"
    logger.debug(detailed_message)

# Inicializa el logger al importar el módulo
initialize_logger()
