import os
import traceback
from flask import render_template, jsonify, request, redirect, url_for, flash
import app.utils.logger as logger
from app.services.api.api_service import APIService
from app.services.answers.analyzer import AnswerAnalyzer

def most_frequent_words(enterprise_id, start_date, end_date):
    logger.log_info(f"📡 Iniciando el análisis de las palabras más frecuentes...{enterprise_id}, {start_date}, {end_date}")
    try:
        total = 0
        word_frequencies = []
        # Obtener el ID de la empresa desde las variables de entorno
        num_common_words = os.environ.get("COMMON_WORDS", 10)
        # Obtener los parámetros de la URL
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        logger.log_info(f"🧰[most_frequent_words] Parámetros de la URL: enterprise_id={enterprise_id}, start_date={start_date}, end_date={end_date}") 
        # Obtener las respuestas de la API
        api_data = APIService.get_answers(enterprise_id, start_date, end_date)
        
        # Filtrar las respuestas que tienen un custom_field no nulo y no vacío
        logger.log_info(f"📝 Respuestas obtenidas: {api_data}")
        if api_data:
            valid_answers = [answer for answer in api_data["answers"] if answer["custom_field"] not in [None, '']]
            logger.log_info(f"📝 Respuestas válidas obtenidas {len(valid_answers)}")
            if len(valid_answers) > 0:
                # Analizar las respuestas válidas para obtener las palabras más frecuentes
                word_frequencies = AnswerAnalyzer.analyze_answers(valid_answers, enterprise_id, num_common_words)
                total = len(word_frequencies)
                logger.log_info("🎯 Análisis completo realizado")
        else:
            valid_answers = []

        # Renderizar la plantilla y enviar los datos necesarios
        return render_template(
            "word_frequencies/index.html", 
            total=total,
            enterprise_id=enterprise_id,
            word_frequencies=word_frequencies
        )
    except Exception as e:
        tb_str = traceback.format_exc()
        logger.log_error(f"🔥[most_frequent_words] Se produjo un error durante el análisis: {e}\n{tb_str}")
        return jsonify(error="Se produjo un error mientras se procesaba tu solicitud."), 500

def publish_word_frequencies():
    logger.log_info(f"📡 Iniciando la publicación de las palabras más frecuentes...{request.form}")
    
    try:
        # Directamente extraemos los datos del formulario, ya que cada form envía solo un conjunto de datos.
        wf_data = {
            'enterprise_id': request.form.get('enterprise_id'),
            'year': request.form.get('year'),
            'quarter': request.form.get('quarter'),
            'word': request.form.get('word'),
            'frequency_word': request.form.get('frequency_word'),
            'frequency_comments': request.form.get('frequency_comments'),
            'frequency_employees': request.form.get('frequency_employees'),
            'total_answers': request.form.get('total_answers'),
            'total_comments': request.form.get('total_comments'),
            'total_employees': request.form.get('total_employees'),
            'total_employees_commenting': request.form.get('total_employees_commenting'),
            'word_frequency_ratio': request.form.get('word_frequency_ratio'),
            'employee_commenting_ratio': request.form.get('employee_commenting_ratio')
        }

        response = APIService.post_word_frequency(wf_data["enterprise_id"], wf_data)

        if not response:
            flash(f"Failed to publish word frequency for enterprise {wf_data['enterprise_id']}", 'error')
            logger.log_debug(f"🔊[publish_word_frequencies] API response: {response}")
            return redirect(url_for('home.home', enterprise_id=wf_data['enterprise_id']))
        elif response.get("message"):
            msg = response.get("message")
            logger.log_info(f"🔊[publish_word_frequencies] API message: {msg}")
            flash(msg, 'info')
        else:
            flash('Word frequencies published successfully', 'success')
    except Exception as e:
        tb_str = traceback.format_exc()
        logger.log_error(f"🔥[publish_word_frequencies] Error during word frequency publishing: {e}\n{tb_str}")
        flash("🔥 Error during word frequency publishing. Please try again.", 'error')

    return render_template('word_frequencies/publish_results.html')

