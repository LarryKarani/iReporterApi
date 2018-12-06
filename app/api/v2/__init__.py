from flask import Blueprint
from flask_restplus import Api

from app.api.v2.views.user import v2_user

v2_blueprint =Blueprint('v2_blueprint', __name__, url_prefix='/api/v2')
v2_api = Api(v2_blueprint,
             title="iReporter",
             version="2",
             description="iReporter is an application that aims at fostering economic growth and reducing corruption in africa by allowing users to raise a redflag incase of a corruption incedence or create an intervention",
             contact_email="karanilarry@gmail.com",
             project_owner= "Andela_Kenya")

from app.api.v2.views import routes
v2_api.add_namespace(v2_user)