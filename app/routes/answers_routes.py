from flask import Blueprint, render_template
from app.controllers import answers_controller
import app.utils.logger as logger

# Definir el Blueprint
answers_bp = Blueprint('answers', __name__, url_prefix='/ai')

@answers_bp.route('/')
def index():
    logger.log_info("Has hecho click en answers page!")
    return answers_controller.index()

@answers_bp.route('/get-answers', methods=['GET'])
def get_answers():
    response = answers_controller.get_answers()
    return response
