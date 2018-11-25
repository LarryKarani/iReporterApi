from flask import Flask,  Blueprint
from flask_restplus import Api

from .config import config

def create_app(config_name):
    """app factory creates the instance of the app"""
    app = Flask(__name__)

    api = Api(
           app=app, version='1.0', 
           title='iReporter API',
           description='Fighting Corruption and fostering economic development\
            through creating corruption red-flags and interventions')

    #add urls or namespaces here

    app.config.from_object(config[config_name])

    return app