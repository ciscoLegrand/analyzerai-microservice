import os
import requests
import json
from flask import jsonify
import app.utils.logger as logger
def index():
    # Simulamos una respuesta de la API
    api_response = {
        "total": 10252,
        "answers": [
            {
                "_id": "641a19b56d425400025f230e",
                # ... más campos ...
            },
            # ... más respuestas ...
        ]
    }

    total_responses = api_response["total"]
    answers = api_response["answers"]

    return render_template("answers/index.html", total_responses=total_responses, answers=answers)

def get_answers():

    id_empresa = os.environ.get("ENTERPRISE_ID")
    BASE_URL = os.environ.get("BASE_URL")
    TOKEN = os.environ.get("TOKEN")
    url = f"{BASE_URL}/api/v2/enterprises/{enterprise_id}/answers?start_date=01-01-2023&end_date=21-03-2023"
    logger.log_debug(f"🔵 Llamando a la API con la URL: {url}")
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=HEADERS)
    try:
        if response.status_code == 200:
            logger.log_info(f"✅ Respuesta de la API recibida con un total de {response.json()['total']} respuestas")
            # return jsonify(response.json())
            return response
        else:
            logger.log_warning(f"👮 Error {response.status_code} al llamar a la API")
            # return jsonify(response.json()), response.status_code
            return response
    except Exception as e:
        logger.log_error(f"❌ Error {e} al llamar a la API")
        return jsonify({"error": str(e)}), 500
    
