from app.routes import pageBlueprint, render_template


# Admin login route
@pageBlueprint.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email_or_username = request.form.get('loginName')
        password = request.form.get('loginPassword')
        admin = Admin.query.filter((Admin.email == email_or_username) | (Admin.username == email_or_username)).first()
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('pageBlueprint.admin_services'))
        flash('Invalid credentials for Admin. Please try again.')
    return render_template('admin/login.html')


# Customer login route
@pageBlueprint.route('/customer/login', methods=['GET', 'POST'])
def customer_login():
    if request.method == 'POST':
        email_or_username = request.form.get('loginName')
        password = request.form.get('loginPassword')
        customer = Customer.query.filter((Customer.email == email_or_username) | (Customer.username == email_or_username)).first()
        if customer and customer.check_password(password):
            login_user(customer)
            return redirect(url_for('pageBlueprint.customer_dashboard'))
        flash('Invalid credentials for Customer. Please try again.')
    return render_template('customer/login.html')


# Service Professional login route
@pageBlueprint.route('/service-professional/login', methods=['GET', 'POST'])
def service_professional_login():
    if request.method == 'POST':
        email_or_username = request.form.get('loginName')
        password = request.form.get('loginPassword')
        service_professional = ServiceProfessional.query.filter(
            (ServiceProfessional.email == email_or_username) | 
            (ServiceProfessional.username == email_or_username)).first()
        if service_professional and service_professional.check_password(password):
            login_user(service_professional)
            return redirect(url_for('pageBlueprint.service_professional_dashboard'))
        flash('Invalid credentials for Service Professional. Please try again.')
    return render_template('service_professional/login.html')
