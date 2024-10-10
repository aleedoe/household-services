from flask import Blueprint

apiBlueprint = Blueprint('api', __name__)

from app.views.admin import *
from app.views.customer import *
from app.views.service import *
from app.views.service_professional import *
from app.views.service_request import *
from app.views.review import *


def register_blueprint_views(app):
    app.register_blueprint(apiBlueprint)