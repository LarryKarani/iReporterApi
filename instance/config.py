"""This module handles app configuration settings """

import os
class Config:
    """This class holds a common config for all environments"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or '@#57#%@'

class DevelopmentConfig(Config):
    """Configurations for the development environment"""
    DEBUG = True


class TestingConfig(Config):
    """configuration for the testing environment"""
    DEBUG = True

class ProductionConfig(Config):
    """configuration for the production environment"""
    DEBUG = False


config = {
       'development': DevelopmentConfig,
       'testing'    : TestingConfig,
       'production': ProductionConfig,
       'default': DevelopmentConfig
}