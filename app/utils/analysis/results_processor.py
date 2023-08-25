import pandas as pd

def process_final_results(enterprise_data):
    results = []
    for enterprise_id, enterprise_info in enterprise_data.items():
        enterprise_info['total_employees'] = len(enterprise_info['unique_employee_ids'])
        enterprise_info['total_employees_commenting'] = len(enterprise_info['commenting_employees'])
        total_comments = enterprise_info['total_comments']
        most_common_words = enterprise_info['word_counts'].most_common(10)
        
        for word, count in most_common_words:
            frequency_word = count
            frequency_comments = enterprise_info['frequency_comments'].get(word, 0)
            frequency_employees = len(enterprise_info['frequency_employees'].get(word, set()))
            enterprise_name = enterprise_info['enterprise_name']
            year = enterprise_info['year']
            quarter = enterprise_info['quarter']
            
            logger.log_info(f"📝 total_comments: {total_comments}")
            logger.log_info(f"🔍 enterprise_id: {enterprise_id}")
            logger.log_info(f"👥 frequency_word: {frequency_word}")
            logger.log_info(f"💬 frequency_employees: {frequency_employees}")
            
            word_frequency = {
                'enterprise_id': enterprise_id,
                'year': year,
                'quarter': quarter,
                'word': word,
                'frequency_word': frequency_word,
                'frequency_comments': frequency_comments,
                'frequency_employees': frequency_employees,
                'total_comments': total_comments
            }
            results.append(word_frequency)

    # después de procesar todos los datos, se crea un DataFrame final (final_df) con los resultados y se ordena según las columnas mencionadas anteriormente. Se agrega una nueva columna 'index' que es un contador acumulado basado en el enterprise_id, y finalmente, se establece esa columna como el índice del DataFrame.
    final_df = pd.DataFrame(results)
    final_df = final_df.sort_values(by=['enterprise_id', 'year', 'quarter', 'frequency_word', 'frequency_comments', 'word'], ascending=[True, True, True, False, False, True])
    final_df['index'] = final_df.groupby('enterprise_id').cumcount() + 1
    final_df = final_df.set_index('index')
    
    return final_df

