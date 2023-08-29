import os
import requests
import traceback
import app.utils.logger as logger

class APIService:
    environment = os.getenv('FLASK_ENV', 'development').upper()
    BASE_URL = os.getenv(f'{environment}_URL', 'DEVELOPMENT_URL')
    TOKEN = os.environ.get(f"{environment}_TOKEN", 'DEVELOPMENT_TOKEN')
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
            tb_str = traceback.format_exc()
            logger.log_warning(f"👮[APIService get_answers] Error response {response.status_code}\n{tb_str}")
            return None

    @classmethod
    def get_enterprises(cls):
        url = f"{cls.BASE_URL}/api/v2/enterprises/active"
        logger.log_debug(f"🔵[get_enterprises(cls)] Llamando a la API con la URL: {url}")
        
        response = requests.get(url, headers=cls.HEADERS)
        if response.status_code == 200:
            logger.log_debug(f"✅ successfull response")
            return response.json()
        else:
            tb_str = traceback.format_exc()
            logger.log_warning(f"👮 [APIService get_enterprises] Error response {response.status_code}\n{tb_str}")
            return None

    @classmethod
    def post_word_frequency(cls, enterprise_id, word_frequency):
        url = f"{cls.BASE_URL}/api/v2/enterprises/{enterprise_id}/word_frequencies"
        logger.log_debug(f"🔵 Llamando a la API con la URL: {url}")

        response = requests.post(url, json={"word_frequency": word_frequency}, headers=cls.HEADERS)
        
        if response.status_code == 200:
            logger.log_debug(f"✅ Successful response for word: {word_frequency['word']}")
            return {"status": "success", "data": response.json()}
        else:
            tb_str = traceback.format_exc()
            logger.log_warning(f"👮 [APIService post_word_frequency] Error response {response.status_code} for word: {word_frequency['word']}\n{tb_str}")
            return {"status": "failed", "data": response.json()}
