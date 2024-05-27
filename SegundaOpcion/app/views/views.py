from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main.route('/alumnos')
@login_required
def alumnos():
    return render_template('alumnos.html')

@main.route('/municipios')
@login_required
def municipios():
    return render_template('municipios.html')
