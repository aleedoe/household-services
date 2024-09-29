from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import *

def create_app():
    app = Flask(__name__)

    migrate = Migrate(app, db)

    from app.views import register_blueprint_views
    register_blueprint_views(app)
    
    from app.routes import register_blueprint_pages
    register_blueprint_pages(app)
    
    app.config.from_pyfile('../config.py')

    db.init_app(app)

    return app