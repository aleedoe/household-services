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
