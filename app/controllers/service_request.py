from flask import request, jsonify, make_response
from app.models import db, ServiceRequest
import math
from datetime import datetime

def controller_get_service_requests():
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
            "customer_name": service_request.customer.username,
            "service_name": service_request.service.name,
            "professional_name": service_request.professional.username if service_request.professional else None
        } for service_request in service_requests_query]

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


def add_service_request():
    try:
        data = request.get_json()

        if not data.get('customer_id') or not data.get('service_id') or not data.get('location'):
            return make_response(jsonify({"error": "Missing required fields"}), 400)

        service_request = ServiceRequest(
            customer_id=data['customer_id'],
            service_id=data['service_id'],
            professional_id=data.get('professional_id', None),
            date_of_request=datetime.now(),
            date_of_completion=None,
            service_status='requested',
            remarks=data.get('remarks', None),
            location=data['location'],
            total_price=data['total_price']
        )

        db.session.add(service_request)
        db.session.commit()

        response = {
            'message': 'Service request added successfully',
            'data': {
                'id': service_request.id,
                'customer_id': service_request.customer_id,
                'service_id': service_request.service_id,
                'professional_id': service_request.professional_id,
                'date_of_request': service_request.date_of_request,
                'service_status': service_request.service_status,
                'remarks': service_request.remarks,
                'location': service_request.location,
                'total_price': service_request.total_price
            }
        }

        return make_response(jsonify(response)), 201

    except Exception as error:
        print(f'Error adding service request: {error}')
        return jsonify(error="Internal server error"), 500

def controller_get_service_requests_customer(customer_id):
    try:
        service_requests_query = ServiceRequest.query.filter_by(customer_id=customer_id).all()

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
            "customer_name": service_request.customer.username,
            "service_name": service_request.service.name,
            "professional_name": service_request.professional.username if service_request.professional else None
        } for service_request in service_requests_query]

        response = {
            'data': service_requests_list,
            'message': 'success',
            'total_data': len(service_requests_list)
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching service requests: {error}')
        return jsonify(error="Internal server error"), 500

def controller_get_service_requests_sp():
    try:
        page = int(request.args.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        total_data = ServiceRequest.query.filter_by(service_status='requested').count()
        total_pages = math.ceil(total_data / limit)

        service_requests_query = ServiceRequest.query.filter_by(service_status='requested') \
            .offset(offset).limit(limit).all()

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
            "customer_name": service_request.customer.username,
            "service_name": service_request.service.name,
            "professional_name": service_request.professional.username if service_request.professional else None
        } for service_request in service_requests_query]

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

def controller_get_service_assigned_sp():
    try:
        page = int(request.args.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        total_data = ServiceRequest.query.filter_by(service_status='assigned').count()
        total_pages = math.ceil(total_data / limit)

        service_requests_query = ServiceRequest.query.filter_by(service_status='assigned') \
            .offset(offset).limit(limit).all()

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
            "customer_name": service_request.customer.username,
            "service_name": service_request.service.name,
            "professional_name": service_request.professional.username if service_request.professional else None
        } for service_request in service_requests_query]

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

def controller_update_service_status(service_request_id):
    try:
        new_status = request.json.get('service_status')
        
        if not new_status or new_status not in ['requested', 'assigned', 'closed', 'rejected']:
            return jsonify(error="Invalid service status"), 400
        
        service_request = ServiceRequest.query.get(service_request_id)
        
        if not service_request:
            return jsonify(error="Service request not found"), 404
        
        service_request.service_status = new_status
        
        if new_status in ['closed', 'rejected']:
            service_request.date_of_completion = datetime.now()

        db.session.commit()

        return jsonify(message="Service status updated successfully"), 200
    
    except Exception as error:
        print(f'Error updating service status: {error}')
        return jsonify(error="Internal server error"), 500


