"""This module handles app configuration settings """

import os


class Config:
    """This class holds a common config for all environments"""
    SECRET_KEY = os.getenv('SECRET_KEY') or '@#57#%@'
    db_url = os.getenv('DATABASE_URL')
    UPLOAD_FOLDER = "upload"


class DevelopmentConfig(Config):
    """Configurations for the development environment"""
    DEBUG = True


class TestingConfig(Config):
    """configuration for the testing environment"""
    DEBUG = True
    db_url = os.getenv('TEST_DATABASE_URL')


class ProductionConfig(Config):
    """configuration for the production environment"""
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
