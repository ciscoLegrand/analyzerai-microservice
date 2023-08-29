from flask import Blueprint, request
from app.controllers import answers_controller
from app.services.api.api_service import APIService

# Definir el Blueprint
answers_bp = Blueprint('answers', __name__, url_prefix='/answers')

@answers_bp.route('/<string:enterprise_id>')
def get_answers(enterprise_id):
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    return answers_controller.index(enterprise_id, start_date, end_date)

# @answers_bp.route('/frequently-words', methods=['GET'])
# def get_most_frequent_words():
#     return answers_controller.most_frequent_words()

