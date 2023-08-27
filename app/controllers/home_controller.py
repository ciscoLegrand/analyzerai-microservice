from flask import render_template, jsonify
from utils.logger import log_info, log_error, log_warning, log_debug

def home_page():
    log_info("😃 Bienvenido, estas en la home 😃") 
    return render_template('home/index.html')

def welcome_message():
    log_info("Has hecho click en home page!")
    return jsonify({"message": "¡Bienvenido, has hecho click en home page!"})
