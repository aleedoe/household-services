from app.views import apiBlueprint
from app.controllers.admin import *


@apiBlueprint.route('/api/admins', methods=['GET'])
def get_admins():
    return controller_get_admins()