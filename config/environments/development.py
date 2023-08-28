import os
from .default import DefaultConfig

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    BASE_URL = os.getenv('DEVELOPMENT_URL')
    TOKEN = os.getenv('DEVELOPMENT_TOKEN')
    LOG_FILE = "logs/development.log"