import os

SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')

SQLALCHEMY_DATABASE_URI = 'sqlite:///household_service.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
