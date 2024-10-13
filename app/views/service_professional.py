from app.views import apiBlueprint
from app.controllers.service_professional import *

@apiBlueprint.route('/api/service-professionals-customer', methods=['GET', 'POST'])
def manage_service_professionals_customer():
    if request.method == 'GET':
        return controller_get_service_professionals_customer()

@apiBlueprint.route('/api/unverified-service-professionals', methods=['GET'])
def get_unverified_service_professionals_admin():
    return controller_get_unverified_service_professionals_admin()

        

@apiBlueprint.route('/api/service-professionals', methods=['GET', 'POST'])
def manage_service_professionals():
    if request.method == 'GET':
        return controller_get_service_professionals()
    elif request.method == 'POST':
        return controller_create_service_professional()

@apiBlueprint.route('/api/service-professionals-customer/<int:professional_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_service_professional_customer(professional_id):
    if request.method == 'GET':
        return controller_get_service_professional_by_id_customer(professional_id)

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



@apiBlueprint.route('/api/verified-service-professionals/<int:professional_id>', methods=['PUT'])
def update_service_professional_assign(professional_id):
    data = request.get_json()

    if 'verified_status' not in data:
        return jsonify({"error": "verified_status field is required"}), 400

    status = data['verified_status']
    response, status_code = assign_verified_status(professional_id, status)
    
    return jsonify(response), status_code


@apiBlueprint.route('/api/verified-service-professionals/<int:professional_id>', methods=['DELETE'])
def update_service_professional_reject(professional_id):
    response, status_code = reject_verified_status(professional_id)
    
    return jsonify(response), status_code