"""This module registers all the urls for the routes"""

from .user import v2_user, Register, Login

#authentication url -prefix(api/v2/)
v2_user.add_resource(Register, '/register', strict_slashes=False)
v2_user.add_resource(Login, '/login', strict_slashes=False)