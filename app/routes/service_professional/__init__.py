from app.routes import pageBlueprint, render_template

@pageBlueprint.route('/service-professionals/')
def service_professional_test():
    return render_template('service_professional/test.html')

@pageBlueprint.route('/service-professionals/service-request/')
def service_professional_request():
    return render_template('service_professional/req_service_professional.html')