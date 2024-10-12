from app.views import apiBlueprint
from app.controllers.auth import *

@apiBlueprint.route('/api/login-admin', methods=['POST'])
def login_admin():
    return controller_admin_login()

@apiBlueprint.route('/api/login-customer', methods=['POST'])
def login_customer():
    return controller_customer_login()

@apiBlueprint.route('/api/register-customer', methods=['POST'])
def register_customer():
    return controller_register_customer()

@apiBlueprint.route('/api/register-service_pro', methods=['POST'])
def register_service_pro():
    return controller_register_service_pro()