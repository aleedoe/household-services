from app.views import apiBlueprint
from app.controllers.review import *

@apiBlueprint.route('/api/review-sp/<int:professional_id>', methods=['GET', 'POST'])
def manage_review_sp(professional_id):
    if request.method == 'GET':
        return controller_get_reviews_sp(professional_id)
#     elif request.method == 'POST':
#         return controller_create_customer()

@apiBlueprint.route('/api/review-sp/review/<int:review_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_review(review_id):
    if request.method == 'GET':
        return controller_get_reviews_sp_by_service_request_id(review_id)
#     elif request.method == 'PUT':
#         return controller_update_customer(customer_id)
#     elif request.method == 'DELETE':
#         return controller_delete_customer(customer_id)


# @apiBlueprint.route('/api/customers/search', methods=['POST'])
# def manage_search_customer():
#     return controller_search_customers()