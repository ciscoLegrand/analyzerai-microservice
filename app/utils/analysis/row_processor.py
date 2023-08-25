import re
from app.utils.analysis.stop_words import stop_words_loader
import app.utils.logger as logger

stop_words = stop_words_loader()

def process_row(answer: Answer, enterprise_comments_lists, enterprise_comments_count, all_comments_count, enterprise_id, enterprise_data):
    custom_field = answer.custom_field
    enterprise_id = answer.enterprise_id
    employee_id = answer.employee_id
    
    if not enterprise_id:
        logger.log_warning(f"⚠️ Skipping answer due to missing 'enterprise_id'. Answer: {answer}")
        return all_comments_count

    enterprise_info = enterprise_data[enterprise_id]
    enterprise_info['enterprise_name'] = answer.enterprise_name
    enterprise_info['year'] = answer.year
    enterprise_info['quarter'] = answer.quarter
    enterprise_info['total_answers'] += 1
    enterprise_info['unique_employee_ids'].add(employee_id)

    if custom_field and custom_field not in ['none', '']:
        custom_field = re.sub(r'[^\w\s]', ' ', custom_field).lower()
        custom_field_words = [word for word in custom_field.split() if word not in stop_words and len(word) > 1]
        enterprise_info['total_comments'] += 1
        enterprise_comments_count[enterprise_id] += 1
        record_text = [
            f"Registro #{enterprise_comments_count[enterprise_id]}",
            f"Enterprise ID: {enterprise_id}",
            f'Pregunta: {answer.description}',
            f'Comentario: {custom_field}',
            f'Nivel de satisfacción: {answer.satisfaction_level}'
        ]
        enterprise_comments_lists[enterprise_id].append(record_text)
        all_comments_count += 1
        general_record_text = [
            f"Registro #{all_comments_count}",
            f"Enterprise ID: {enterprise_id}",
            f'Pregunta: {answer.description}',
            f'Comentario: {custom_field}',
            f'Nivel de satisfacción: {answer.satisfaction_level}'
        ]
        enterprise_comments_lists["all"].append(general_record_text)
        enterprise_info['word_counts'].update(custom_field_words)
        for word in set(custom_field_words):
            enterprise_info['frequency_comments'][word] += 1
            enterprise_info['frequency_employees'][word].add(employee_id)
        enterprise_info['commenting_employees'].add(employee_id)

    return all_comments_count
