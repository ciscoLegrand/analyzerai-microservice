from flask import Blueprint
from app.controllers import word_frequencies_controller

word_frequencies_bp = Blueprint('word_frequencies', __name__)

@word_frequencies_bp.route('/word-frequencies/', methods=['GET'])
def get_word_frequencies():
    return word_frequencies_controller.most_frequent_words()
