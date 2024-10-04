from flask import request, jsonify, make_response
from app.models import db, Service
import math

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
            existing_service = Service.query.filter_by(name=data['name']).first()
            if existing_service and existing_service.id != service_id:
                return jsonify(error="Service name already exists"), 400
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
