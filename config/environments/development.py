import os
from .default import DefaultConfig

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    BASE_URL = os.getenv('STAGING_URL')
    TOKEN = os.getenv('STAGING_TOKEN')
