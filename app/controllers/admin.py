from flask import request, jsonify, make_response
from app.models import db, Admin
import math

def controller_get_admins():
    try:
        page = int(request.args.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        total_data = Admin.query.count()
        total_pages = math.ceil(total_data / limit)

        admins_query = Admin.query.offset(offset).limit(limit).all()
        admins_list = [{"id": admin.id, "username": admin.username, "email": admin.email} for admin in admins_query]

        response = {
            'data': admins_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error fetching admins: {error}')
        return jsonify(error="Internal server error"), 500

def controller_search_admins():
    try:
        page = int(request.json.get('page', 1))
        limit = 5
        offset = (page - 1) * limit

        search_keyword = request.json.get('keyword', '')

        if search_keyword:
            admins_query = Admin.query.filter(
                (Admin.username.ilike(f'%{search_keyword}%')) | 
                (Admin.email.ilike(f'%{search_keyword}%'))
            )
        else:
            admins_query = Admin.query

        total_data = admins_query.count()
        total_pages = math.ceil(total_data / limit)

        admins_result = admins_query.offset(offset).limit(limit).all()

        admins_list = [{
            "id": admin.id,
            "username": admin.username,
            "email": admin.email
        } for admin in admins_result]

        response = {
            'data': admins_list,
            'message': 'success',
            'total_pages': total_pages,
            'total_data': total_data
        }

        return make_response(jsonify(response)), 200

    except Exception as error:
        print(f'Error searching admins: {error}')
        return jsonify(error="Internal server error"), 500


def controller_delete_admin(admin_id):
    try:
        admin = Admin.query.get(admin_id)
        if not admin:
            return jsonify(error="Admin not found"), 404

        db.session.delete(admin)
        db.session.commit()

        return jsonify(message="Admin deleted successfully"), 200

    except Exception as error:
        print(f'Error deleting admin: {error}')
        return jsonify(error="Internal server error"), 500


def controller_get_admin_by_id(admin_id):
    try:
        admin = Admin.query.get(admin_id)
        if not admin:
            return jsonify(error="Admin not found"), 404

        return jsonify({
            "id": admin.id,
            "username": admin.username,
            "email": admin.email
        }), 200

    except Exception as error:
        print(f'Error fetching admin: {error}')
        return jsonify(error="Internal server error"), 500


def controller_create_admin():
    try:
        data = request.get_json()

        existing_admin = Admin.query.filter((Admin.username == data['username']) | (Admin.email == data['email'])).first()
        if existing_admin:
            return jsonify(error="Username or email already exists"), 400

        new_admin = Admin(
            username=data['username'],
            email=data['email']
        )
        new_admin.set_password(data['password'])

        db.session.add(new_admin)
        db.session.commit()

        return jsonify(message="Admin created successfully", admin_id=new_admin.id), 201

    except Exception as error:
        print(f'Error creating admin: {error}')
        return jsonify(error="Internal server error"), 500


def controller_update_admin(admin_id):
    try:
        data = request.get_json()

        admin = Admin.query.get(admin_id)
        if not admin:
            return jsonify(error="Admin not found"), 404

        if 'username' in data:
            admin.username = data['username']

        if 'email' in data:
            existing_admin = Admin.query.filter_by(email=data['email']).first()
            if existing_admin and existing_admin.id != admin_id:
                return jsonify(error="Email already exists"), 400
            admin.email = data['email']

        if 'password' in data and data['password']:
            admin.set_password(data['password'])

        db.session.commit()

        return jsonify(message="Admin updated successfully"), 200

    except Exception as error:
        print(f'Error updating admin: {error}')
        return jsonify(error="Internal server error"), 500
