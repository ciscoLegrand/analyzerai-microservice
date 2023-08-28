import os
import requests
import app.utils.logger as logger

class APIService:
    environment = os.getenv('FLASK_ENV', 'development').upper()
    BASE_URL = os.getenv(f'{environment}_URL', 'DEVELOPMENT_URL')
    TOKEN = os.environ.get(f"{environment}_TOKEN")
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    @classmethod
    def get_answers(cls, enterprise_id, start_date, end_date, items=100000):
        url = f"{cls.BASE_URL}/api/v2/enterprises/{enterprise_id}/answers?start_date={start_date}&end_date={end_date}&items={items}"
        logger.log_debug(f"🔵 Llamando a la API con la URL: {url}")
        
        response = requests.get(url, headers=cls.HEADERS)
        if response.status_code == 200:
            logger.log_debug(f"✅ successfull response")
            return response.json()
        else:
            logger.log_warning(f"👮 Error response {response.status_code}")
            return None
