from flask import Blueprint, render_template
from app.controllers import home_controller

# Definir el Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return home_controller.home_page()

@home_bp.route('/welcome-message', methods=['POST'])
def welcome():
    return home_controller.welcome_message()
