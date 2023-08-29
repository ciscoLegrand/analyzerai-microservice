import os
import stat
from flask import Flask
from config import config
from app.utils.logger import initialize_logger, log_info, log_error, log_warning, log_debug
from app.utils import date_utils



from app.routes import home_routes, answers_routes, word_frequencies_routes, enterprises_routes

from app.handlers.error_handlers import (
    handle_400_error,
    handle_401_error,
    handle_403_error,
    handle_404_error,
    handle_405_error,
    handle_408_error,
    handle_500_error
)


def create_app(config_name='default'):
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(config[config_name])
    app.secret_key = 'super_fancy_secret_key'
    # usar decorador para utilizar el error handler a nivel de aplicación
    @app.errorhandler(400)
    def bad_request_error(error):
        return handle_400_error(error)

    @app.errorhandler(401)
    def unauthorized_error(error):
        return handle_401_error(error)

    @app.errorhandler(403)
    def forbidden_error(error):
        return handle_403_error(error)

    @app.errorhandler(404)
    def not_found_error(error):
        return handle_404_error(error)

    @app.errorhandler(405)
    def method_not_allowed_error(error):
        return handle_405_error(error)

    @app.errorhandler(408)
    def request_timeout_error(error):
        return handle_408_error(error)

    @app.errorhandler(500)
    def internal_server_error(error):
        return handle_500_error(error)

    #utils/helpers
    app.jinja_env.filters['quarter_dates'] = date_utils.quarter_dates

    # Registrar routes con Blueprint
    app.register_blueprint(home_routes.home_bp)
    app.register_blueprint(answers_routes.answers_bp)
    app.register_blueprint(word_frequencies_routes.word_frequencies_bp)
    app.register_blueprint(enterprises_routes.enterprises_bp)
    return app

