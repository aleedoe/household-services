from flask import request, jsonify, make_response
from app.models import db, Customer
import math


def controller_delete_customer(customer_id):
    try:
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify(error="Customer not found"), 404

        db.session.delete(customer)
        db.session.commit()

        return jsonify(message="Customer deleted successfully"), 200

    except Exception as error:
        print(f'Error deleting customer: {error}')
        return jsonify(error="Internal server error"), 500


def controller_get_customer_by_id(customer_id):
    try:
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify(error="Customer not found"), 404

        return jsonify({
            "id": customer.id,
            "username": customer.username,
            "email": customer.email,
            "phone": customer.phone,
            "address": customer.address,
            "created_at": customer.created_at
        }), 200

    except Exception as error:
        print(f'Error fetching customer: {error}')
        return jsonify(error="Internal server error"), 500


def controller_create_customer():
    try:
        data = request.get_json()

        existing_customer = Customer.query.filter((Customer.username == data['username']) | (Customer.email == data['email'])).first()
        if existing_customer:
            return jsonify(error="Username or email already exists"), 400

        new_customer = Customer(
            username=data['username'],
            email=data['email'],
            phone=data['phone'],
            address=data['address']
        )
        new_customer.set_password(data['password'])

        db.session.add(new_customer)
        db.session.commit()

        return jsonify(message="Customer created successfully", customer_id=new_customer.id), 201

    except Exception as error:
        print(f'Error creating customer: {error}')
        return jsonify(error="Internal server error"), 500


def controller_update_customer(customer_id):
    try:
        data = request.get_json()

        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify(error="Customer not found"), 404

        if 'username' in data:
            existing_customer = Customer.query.filter_by(username=data['username']).first()
            if existing_customer and existing_customer.id != customer_id:
                return jsonify(error="Username already exists"), 400
            customer.username = data['username']

        if 'email' in data:
            existing_customer = Customer.query.filter_by(email=data['email']).first()
            if existing_customer and existing_customer.id != customer_id:
                return jsonify(error="Email already exists"), 400
            customer.email = data['email']

        if 'phone' in data:
            customer.phone = data['phone']

        if 'address' in data:
            customer.address = data['address']

        if 'password' in data and data['password']:
            customer.set_password(data['password'])

        db.session.commit()

        return jsonify(message="Customer updated successfully"), 200

    except Exception as error:
        print(f'Error updating customer: {error}')
        return jsonify(error="Internal server error"), 500
