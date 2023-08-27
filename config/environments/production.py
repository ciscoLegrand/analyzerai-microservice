from .default import DefaultConfig

class DevelopmentConfig(DefaultConfig):
    DEBUG = false
    BASE_URL = os.getenv('PRODUCTION_URL')
    TOKEN = os.getenv('PRODUCTION_TOKEN')
