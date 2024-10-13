from flask import render_template, redirect, url_for

from . import pageBlueprint, render_template
from app.routes.auth import session

@pageBlueprint.route('/')
def test():
    return render_template('test.html', title='Test Page')

@pageBlueprint.route('/home')
def home():
    if 'is_logged_in' in session:
        return render_template('home.html', title='Home Page')
    else:
        return redirect(url_for('pages.login_customer'))

