from flask import request, jsonify, make_response
from app.models import db, Review
import math

def controller_get_reviews_admin():
    try:
        page = int(request.args.get('page', 1))
        limit = 12
        offset = (page - 1) * limit

        total_data = Review.query.count()
        total_pages = math.ceil(total_data / limit)

        reviews_query = Review.query.offset(offset).limit(limit).all()

        reviews_list = [{
            "id": review.id,
            "service_request_id": review.service_request_id,
            "customer_id": review.customer_id,
            "customer_username": review.customer.username,
            "professional_id": review.professional_id,
            "professional_username": review.professional.username,
            "rating": review.rating,
            "comments": review.comments,
            "created_at": review.created_at
        } for review in reviews_query]

        response = {
            'data': reviews_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching reviews: {error}')
        return jsonify(error="Internal server error"), 500


def controller_get_reviews_sp(professional_id):
    try:
        page = int(request.args.get('page', 1))
        limit = 12
        offset = (page - 1) * limit

        query = Review.query
        if professional_id:
            query = query.filter_by(professional_id=professional_id)

        total_data = query.count()
        total_pages = math.ceil(total_data / limit)

        reviews_query = query.offset(offset).limit(limit).all()

        reviews_list = [{
            "id": review.id,
            "service_request_id": review.service_request_id,
            "customer_id": review.customer_id,
            "customer_username": review.customer.username,
            "professional_id": review.professional_id,
            "professional_username": review.professional.username,
            "rating": review.rating,
            "comments": review.comments,
            "created_at": review.created_at
        } for review in reviews_query]

        response = {
            'data': reviews_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching reviews: {error}')
        return jsonify(error="Internal server error"), 500


def controller_get_reviews_sp_by_service_request_id(service_request_id):
    try:
        review = Review.query.filter_by(service_request_id=service_request_id).first()

        if not review:
            return jsonify(error="Review not found"), 404

        review_data = {
            "id": review.id,
            "service_request_id": review.service_request_id,
            "customer_id": review.customer_id,
            "customer_username": review.customer.username,
            "professional_id": review.professional_id,
            "professional_username": review.professional.username,
            "rating": review.rating,
            "comments": review.comments,
            "created_at": review.created_at
        }

        response = {
            'data': review_data,
            'message': 'success'
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching review by service request: {error}')
        return jsonify(error="Internal server error"), 500
