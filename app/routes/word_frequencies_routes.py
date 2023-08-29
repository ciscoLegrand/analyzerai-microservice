from flask import Blueprint, request
import app.utils.logger as logger
from app.controllers import word_frequencies_controller

word_frequencies_bp = Blueprint('word_frequencies', __name__, url_prefix='/word-frequencies')

@word_frequencies_bp.route('/<string:enterprise_id>', methods=['GET'])
def get_word_frequencies(enterprise_id):
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return word_frequencies_controller.most_frequent_words(enterprise_id, start_date, end_date)

@word_frequencies_bp.route('/publish', methods=['POST'])
def post_word_frequencies():
    logger.log_debug(f"🔊[post_word_frequencies] Request: {request}")
    return word_frequencies_controller.publish_word_frequencies()