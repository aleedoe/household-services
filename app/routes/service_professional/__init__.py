from flask import render_template, redirect, url_for

from app.routes import pageBlueprint, render_template
from app.routes.auth import session


@pageBlueprint.route('/service-professionals/')
def service_professional_test():
    if 'is_logged_in' in session:
        return render_template('service_professional/test.html')
    else:
        return redirect(url_for('pages.login_customer'))

@pageBlueprint.route('/service-professionals/service-request/')
def service_professional_request():
    if 'is_logged_in' in session:
        return render_template('service_professional/req_service_professional.html')
    else:
        return redirect(url_for('pages.login_customer'))

@pageBlueprint.route('/service-professionals/service-assigned/')
def service_professional_assigned():
    if 'is_logged_in' in session:
        return render_template('service_professional/ass_service_professional.html')
    else:
        return redirect(url_for('pages.login_customer'))

@pageBlueprint.route('/service-professionals/service-review/')
def service_professional_review():
    if 'is_logged_in' in session:
        return render_template('service_professional/review_service_professional.html')
    else:
        return redirect(url_for('pages.login_customer'))
