'''Set up environment specific configurations'''
import os


class Config():
    '''Parent configuration class'''
    DEBUG = False
    SECRET = os.getenv('SECRET')


class Development(Config):
    '''Configuration for development environment'''
    DEBUG = True


class Testing(Config):
    '''Configuration for testing environment'''
    DEBUG = True


class Production(Config):
    '''Configuration for production environment'''
    DEBUG = False


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
}
