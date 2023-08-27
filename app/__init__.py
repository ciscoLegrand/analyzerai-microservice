from flask import Flask
from config import configure_app
from app.routes import home_routes

def create_app(config_name='default'):
    app = Flask(__name__, template_folder="../templates")
    
    # Configuración basada en el nombre
    app.config.from_object(config[config_name])
    
    # Registrar el Blueprint
    app.register_blueprint(home_routes.home_bp)

    return app

