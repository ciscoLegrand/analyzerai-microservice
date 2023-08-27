import os
from .environments.default import DefaultConfig

config = {
    'development': 'config.environments.development.DevelopmentConfig',
    'production': 'config.environments.production.ProductionConfig',
    'default': 'config.environments.default.DefaultConfig'
}

def configure_app(app):
    config_name = os.getenv('ENVIRONMENT', 'development')
    app.config.from_object(config[config_name])
