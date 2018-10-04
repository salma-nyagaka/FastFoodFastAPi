'''Set up environment specific configurations'''
import os

class Config():
    '''Parent configuration class'''
    DEBUG = False
    



class Development(Config):
    '''Configuration for development environment'''
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = 'fastfoodtest'
    SECRET_KEY = 'fastfoodtest'


class Testing(Config):
    '''Configuration for testing environment'''
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv('DATABASE_TEST_URL')

    JWT_SECRET_KEY = 'fastfoodtest'
    SECRET_KEY = 'fastfoodtest'


class Production(Config):
    '''Configuration for production environment'''
    DEBUG = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}