"""Contains custom error messages."""


def bad_request(response):
    """request not processed due to client error"""
    return {'error': response, 'status': 400}, 400


def non_existent_content(response):
    """handles the error when a request is successfull but no content"""
    return {'error': response, 'status': 204}, 204


def request_not_found(response):
    """url or request does not exist"""
    return {'error': response, 'status': 404}, 404


def forbidden(response):
    """Request is not authorized to perfom the specific action"""
    return {'error': response, 'status': 403}, 403


def unauthorized(response):
    """request lacks authorizations"""
    return {'error': response, 'status': 401}, 401
