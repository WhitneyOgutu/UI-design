import os


class Config:
    """Contains common configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY')

 
class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
