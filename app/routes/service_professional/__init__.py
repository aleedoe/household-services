from app.routes import pageBlueprint, render_template

@pageBlueprint.route('/service-professionals/')
def service_professional_test():
    return render_template('service_professional/test.html')