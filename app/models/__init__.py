from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

from .admin import Admin
from .customer import Customer
from .service import Service
from .service_professional import ServiceProfessional
from .service_request import ServiceRequest
from .review import Review