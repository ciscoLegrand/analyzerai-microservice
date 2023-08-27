import os
from app import create_app
import logging

# Configura el registro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

ENVIRONMENT = os.getenv('FLASK_ENV', 'default')
BASE_URL = os.getenv('BASE_URL', '')

# Registrar las variables de entorno
logger.info(f"🌐 Cargando entorno: {ENVIRONMENT}")
logger.info(f"🌐 Cargando URL base: {BASE_URL}")
# Si quieres ver todas las variables de entorno, puedes hacer un bucle:
for key, value in os.environ.items():
    logger.info(f"🔧 {key} = {value}")

app = create_app(ENVIRONMENT)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
