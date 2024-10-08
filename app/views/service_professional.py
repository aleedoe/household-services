from app.views import apiBlueprint
from app.controllers.service_professional import *

@apiBlueprint.route('/api/service-professionals', methods=['GET', 'POST'])
def manage_service_professionals():
    if request.method == 'GET':
        return controller_get_service_professionals()
    elif request.method == 'POST':
        return controller_create_service_professional()

@apiBlueprint.route('/api/service-professionals/<int:professional_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_service_professional(professional_id):
    if request.method == 'GET':
        return controller_get_service_professional_by_id(professional_id)
    elif request.method == 'PUT':
        return controller_update_service_professional(professional_id)
    elif request.method == 'DELETE':
        return controller_delete_service_professional(professional_id)

@apiBlueprint.route('/api/service-professionals/search', methods=['POST'])
def manage_search_service_professionals():
    return controller_search_service_professionals()