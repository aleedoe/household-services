from flask import request, jsonify, make_response
from app.models import db, Review
import math

def controller_get_reviews_admin():
    try:
        # Mendapatkan parameter halaman dari request query, default 1
        page = int(request.args.get('page', 1))
        limit = 12  # Membatasi 12 review per halaman
        offset = (page - 1) * limit

        # Menghitung total review dan jumlah halaman
        total_data = Review.query.count()
        total_pages = math.ceil(total_data / limit)

        # Query untuk mengambil review dengan pagination
        reviews_query = Review.query.offset(offset).limit(limit).all()

        # Membentuk list dari hasil query dengan informasi review
        reviews_list = [{
            "id": review.id,
            "service_request_id": review.service_request_id,
            "customer_id": review.customer_id,
            "customer_username": review.customer.username,  # Nama customer
            "professional_id": review.professional_id,
            "professional_username": review.professional.username,  # Nama profesional
            "rating": review.rating,
            "comments": review.comments,
            "created_at": review.created_at
        } for review in reviews_query]

        # Membentuk response dalam bentuk JSON
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
        # Mendapatkan parameter halaman dan professional_id dari query, default 1 dan None
        page = int(request.args.get('page', 1))
        limit = 12  # Membatasi 12 review per halaman
        offset = (page - 1) * limit

        # Mulai query dengan kondisi jika professional_id diberikan
        query = Review.query
        if professional_id:
            query = query.filter_by(professional_id=professional_id)

        # Menghitung total review dan jumlah halaman berdasarkan kondisi professional_id
        total_data = query.count()
        total_pages = math.ceil(total_data / limit)

        # Query untuk mengambil review dengan pagination
        reviews_query = query.offset(offset).limit(limit).all()

        # Membentuk list dari hasil query dengan informasi review
        reviews_list = [{
            "id": review.id,
            "service_request_id": review.service_request_id,
            "customer_id": review.customer_id,
            "customer_username": review.customer.username,  # Nama customer
            "professional_id": review.professional_id,
            "professional_username": review.professional.username,  # Nama profesional
            "rating": review.rating,
            "comments": review.comments,
            "created_at": review.created_at
        } for review in reviews_query]

        # Membentuk response dalam bentuk JSON
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