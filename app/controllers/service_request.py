from flask import request, jsonify, make_response
from app.models import db, ServiceRequest
import math

def controller_get_service_requests_sp():
    try:
        page = int(request.args.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        total_data = ServiceRequest.query.count()
        total_pages = math.ceil(total_data / limit)

        service_requests_query = ServiceRequest.query.offset(offset).limit(limit).all()

        service_requests_list = [{
            "id": service_request.id,
            "customer_id": service_request.customer_id,
            "service_id": service_request.service_id,
            "professional_id": service_request.professional_id,
            "date_of_request": service_request.date_of_request,
            "date_of_completion": service_request.date_of_completion,
            "service_status": service_request.service_status,
            "remarks": service_request.remarks,
            "location": service_request.location,
            "total_price": service_request.total_price,
            "customer_name": service_request.customer.name,
            "service_name": service_request.service.name,
            "professional_name": service_request.professional.name if service_request.professional else None
        } for service_request in service_requests_query]

        # Membuat response JSON
        response = {
            'data': service_requests_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching service requests: {error}')
        return jsonify(error="Internal server error"), 500
