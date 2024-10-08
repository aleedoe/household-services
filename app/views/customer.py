from app.views import apiBlueprint
from app.controllers.customer import *

@apiBlueprint.route('/api/customers', methods=['GET', 'POST'])
def manage_customers():
    if request.method == 'GET':
        return controller_get_customers()
    elif request.method == 'POST':
        return controller_create_customer()

@apiBlueprint.route('/api/customers/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_customer(customer_id):
    if request.method == 'GET':
        return controller_get_customer_by_id(customer_id)
    elif request.method == 'PUT':
        return controller_update_customer(customer_id)
    elif request.method == 'DELETE':
        return controller_delete_customer(customer_id)


@apiBlueprint.route('/api/customers/search', methods=['POST'])
def manage_search_customer():
    return controller_search_customers()