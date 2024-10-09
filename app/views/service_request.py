from app.views import apiBlueprint
from app.controllers.service_request import *

@apiBlueprint.route('/api/service-requests-sp', methods=['GET', 'POST'])
def manage_service_requests_sp():
    if request.method == 'GET':
        return controller_get_service_requests_sp()

@apiBlueprint.route('/api/service-assigned-sp', methods=['GET', 'POST'])
def manage_service_assigned_sp():
    if request.method == 'GET':
        return controller_get_service_assigned_sp()
    # elif request.method == 'POST':
    #     return controller_create_service_request_sp()

@apiBlueprint.route('/api/service-requests-sp/<int:request_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_service_request_sp(request_id):
    if request.method == 'GET':
        return
        # return controller_get_service_request_by_id_sp(request_id)
    elif request.method == 'PUT':
        return controller_update_service_status(request_id)
    elif request.method == 'DELETE':
        return controller_update_service_status(request_id)

# @apiBlueprint.route('/api/service-requests/sp/search', methods=['POST'])
# def manage_search_service_requests_sp():
#     return controller_search_service_requests_sp()
