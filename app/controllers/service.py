from flask import request, jsonify, make_response
from app.models import db, Service
import math

def controller_get_services():
    try:
        page = int(request.args.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        total_data = Service.query.count()
        total_pages = math.ceil(total_data / limit)

        services_query = Service.query.offset(offset).limit(limit).all()
        services_list = [{
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "base_price": service.base_price,
            "time_required": service.time_required,
            "created_at": service.created_at,
            "updated_at": service.updated_at
        } for service in services_query]

        response = {
            'data': services_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching services: {error}')
        return jsonify(error="Internal server error"), 500


def controller_search_services():
    try:
        page = int(request.json.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        search_keyword = request.json.get('keyword', '')

        if search_keyword:
            services_query = Service.query.filter(Service.name.ilike(f'%{search_keyword}%'))
        else:
            services_query = Service.query

        total_data = services_query.count()
        total_pages = math.ceil(total_data / limit)

        services_result = services_query.offset(offset).limit(limit).all()
        services_list = [{
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "base_price": service.base_price,
            "time_required": service.time_required,
            "created_at": service.created_at,
            "updated_at": service.updated_at
        } for service in services_result]

        response = {
            'data': services_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error searching services: {error}')
        return jsonify(error="Internal server error"), 500


def controller_delete_service(service_id):
    try:
        service = Service.query.get(service_id)
        if not service:
            return jsonify(error="Service not found"), 404

        db.session.delete(service)
        db.session.commit()

        return jsonify(message="Service deleted successfully"), 200

    except Exception as error:
        print(f'Error deleting service: {error}')
        return jsonify(error="Internal server error"), 500


def controller_get_service_by_id(service_id):
    try:
        service = Service.query.get(service_id)
        if not service:
            return jsonify(error="Service not found"), 404

        return jsonify({
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "base_price": service.base_price,
            "time_required": service.time_required,
            "created_at": service.created_at,
            "updated_at": service.updated_at
        }), 200

    except Exception as error:
        print(f'Error fetching service: {error}')
        return jsonify(error="Internal server error"), 500


def controller_create_service():
    try:
        data = request.get_json()

        existing_service = Service.query.filter_by(name=data['name']).first()
        if existing_service:
            return jsonify(error="Service name already exists"), 400

        new_service = Service(
            name=data['name'],
            description=data.get('description'),
            base_price=data['base_price'],
            time_required=data['time_required']
        )
        db.session.add(new_service)
        db.session.commit()

        return jsonify(message="Service created successfully", service_id=new_service.id), 201

    except Exception as error:
        print(f'Error creating service: {error}')
        return jsonify(error="Internal server error"), 500


def controller_update_service(service_id):
    try:
        data = request.get_json()

        service = Service.query.get(service_id)
        if not service:
            return jsonify(error="Service not found"), 404

        if 'name' in data:
            service.name = data['name']

        if 'description' in data:
            service.description = data['description']

        if 'base_price' in data:
            service.base_price = data['base_price']

        if 'time_required' in data:
            service.time_required = data['time_required']

        db.session.commit()

        return jsonify(message="Service updated successfully"), 200

    except Exception as error:
        print(f'Error updating service: {error}')
        return jsonify(error="Internal server error"), 500
