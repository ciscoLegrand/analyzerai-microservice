from flask import render_template, jsonify

def home_page():
    return render_template('home.html')

def welcome_message():
    return jsonify({"message": "¡Bienvenido, has hecho click en home page!"})
