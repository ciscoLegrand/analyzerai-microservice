import os
class DefaultConfig:
    DEBUG = False
    TESTING = False
    BASE_URL = os.getenv('DEVELOPMENT_URL')
    TOKEN = os.getenv('DEVELOPMENT_TOKEN')
    LOG_FILE = "logs/development.log"