import pandas as pd
import traceback
from collections import Counter, defaultdict
import app.utils.logger as logger
from app.models.word_frequency import WordFrequency
from app.utils.analysis.stop_words import stop_words_loader

class AnswerAnalyzer:
    
    @staticmethod
    def tokenize_and_clean(text, stop_words):
        logger.log_info("🔠 Tokenizando y limpiando texto...")
        try:
            words = text.lower().split()
            filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
            return filtered_words
        except Exception as e:
            tb_str = traceback.format_exc()
            logger.log_error(f"🔥[AnswerAnalyzer.tokenize_and_clean] Error durante la tokenización y limpieza del texto: {e}\n{tb_str}")
            return []

    @staticmethod
    def analyze_row(row, enterprise_id, enterprise_data, stop_words):
        logger.log_info("📝 Analizando respuesta individual...")
        try:
            logger.log_debug(f"🐳 Respuesta row: {row}\n🐳 Enterprise data: {enterprise_data}") 
            description = row['custom_field']
            employee_id = row['employee_id']
            tokens = AnswerAnalyzer.tokenize_and_clean(description, stop_words)

            enterprise_info = enterprise_data.get(enterprise_id, {
                'word_counts': Counter(),
                'total_comments': 0,
                'unique_employee_ids': set(),
                'commenting_employees': set(),
                'frequency_comments': defaultdict(int),
                'frequency_employees': defaultdict(set)
            })
            
            enterprise_info['word_counts'].update(tokens)
            enterprise_info['total_comments'] += 1
            enterprise_info['unique_employee_ids'].add(employee_id)
            for word in set(tokens):
                enterprise_info['frequency_comments'][word] += 1
                enterprise_info['frequency_employees'][word].add(employee_id)
            if description:
                enterprise_info['commenting_employees'].add(employee_id)
            
            logger.log_info("📊 Respuesta individual analizada")
            enterprise_data[enterprise_id] = enterprise_info
        except Exception as e:
            tb_str = traceback.format_exc()
            logger.log_error(f"🔥[AnswerAnalyzer.analyze_row] Error durante el análisis de la respuesta individual: {e}\n{tb_str}")

    @staticmethod
    def analyze_answers(answers, enterprise_id, num_common_words=10):
        logger.log_info("📝 Comenzando análisis completo de respuestas...")
        try:

            df = pd.DataFrame(answers)
            all_stopwords = stop_words_loader()

            enterprise_data = {}
            df.apply(lambda row: AnswerAnalyzer.analyze_row(row, enterprise_id, enterprise_data, all_stopwords), axis=1)
            
            info = enterprise_data.get(enterprise_id, {})
            result = []
            logger.log_info(f"📊 Enterprise data: {info}")
            # Asegúrate de que num_common_words es un entero
            num_common_words = int(num_common_words)

            # Ordenar las palabras por su frecuencia y limitar a las palabras más comunes
            sorted_words = sorted(info['word_counts'].items(), key=lambda x: x[1], reverse=True)[:num_common_words]
        
            for word, count in sorted_words:
                data = {
                    'year': '2023',
                    'quarter': '1',
                    'word': word,
                    'frequency_word': count,
                    'frequency_employees': len(info['frequency_employees'][word]),
                    'frequency_comments': info['frequency_comments'][word],
                    'total_answers': len(answers),
                    'total_comments': info['total_comments'],
                    'total_employees': len(info['unique_employee_ids']),
                    'total_employees_commenting': len(info['commenting_employees']),
                    'enterprise_id': enterprise_id
                }
                word_frequency = WordFrequency(data)
                logger.log_info(f"📊 Respuesta completa analizada: {word_frequency}")
                result.append(word_frequency)
            
            return result
        except Exception as e:
            tb_str = traceback.format_exc()
            logger.log_error(f"🔥[AnswerAnalyzer.analyze_answers] Error durante el análisis completo de respuestas: {e}\n{tb_str}")
            return []
