import logging
import os

# Configura el registro
log_directory = os.path.join(os.getcwd(), "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(log_directory, "app.log")),
                        logging.StreamHandler()  # también imprimir en la consola
                    ])

logger = logging.getLogger()

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


