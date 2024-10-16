from flask import request, jsonify, make_response
from app.models import db, ServiceProfessional, Review, Service, ServiceRequest
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

def controller_get_service_professionals_customer():
    try:
        page = int(request.args.get('page', 1))
        limit = 8
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
            "service_id": professional.service.id if professional.service else None,
            "service": professional.service.name if professional.service else None,
            "service_price": professional.service.base_price if professional.service else None,
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

def controller_get_unverified_service_professionals_admin():
    try:
        page = int(request.args.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        total_data = ServiceProfessional.query.filter_by(verified_status=False).count()
        total_pages = math.ceil(total_data / limit)

        professionals_query = ServiceProfessional.query.filter_by(verified_status=False).offset(offset).limit(limit).all()
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
        print(f'Error fetching unverified service professionals: {error}')
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

def controller_get_service_professional_by_id_customer(professional_id):
    try:
        professional = ServiceProfessional.query.get(professional_id)
        if not professional:
            return jsonify(error="Service Professional not found"), 404

        page = int(request.args.get('page', 1))
        limit = 12
        offset = (page - 1) * limit

        review_query = Review.query.filter_by(professional_id=professional_id)
        total_data = review_query.count()
        total_pages = math.ceil(total_data / limit)

        reviews_query = (Review.query
                         .join(ServiceRequest, Review.service_request_id == ServiceRequest.id)
                         .join(Service, ServiceRequest.service_id == Service.id)
                         .filter(Review.professional_id == professional_id)
                         .offset(offset)
                         .limit(limit)
                         .all())

        reviews_list = [{
            "id": review.id,
            "service_id": review.service_request.service.id,
            "service_name": review.service_request.service.name,
            "customer_id": review.customer_id,
            "customer_username": review.customer.username,
            "professional_id": review.professional_id,
            "professional_username": review.professional.username,
            "rating": review.rating,
            "comments": review.comments,
            "created_at": review.created_at
        } for review in reviews_query]

        return jsonify({
            "id": professional.id,
            "service_id": professional.service_id,
            "username": professional.username,
            "email": professional.email,
            "description": professional.description,
            "reviews": reviews_list,
            "service": professional.service.name if professional.service else None,
            "experience": professional.experience,
            "verified_status": professional.verified_status,
            "created_at": professional.created_at,
            "total_pages": total_pages,
            "total_data": total_data
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
            professionals_query = ServiceProfessional.query.filter(
                (ServiceProfessional.username.ilike(f'%{search_keyword}%')) |
                (ServiceProfessional.email.ilike(f'%{search_keyword}%'))
            )
        else:
            professionals_query = ServiceProfessional.query

        total_data = professionals_query.count()
        total_pages = math.ceil(total_data / limit)

        professionals_result = professionals_query.offset(offset).limit(limit).all()

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


def assign_verified_status(professional_id, status):
    try:
        professional = ServiceProfessional.query.get_or_404(professional_id)
        
        if status == 'true':
            professional.verified_status = True
        elif status == 'false':
            professional.verified_status = False
        else:
            return {"error": "Invalid verified status value"}, 400

        db.session.commit()

        return {
            "message": "Service professional status updated successfully",
            "verified_status": professional.verified_status
        }, 200

    except Exception as error:
        print(f"Error updating service professional: {error}")
        return {"error": "Internal server error"}, 500


def reject_verified_status(professional_id):
    try:
        professional = ServiceProfessional.query.get_or_404(professional_id)
        
        professional.verified_status = False
        db.session.commit()

        return {
            "message": "Service professional verification rejected",
            "verified_status": professional.verified_status
        }, 200

    except Exception as error:
        print(f"Error rejecting service professional: {error}")
        return {"error": "Internal server error"}, 500