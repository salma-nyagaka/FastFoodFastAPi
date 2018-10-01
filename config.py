'''Set up environment specific configurations'''
import os

class Config():
    '''Parent configuration class'''
    DEBUG = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class Development(Config):
    '''Configuration for development environment'''
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class Testing(Config):
    '''Configuration for testing environment'''
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_TEST_URL')

class Production(Config):
    '''Configuration for production environment'''
    DEBUG = False


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}