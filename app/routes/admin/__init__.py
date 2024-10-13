from flask import render_template, redirect, url_for

from app.routes import pageBlueprint, render_template
from app.routes.auth import session

@pageBlueprint.route('/admin/')
def admin_test():
    if 'is_logged_in' in session:
        return render_template('admin/test.html')
    else:
        return redirect(url_for('pages.login_admin'))

@pageBlueprint.route('/admin/services')
def admin_services():
    if 'is_logged_in' in session:
        return render_template('admin/services.html')
    else:
        return redirect(url_for('pages.login_admin'))

@pageBlueprint.route('/admin/customers')
def admin_customers():
    if 'is_logged_in' in session:
        return render_template('admin/customers.html')
    else:
        return redirect(url_for('pages.login_admin'))

@pageBlueprint.route('/admin/service-professionals')
def admin_service_professionals():
    if 'is_logged_in' in session:
        return render_template('admin/service_professional.html')
    else:
        return redirect(url_for('pages.login_admin'))

@pageBlueprint.route('/admin/admins')
def admin_service_admins():
    if 'is_logged_in' in session:
        return render_template('admin/admins.html')
    else:
        return redirect(url_for('pages.login_admin'))

@pageBlueprint.route('/admin/req-services')
def admin_req_service_admins():
    if 'is_logged_in' in session:
        return render_template('admin/req_services.html')
    else:
        return redirect(url_for('pages.login_admin'))

@pageBlueprint.route('/admin/req-services-pro')
def admin_req_service_pro_admins():
    if 'is_logged_in' in session:
        return render_template('admin/req_service_pro.html')
    else:
        return redirect(url_for('pages.login_admin'))