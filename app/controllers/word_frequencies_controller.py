import os
from flask import render_template, jsonify
import app.utils.logger as logger
from app.services.api.answers_service import APIService
from app.services.answers.analyzer import AnswerAnalyzer

def most_frequent_words():
    logger.log_info("📡 Iniciando el análisis de las palabras más frecuentes...")
    try:
        # Obtener el ID de la empresa desde las variables de entorno
        enterprise_id = os.environ.get("ENTERPRISE_ID")
        num_common_words = os.environ.get("COMMON_WORDS")
    
        # Obtener las respuestas de la API
        api_data = APIService.get_answers(enterprise_id, "01-01-2023", "21-03-2023")
        
        # Filtrar las respuestas que tienen un custom_field no nulo y no vacío
        if api_data:
            valid_answers = [answer for answer in api_data["answers"] if answer["custom_field"] not in [None, '']]
        else:
            valid_answers = []

        logger.log_info("📝 Respuestas válidas obtenidas")
        
        # Analizar las respuestas válidas para obtener las palabras más frecuentes
        word_frequencies = AnswerAnalyzer.analyze_answers(valid_answers, enterprise_id, num_common_words)

        total = len(word_frequencies)

        logger.log_info("🎯 Análisis completo realizado")
        
        # Renderizar la plantilla y enviar los datos necesarios
        return render_template(
            "word_frequencies/index.html", 
            total=total,
            enterprise_id=enterprise_id,
            word_frequencies=word_frequencies
        )
    except Exception as e:
        logger.log_error(f"🔥 Se produjo un error durante el análisis: {e}")
        return jsonify(error="Se produjo un error mientras se procesaba tu solicitud."), 500