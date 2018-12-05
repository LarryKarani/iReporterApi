from flask import Flask,  jsonify
from app.api.v1 import v1_blueprint
from app.api.v1 import v1_api
from flask_jwt_extended import JWTManager


from .config import config

def create_app(config_name):
    """app factory creates the instance of the app"""
    app = Flask(__name__)

    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = '%****#@#'
    app.config.from_object(config[config_name])
    app.register_blueprint(v1_blueprint, url_prefix="/api/v1")
    api = v1_api

    jwt._set_error_handler_callbacks(api)
    
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "page not found"}), 404

    return app
    