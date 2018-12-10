"""This module registers all the urls for the routes"""

from .user import v2_user, Register, Login
from .incident import v2_incident, Incidences, AnIncident, UpdateLocation, UpdateComment,UpdateStatus

#authentication url -prefix(api/v2/)
v2_user.add_resource(Register, '/signup', strict_slashes=False)
v2_user.add_resource(Login, '/login', strict_slashes=False)

#incident url 
v2_incident.add_resource(Incidences, '/', strict_slashes=False)
v2_incident.add_resource(AnIncident, '/<int:incident_id>', strict_slashes=False)
v2_incident.add_resource(UpdateLocation,'/<int:incident_id>/location', strict_slashes=False)
v2_incident.add_resource(UpdateComment,'/<int:incident_id>/comment', strict_slashes=False)
v2_incident.add_resource(UpdateStatus,'/<int:incident_id>/status', strict_slashes=False)