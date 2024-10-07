from app.views import apiBlueprint
from app.controllers.service import *

@apiBlueprint.route('/api/services', methods=['GET', 'POST'])
def manage_services():
    if request.method == 'GET':
        return controller_get_services()
    elif request.method == 'POST':
        return controller_create_service()

@apiBlueprint.route('/api/services/<int:service_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_service(service_id):
    if request.method == 'GET':
        return controller_get_service_by_id(service_id)
    elif request.method == 'PUT':
        return controller_update_service(service_id)
    elif request.method == 'DELETE':
        return controller_delete_service(service_id)


@apiBlueprint.route('/api/services/search', methods=['POST'])
def manage_search_service():
    return controller_search_services()
