import os
from .default import DefaultConfig

class ProductionConfig(DefaultConfig):
    DEBUG = False
    BASE_URL = os.getenv('PRODUCTION_URL')
    TOKEN = os.getenv('PRODUCTION_TOKEN')
    LOG_FILE = "logs/production.log"