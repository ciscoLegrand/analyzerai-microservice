from flask import render_template, jsonify
import app.utils.logger as logger

def home_page():
    logger.log_info("😃 Bienvenido, estas en la home 😃") 
    return render_template('home/index.html')

def welcome_message():
    logger.log_info("Has hecho click en home page!")
    return jsonify({"message": "¡Bienvenido, has hecho click en home page!"})
