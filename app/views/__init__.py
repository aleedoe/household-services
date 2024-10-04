from flask import Blueprint

apiBlueprint = Blueprint('api', __name__)

from app.views.admin import *

def register_blueprint_views(app):
    app.register_blueprint(apiBlueprint)