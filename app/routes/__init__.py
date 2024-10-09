from flask import Blueprint, render_template, request, redirect, url_for, session, flash

pageBlueprint = Blueprint('pages', __name__)

from app.routes.test import *
from app.routes.admin import *
from app.routes.service_professional import *

def register_blueprint_pages(app):
    app.register_blueprint(pageBlueprint)