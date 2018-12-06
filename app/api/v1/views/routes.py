"""This module registers all the urls for the routes"""
from .incidence_view import (v1_incidence, Incidences, AnIncidence, UpdateLocation,
                            UpdateComment, UpdateStatus)
from .user import v1_user, Register, Login

#incidents url -prefix(api/v1/red-flags)
v1_incidence.add_resource(Incidences, '/' , strict_slashes=False)
v1_incidence.add_resource(AnIncidence, '/<int:red_id>', strict_slashes=False)
v1_incidence.add_resource(UpdateLocation, '/<int:red_id>/location', strict_slashes=False)
v1_incidence.add_resource(UpdateComment, '/<int:red_id>/comment', strict_slashes=False)
v1_incidence.add_resource(UpdateStatus, '/<int:red_id>/status', strict_slashes=False)
        
#authentication url -prefix(api/v1/)
v1_user.add_resource(Register, '/register', strict_slashes=False)
v1_user.add_resource(Login, '/login', strict_slashes=False)
