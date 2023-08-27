import os
from .environments.default import DefaultConfig
from .environments.development import DevelopmentConfig
from .environments.production import ProductionConfig

config = {
    'default': DefaultConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

def configure_app(app):
    config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[config_name])
