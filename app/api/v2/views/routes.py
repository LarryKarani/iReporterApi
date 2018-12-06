"""This module registers all the urls for the routes"""

from .user import v2_user, Register

#authentication url -prefix(api/v2/)
v2_user.add_resource(Register, '/register', strict_slashes=False)
