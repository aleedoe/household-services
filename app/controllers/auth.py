from flask import request, jsonify
from app.models import Admin, Customer, ServiceProfessional, db


def controller_admin_login():
    try:
        data = request.get_json()
        print(data)

        email_or_username = data['loginName']
        password = data['loginPassword']

        admin = Admin.query.filter((Admin.email == email_or_username) | (Admin.username == email_or_username)).first()
        print(admin)

        if admin and admin.check_password(password):
            return jsonify(message="Login successful", user_id=admin.id, user_name=admin.username), 200
        else:
            return jsonify(error="Invalid credentials"), 401

    except Exception as error:
        print(f'Error logging in: {error}')
        return jsonify(error="Internal server error"), 500


def controller_customer_login():
    try:
        data = request.get_json()

        email_or_username = data['loginName']
        password = data['loginPassword']

        customer = Customer.query.filter((Customer.email == email_or_username) | (Customer.username == email_or_username)).first()
        if customer and customer.check_password(password):
            return jsonify(message="Login successful", user_id=customer.id, user_name=customer.username), 200

    except Exception as error:
        print(f'Error logging in: {error}')
        return jsonify(error="Internal server error"), 500


def controller_register_customer():
    try:
        data = request.get_json()

        username = data['username']
        password = data['password']
        email = data['email']
        phone = data['phone']
        address = data['address']

        if Customer.query.filter((Customer.username == username) | (Customer.email == email)).first():
            return jsonify(error="Username or email already exists"), 400

        new_customer = Customer(
            username=username,
            email=email,
            phone=phone,
            address=address
        )
        new_customer.set_password(password)

        db.session.add(new_customer)
        db.session.commit()

        return jsonify(message="Customer registered successfully", user_id=new_customer.id), 201

    except Exception as error:
        print(f'Error registering customer: {error}')
        return jsonify(error="Internal server error"), 500


def controller_service_pro_login():
    try:
        data = request.get_json()

        email_or_username = data['loginName']
        password = data['loginPassword']

        service_pro = ServiceProfessional.query.filter((ServiceProfessional.email == email_or_username) | (ServiceProfessional.username == email_or_username)).first()
        if service_pro and service_pro.check_password(password):
            return jsonify(message="Login successful", user_id=service_pro.id, user_name=service_pro.username), 200

    except Exception as error:
        print(f'Error logging in: {error}')
        return jsonify(error="Internal server error"), 500


def controller_register_service_pro():
    try:
        data = request.get_json()

        username = data['username']
        password = data['password']
        email = data['email']
        service_id = data['service_id']
        description = data.get('description', '')
        experience = data['experience']

        if ServiceProfessional.query.filter((ServiceProfessional.username == username) | (ServiceProfessional.email == email)).first():
            return jsonify(error="Username or email already exists"), 400

        new_service_pro = ServiceProfessional(
            username=username,
            email=email,
            service_id=service_id,
            description=description,
            experience=experience
        )
        new_service_pro.set_password(password)

        db.session.add(new_service_pro)
        db.session.commit()

        return jsonify(message="Service professional registered successfully", user_id=new_service_pro.id), 201

    except Exception as error:
        print(f'Error registering service professional: {error}')
        return jsonify(error="Internal server error"), 500