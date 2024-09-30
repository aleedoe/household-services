from . import pageBlueprint, render_template

@pageBlueprint.route('/')
def test():
    return render_template('test.html', title='Test Page')