from flask import request, jsonify, make_response
from app.models import db, ServiceProfessional
import math


def controller_delete_service_professional(professional_id):
    try:
        # Cari service professional berdasarkan ID
        professional = ServiceProfessional.query.get(professional_id)
        if not professional:
            return jsonify(error="Service Professional not found"), 404

        # Hapus service professional
        db.session.delete(professional)
        db.session.commit()

        return jsonify(message="Service Professional deleted successfully"), 200

    except Exception as error:
        print(f'Error deleting service professional: {error}')
        return jsonify(error="Internal server error"), 500


def controller_get_service_professional_by_id(professional_id):
    try:
        # Cari service professional berdasarkan ID
        professional = ServiceProfessional.query.get(professional_id)
        if not professional:
            return jsonify(error="Service Professional not found"), 404

        # Kembalikan data dalam format JSON
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
        # Ambil data dari body request (JSON)
        data = request.get_json()

        # Cek apakah username atau email sudah ada
        existing_professional = ServiceProfessional.query.filter((ServiceProfessional.username == data['username']) | (ServiceProfessional.email == data['email'])).first()
        if existing_professional:
            return jsonify(error="Username or email already exists"), 400

        # Buat service professional baru
        new_professional = ServiceProfessional(
            service_id=data['service_id'],
            username=data['username'],
            email=data['email'],
            description=data.get('description'),
            experience=data['experience'],
            verified_status=data.get('verified_status', False)
        )
        new_professional.set_password(data['password'])  # Hash password dan simpan

        db.session.add(new_professional)
        db.session.commit()

        return jsonify(message="Service Professional created successfully", professional_id=new_professional.id), 201

    except Exception as error:
        print(f'Error creating service professional: {error}')
        return jsonify(error="Internal server error"), 500


def controller_update_service_professional(professional_id):
    try:
        # Ambil data dari body request (JSON)
        data = request.get_json()

        # Cari service professional berdasarkan ID
        professional = ServiceProfessional.query.get(professional_id)
        if not professional:
            return jsonify(error="Service Professional not found"), 404

        # Update service_id jika ada
        if 'service_id' in data:
            professional.service_id = data['service_id']

        # Update username jika ada
        if 'username' in data:
            # Cek apakah username sudah digunakan oleh professional lain
            existing_professional = ServiceProfessional.query.filter_by(username=data['username']).first()
            if existing_professional and existing_professional.id != professional_id:
                return jsonify(error="Username already exists"), 400
            professional.username = data['username']

        # Update email jika ada
        if 'email' in data:
            # Cek apakah email sudah digunakan oleh professional lain
            existing_professional = ServiceProfessional.query.filter_by(email=data['email']).first()
            if existing_professional and existing_professional.id != professional_id:
                return jsonify(error="Email already exists"), 400
            professional.email = data['email']

        # Update description jika ada
        if 'description' in data:
            professional.description = data['description']

        # Update experience jika ada
        if 'experience' in data:
            professional.experience = data['experience']

        # Update verified_status jika ada
        if 'verified_status' in data:
            professional.verified_status = data['verified_status']

        # Update password jika ada
        if 'password' in data and data['password']:
            professional.set_password(data['password'])

        # Simpan perubahan ke database
        db.session.commit()

        return jsonify(message="Service Professional updated successfully"), 200

    except Exception as error:
        print(f'Error updating service professional: {error}')
        return jsonify(error="Internal server error"), 500
