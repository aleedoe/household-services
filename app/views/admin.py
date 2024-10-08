from app.views import apiBlueprint
from app.controllers.admin import *


@apiBlueprint.route('/api/admins', methods=['GET', 'POST'])
def manage_admins():
    if request.method == 'GET':
        return controller_get_admins()
    elif request.method == 'POST':
        return controller_create_admin()

@apiBlueprint.route('/api/admins/<int:admin_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_admin(admin_id):
    if request.method == 'GET':
        return controller_get_admin_by_id(admin_id)
    elif request.method == 'PUT':
        return controller_update_admin(admin_id)
    elif request.method == 'DELETE':
        return controller_delete_admin(admin_id)


@apiBlueprint.route('/api/admins/search', methods=['POST'])
def manage_search_admin():
    return controller_search_admins()