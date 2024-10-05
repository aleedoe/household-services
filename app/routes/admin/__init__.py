from app.routes import pageBlueprint, render_template

@pageBlueprint.route('/admin/')
def admin_test():
    return render_template('admin/test.html')


@pageBlueprint.route('/admin/services')
def admin_services():
    return render_template('admin/services.html')