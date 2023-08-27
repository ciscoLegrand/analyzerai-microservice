from flask import Blueprint, jsonify
from app.controllers import word_frequencies_controller as frequency
import app.utils.logger as logger

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/word-frequency/<string:enterprise_id>', methods=['GET'])
def get_word_frequency_analysis(enterprise_id):
    logger.log_info(f"🔎 Starting process to fetch answers from api and analyze words for enterprise {enterprise_id}...")
    if not enterprise_id:
        return jsonify({"error": "enterprise_id is required"}), 400

    response = frequency.analyze_word_frequency(enterprise_id)
    return jsonify(response), 200

# create a new route with test purpose to /test  
@analysis_bp.route('/test', methods=['GET'])
def test():
    logger.log_info(f"🔎 Testing routes ...")
    return jsonify({"message": "Test is running"}), 200