from flask import render_template, request, redirect, url_for, session, flash
import requests
from app.routes import pageBlueprint, render_template


# Admin login route
@pageBlueprint.route('/login-admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST' and 'loginName' in request.form and 'loginPassword' in request.form:
        login_name = request.form['loginName']
        password = request.form['loginPassword']

        # Mengirim data sebagai JSON
        api_url = 'http://localhost:5000/api/login-admin'
        api_data = {'loginName': login_name, 'loginPassword': password}
        response = requests.post(api_url, json=api_data)

        if response.status_code == 200:
            api_response = response.json()

            # Simpan session jika login berhasil
            session['is_logged_in'] = True
            session['username'] = api_response['user_name']
            session['id_user'] = api_response['user_id']
            session['role'] = 'admin'
            return redirect(url_for('pages.admin_services'))

        flash('Invalid admin credentials. Please try again.', 'error')

    if session.get('is_logged_in'):
        return redirect(url_for('pages.home'))

    return render_template('/admin/login.html')


@pageBlueprint.route('/login-customer', methods=['GET', 'POST'])
def login_customer():
    if request.method == 'POST' and 'loginName' in request.form and 'loginPassword' in request.form:
        login_name = request.form['loginName']
        password = request.form['loginPassword']

        # Mengirim data sebagai JSON
        api_url = 'http://localhost:5000/api/login-customer'
        api_data = {'loginName': login_name, 'loginPassword': password}
        response = requests.post(api_url, json=api_data)

        if response.status_code == 200:
            api_response = response.json()

            # Simpan session jika login berhasil
            session['is_logged_in'] = True
            session['username'] = api_response['user_name']
            session['id_user'] = api_response['user_id']
            session['role'] = 'customer'
            return redirect(url_for('pages.home'))

        flash('Invalid customer credentials. Please try again.', 'error')

    if session.get('is_logged_in'):
        return redirect(url_for('pages.home'))

    return render_template('login.html')


@pageBlueprint.route('/register-customer', methods=['GET', 'POST'])
def register_customer():
    if request.method == 'POST' and all(k in request.form for k in ('username', 'password', 'email', 'phone', 'address')):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        # Mengirim data sebagai JSON
        api_url = 'http://localhost:5000/api/register-customer'
        api_data = {
            'username': username,
            'password': password,
            'email': email,
            'phone': phone,
            'address': address
        }
        response = requests.post(api_url, json=api_data)

        if response.status_code == 201:
            flash('Customer registered successfully', 'success')
            return redirect(url_for('pages.login_customer'))

        flash('Error registering customer. Please try again.', 'error')

    return render_template('register.html')


@pageBlueprint.route('/login-service_pro', methods=['GET', 'POST'])
def login_service_pro():
    if request.method == 'POST' and 'loginName' in request.form and 'loginPassword' in request.form:
        login_name = request.form['loginName']
        password = request.form['loginPassword']

        # Mengirim data sebagai JSON
        api_url = 'http://localhost:5000/api/login-service_pro'
        api_data = {'loginName': login_name, 'loginPassword': password}
        response = requests.post(api_url, json=api_data)

        if response.status_code == 200:
            api_response = response.json()

            # Simpan session jika login berhasil
            session['is_logged_in'] = True
            session['username'] = api_response['user_name']
            session['id_user'] = api_response['user_id']
            session['role'] = 'service_pro'
            return redirect(url_for('pages.home'))

        flash('Invalid service professional credentials. Please try again.', 'error')

    if session.get('is_logged_in'):
        return redirect(url_for('pages.home'))

    return render_template('login_service_pro.html')


@pageBlueprint.route('/register-service_pro', methods=['GET', 'POST'])
def register_service_pro():
    if request.method == 'POST' and all(k in request.form for k in ('username', 'password', 'email', 'service_id', 'experience')):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        service_id = request.form['service_id']
        experience = request.form['experience']
        description = request.form.get('description', '')

        # Mengirim data sebagai JSON
        api_url = 'http://localhost:5000/api/register-service_pro'
        api_data = {
            'username': username,
            'password': password,
            'email': email,
            'service_id': service_id,
            'description': description,
            'experience': experience
        }
        response = requests.post(api_url, json=api_data)

        if response.status_code == 201:
            flash('Service professional registered successfully', 'success')
            return redirect(url_for('pages.login_service_pro'))

        flash('Error registering service professional. Please try again.', 'error')

    return render_template('register_service_pro.html')


@pageBlueprint.route('/logout-admin', methods=['GET'])
def logout_admin():
    # Menghapus session admin
    session.pop('is_logged_in', None)
    session.pop('username', None)
    session.pop('id_user', None)
    session.pop('role', None)
    
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('pages.login_admin'))


@pageBlueprint.route('/logout-customer', methods=['GET'])
def logout_customer():
    # Menghapus session customer
    session.pop('is_logged_in', None)
    session.pop('username', None)
    session.pop('id_user', None)
    session.pop('role', None)

    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('pages.login_customer'))


@pageBlueprint.route('/logout-service_pro', methods=['GET'])
def logout_service_pro():
    # Menghapus session service professional
    session.pop('is_logged_in', None)
    session.pop('username', None)
    session.pop('id_user', None)
    session.pop('role', None)
    
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('pages.login_service_pro'))
