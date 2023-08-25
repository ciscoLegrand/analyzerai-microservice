
from flask import Flask
from app.routes import analysis_routes
from app.handlers import error_handlers

def create_app():
    app = Flask(__name__)
    
    # Registrar blueprints
    app.register_blueprint(analysis_routes.analysis_bp, url_prefix='/ai')

    # Configurar manejo de errores
    app.register_error_handler(400, error_handlers.handle_400_error)
    app.register_error_handler(401, error_handlers.handle_401_error)
    app.register_error_handler(403, error_handlers.handle_403_error)
    app.register_error_handler(404, error_handlers.handle_404_error)
    app.register_error_handler(405, error_handlers.handle_405_error)
    app.register_error_handler(408, error_handlers.handle_408_error)
    app.register_error_handler(500, error_handlers.handle_500_error)

    return app
