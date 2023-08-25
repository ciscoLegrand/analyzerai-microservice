import os
import requests
import traceback # Para hacer debugging
import pdb # Para hacer debugging
from app.models import Answer
from app.utils.analysis.stop_words import stop_words_loader
from app.utils.analysis.word_analyzer import analyze_single_enterprise
import app.utils.logger as logger

BASE_URL = os.environ.get("STAGING_URL")
TOKEN = os.environ.get("TOKEN")
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

def fetch_answers_from_api(enterprise_id):
    url = f"{BASE_URL}/api/v2/enterprises/{enterprise_id}/answers"
    start_date = "01-01-2023"
    end_date = "31-03-2023"
    body = {
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.get(url, headers=HEADERS, json=body)
    
    if response.status_code != 200:
        logger.log_error(f"🔴 Error fetching answers for enterprise {enterprise_id}: {response.text}")
        raise Exception(f"Error fetching answers for enterprise {enterprise_id}: {response.text}")

    response_data = response.json()
    total = response_data.get('total', 'N/A')
    
    logger.log_info(f"✅ Successfully fetched answers for enterprise {enterprise_id}. Total: {total}")
    
    # Crear una instancia Answer para cada respuesta y añadirla a la lista.
    answer_objects = [Answer(data=answer) for answer in response_data.get('answers', [])]
    
    if answer_objects:  # Verificar si hay respuestas antes de acceder al primer elemento
        logger.log_info(f"✅ Successfully fetched answers for enterprise {enterprise_id}. Total: {total}, First answer: {answer_objects[0].__dict__}")
    
    return answer_objects


def analyze_most_repeated_words(enterprise_id):
    logger.log_info(f"🔎 Analyzing most repeated words for enterprise {enterprise_id}...")
    try:
        answers = fetch_answers_from_api(enterprise_id)
        # Llamando a analyze_and_process_answers con enterprise_id
        results = []
        results = analyze_single_enterprise(answers, enterprise_id, 2023, 1)
        # get lenght of results
        logger.log_info(f"✅ Results: {len(results)}")
        logger.log_info(f"✅ Most common words for enterprise {enterprise_id}: {results}")

        return results

    except Exception as e:
        error_message = f"🔴 Failed to analyze answers for enterprise {enterprise_id}. Reason: {str(e)}.\n"
        error_message += "Traceback:\n" + traceback.format_exc()
        logger.log_error(error_message)
        raise e
