import os
from flask import render_template
import app.utils.logger as logger
from app.services.answers.builder import process_answers
from app.services.api.api_service import APIService
from app.services.answers.filtering_comments import filter_custom_fields
from app.services.answers.analyzer import AnswerAnalyzer

def index(enterprise_id, start_date, end_date):
    logger.log_info("📡 Obteniendo respuestas de la API...")
    api_data = APIService.get_answers(enterprise_id, start_date, end_date)
    if api_data:
        total_responses = api_data["total"]
        logger.log_info("🔢 Total de respuestas: {}".format(total_responses)) 
        
        custom_answers_list = filter_custom_fields(api_data["answers"])
        custom_answers = {
            "total": len(custom_answers_list),
            "answers": custom_answers_list
        }
        logger.log_info("🔢 Total de respuestas con custom_field: {}".format(custom_answers["total"]))
        answers = process_answers(custom_answers)
    else:
        total_responses = 0
        custom_answers = {"total": 0, "answers": []}
        answers = []
    
    return render_template("answers/index.html", total=total_responses, total_custom=custom_answers["total"], answers=answers)


