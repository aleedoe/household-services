from app.routes import pageBlueprint, render_template

@pageBlueprint.route('/admin/')
def admin_test():
    return render_template('admin/test.html')