from flask import Blueprint

pageBlueprint = Blueprint('pages', __name__)

def register_blueprint_pages(app):
    app.register_blueprint(pageBlueprint)