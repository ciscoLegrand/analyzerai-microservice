import re
from app.models import Answer, FrequentlyWord
from app.utils.analysis.stop_words import stop_words_loader
import app.utils.logger as logger
from collections import defaultdict, Counter

stop_words = stop_words_loader()

def analyze_single_enterprise(answers_list, enterprise_id, year, quarter):
    logger.log_info(f"🛑 Stop words loaded: {len(stop_words)}")
    # Inicializar un diccionario para almacenar la información de la empresa
    enterprise_info = {
        'word_counts': Counter(),
        'frequency_comments': defaultdict(int),
        'frequency_employees': defaultdict(set),
        'total_comments': 0,
        'unique_employee_ids': set(),
        'total_answers': 0,
        'commenting_employees': set()
    }

    # Procesar cada respuesta en answers_list
    # log type of items of answer list 
    logger.log_debug(f"🔎 {answers_list.__class__}")

    for answer in answers_list:
        # Actualizar contador de respuestas y conjunto de empleados únicos
        enterprise_info['total_answers'] += 1
        enterprise_info['unique_employee_ids'].add(answer.employee_id)

        # Procesar el campo 'custom_field' si tiene contenido relevante
        custom_field = answer.custom_field
        if custom_field and custom_field not in ['none', '']:
            custom_field = re.sub(r'[^\w\s]', ' ', custom_field).lower()
            custom_field_words = [word for word in custom_field.split() if word not in stop_words and len(word) > 1]

            # Actualizar contador de comentarios
            enterprise_info['total_comments'] += 1

            # Actualizar contadores de palabras y frecuencias
            enterprise_info['word_counts'].update(custom_field_words)
            for word in set(custom_field_words):
                enterprise_info['frequency_comments'][word] += 1
                enterprise_info['frequency_employees'][word].add(answer.employee_id)

            # Añadir al conjunto de empleados que comentan
            enterprise_info['commenting_employees'].add(answer.employee_id)
            logger.log_debug(f"🤢 {enterprise_info}\n")
    # Obtener las 10 palabras más repetidas
    most_common_words = enterprise_info['word_counts'].most_common(10)

    # Crear y devolver una lista de 10 objetos RepeatedWord para las palabras más repetidas
    repeated_word_objects = []
    for word, count in most_common_words:
        data = {
            'enterprise_id': enterprise_id,
            'year': year,
            'quarter': quarter,
            'word_counts': {word: count},
            'frequency_comments': {word: enterprise_info['frequency_comments'][word]},
            'frequency_employees': {word: enterprise_info['frequency_employees'][word]},
            'total_comments': enterprise_info['total_comments'],
            'unique_employee_ids': enterprise_info['unique_employee_ids'],
            'total_answers': enterprise_info['total_answers'],
            'commenting_employees': enterprise_info['commenting_employees']
        }
        logger.log_debug(f"🥶 {data}\n")
        repeated_word_objects.append(FrequentlyWord(data))

    logger.log_info(f"📖 Most common words for enterprise {enterprise_id}: {repeated_word_objects}") 
    return repeated_word_objects
