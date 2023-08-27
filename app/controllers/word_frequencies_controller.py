from flask import jsonify
from app.services import analysis_service
import app.utils.logger as logger

def get_most_repeated_words(enterprise_id):
    try:
        result_df = analysis_service.word_frequency_analysis(enterprise_id)
        result = result_df.to_dict(orient='records')  # Convertir DataFrame a lista de diccionarios
        return jsonify(result), 200
    except Exception as e:
        logger.log_error(f"🔴 Error processing analysis for enterprise {enterprise_id}. Reason: {str(e)}")
        return jsonify({"error": "Failed to process analysis."}), 500

def analyze_word_frequency(enterprise_id):
    try:
        results = analysis_service.analyze_most_repeated_words(enterprise_id)
        # Como ahora 'results' ya es un diccionario, podemos devolverlo directamente como respuesta JSON.
        logger.log_info(f"✅ Analyze most repeated words are: {results}")
        return results
    except Exception as e:
        logger.log_error(f"🔴 Error processing analysis for enterprise {enterprise_id}. Reason: {str(e)}")
        return {"error": f"Failed to process analysis for enterprise {enterprise_id}. Reason: {str(e)}"}
