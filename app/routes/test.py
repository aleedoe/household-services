from . import pageBlueprint, render_template

@pageBlueprint.route('/')
def test():
    return render_template('test.html', title='Test Page')

@pageBlueprint.route('/home')
def home():
    return render_template('home.html', title='Home Page')

