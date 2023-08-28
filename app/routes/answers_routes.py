from flask import Blueprint
from app.controllers import answers_controller

# Definir el Blueprint
answers_bp = Blueprint('answers', __name__, url_prefix='/answers')

@answers_bp.route('/')
def get_answers():
    return answers_controller.index()

@answers_bp.route('/frequently-words', methods=['GET'])
def get_most_frequent_words():
    return answers_controller.most_frequent_words()