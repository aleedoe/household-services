from flask import request, jsonify, make_response
from app.models import db, ServiceProfessional
import math

def controller_get_service_professionals():
    try:
        page = int(request.args.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        total_data = ServiceProfessional.query.count()
        total_pages = math.ceil(total_data / limit)

        professionals_query = ServiceProfessional.query.offset(offset).limit(limit).all()
        professionals_list = [{
            "id": professional.id,
            "username": professional.username,
            "email": professional.email,
            "description": professional.description,
            "experience": professional.experience,
            "verified_status": professional.verified_status,
            "service": professional.service.name if professional.service else None,
            "created_at": professional.created_at
        } for professional in professionals_query]

        response = {
            'data': professionals_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching service professionals: {error}')
        return jsonify(error="Internal server error"), 500



def controller_delete_service_professional(professional_id):
    try:
        professional = ServiceProfessional.query.get(professional_id)
        if not professional:
            return jsonify(error="Service Professional not found"), 404

        db.session.delete(professional)
        db.session.commit()

        return jsonify(message="Service Professional deleted successfully"), 200

    except Exception as error:
        print(f'Error deleting service professional: {error}')
        return jsonify(error="Internal server error"), 500


def controller_get_service_professional_by_id(professional_id):
    try:
        professional = ServiceProfessional.query.get(professional_id)
        if not professional:
            return jsonify(error="Service Professional not found"), 404

        return jsonify({
            "id": professional.id,
            "service_id": professional.service_id,
            "username": professional.username,
            "email": professional.email,
            "description": professional.description,
            "experience": professional.experience,
            "verified_status": professional.verified_status,
            "created_at": professional.created_at
        }), 200

    except Exception as error:
        print(f'Error fetching service professional: {error}')
        return jsonify(error="Internal server error"), 500


def controller_create_service_professional():
    try:
        data = request.get_json()

        existing_professional = ServiceProfessional.query.filter((ServiceProfessional.username == data['username']) | (ServiceProfessional.email == data['email'])).first()
        if existing_professional:
            return jsonify(error="Username or email already exists"), 400

        new_professional = ServiceProfessional(
            service_id=data['service_id'],
            username=data['username'],
            email=data['email'],
            description=data.get('description'),
            experience=data['experience'],
            verified_status=data.get('verified_status', False)
        )
        new_professional.set_password(data['password'])

        db.session.add(new_professional)
        db.session.commit()

        return jsonify(message="Service Professional created successfully", professional_id=new_professional.id), 201

    except Exception as error:
        print(f'Error creating service professional: {error}')
        return jsonify(error="Internal server error"), 500


def controller_update_service_professional(professional_id):
    try:
        data = request.get_json()

        professional = ServiceProfessional.query.get(professional_id)
        if not professional:
            return jsonify(error="Service Professional not found"), 404

        if 'service_id' in data:
            professional.service_id = data['service_id']

        if 'username' in data:
            professional.username = data['username']

        if 'email' in data:
            existing_professional = ServiceProfessional.query.filter_by(email=data['email']).first()
            if existing_professional and existing_professional.id != professional_id:
                return jsonify(error="Email already exists"), 400
            professional.email = data['email']

        if 'description' in data:
            professional.description = data['description']

        if 'experience' in data:
            professional.experience = data['experience']

        if 'verified_status' in data:
            professional.verified_status = data['verified_status']

        if 'password' in data and data['password']:
            professional.set_password(data['password'])

        db.session.commit()

        return jsonify(message="Service Professional updated successfully"), 200

    except Exception as error:
        print(f'Error updating service professional: {error}')
        return jsonify(error="Internal server error"), 500

def controller_search_service_professionals():
    try:
        page = int(request.json.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        search_keyword = request.json.get('keyword', '')

        if search_keyword:
            # Pencarian menggunakan username atau email yang sesuai dengan keyword
            professionals_query = ServiceProfessional.query.filter(
                (ServiceProfessional.username.ilike(f'%{search_keyword}%')) |
                (ServiceProfessional.email.ilike(f'%{search_keyword}%'))
            )
        else:
            professionals_query = ServiceProfessional.query

        total_data = professionals_query.count()
        total_pages = math.ceil(total_data / limit)

        # Membatasi hasil pencarian dengan paginasi
        professionals_result = professionals_query.offset(offset).limit(limit).all()

        # Menyusun hasil pencarian dalam bentuk list of dict
        professionals_list = [{
            "id": professional.id,
            "service": professional.service.name if professional.service else None,
            "username": professional.username,
            "email": professional.email,
            "description": professional.description,
            "experience": professional.experience,
            "verified_status": professional.verified_status,
            "created_at": professional.created_at
        } for professional in professionals_result]

        response = {
            'data': professionals_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error searching service professionals: {error}')
        return jsonify(error="Internal server error"), 500
