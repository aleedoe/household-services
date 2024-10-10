from app.routes import pageBlueprint, render_template

@pageBlueprint.route('/service-professionals/')
def service_professional_test():
    return render_template('service_professional/test.html')

@pageBlueprint.route('/service-professionals/service-request/')
def service_professional_request():
    return render_template('service_professional/req_service_professional.html')

@pageBlueprint.route('/service-professionals/service-assigned/')
def service_professional_assigned():
    return render_template('service_professional/ass_service_professional.html')

@pageBlueprint.route('/service-professionals/service-review/')
def service_professional_review():
    return render_template('service_professional/review_service_professional.html')