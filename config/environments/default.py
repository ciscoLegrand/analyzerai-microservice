class DefaultConfig:
    DEBUG = False
    TESTING = False
    BASE_URL = os.getenv('STAGING_URL')
    TOKEN = os.getenv('STAGING_TOKEN')
