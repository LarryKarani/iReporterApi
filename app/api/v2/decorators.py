from flask import Blueprint, jsonify
errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def url_not_found(e):
    """error for non_existent request"""
    return jsonify({"error": "Oops! wrong url"}), 404


@errors.app_errorhandler(500)
def internal_server_error(e):
    """error for serverside error"""
    return jsonify({"error": "Oops! Internal Server error"}), 500
