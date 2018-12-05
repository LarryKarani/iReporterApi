from flask import Blueprint
from flask_restplus import Api

from app.api.v1.views.incidence_view import v1_incidence
from app.api.v1.views.user import v1_user

v1_blueprint =Blueprint('v1_blueprint', __name__, url_prefix='/api/v1')
v1_api = Api(v1_blueprint,
             title="iReporter",
             version="1",
             description="iReporter is an application that aims at fostering economic growth and reducing corruption in africa by allowing users to raise a redflag incase of a corruption incedence or create an intervention",
             contact_email="karanilarry@gmail.com",
             project_owner= "Andela_Kenya")

from app.api.v1.views import routes
v1_api.add_namespace(v1_incidence)
v1_api.add_namespace(v1_user)
            