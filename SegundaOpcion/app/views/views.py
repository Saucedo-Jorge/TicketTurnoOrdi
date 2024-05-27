from flask import Blueprint, render_template, session, redirect, url_for
from functools import wraps

bp = Blueprint('views', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@bp.route('/appointments')
@login_required
def appointments():
    return render_template('appointments.html')
