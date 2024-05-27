from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models.user import User

admin = Blueprint('admin', __name__)

@admin.route('/register_student', methods=['GET', 'POST'])
@login_required
def register_student():
    if not current_user.is_authenticated or current_user.role != 'admin':
        flash('Acceso denegado.')
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        # Lógica para registrar un estudiante
        pass

    return render_template('register_student.html')

@admin.route('/register_municipality', methods=['GET', 'POST'])
@login_required
def register_municipality():
    if not current_user.is_authenticated or current_user.role != 'admin':
        flash('Acceso denegado.')
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        # Lógica para registrar un municipio
        pass

    return render_template('register_municipality.html')
