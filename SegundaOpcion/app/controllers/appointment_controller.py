from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..models.appointment import Appointment

appointment = Blueprint('appointment', __name__)

@appointment.route('/create_appointment', methods=['GET', 'POST'])
@login_required
def create_appointment():
    if request.method == 'POST':
        # Obtener los datos del formulario y crear una nueva cita
        date = request.form['date']
        time = request.form['time']
          # ID del usuario actual
        Appointment.create(date, time)
        flash('Cita creada exitosamente')
        return redirect(url_for('main.dashboard'))
    return render_template('create_appointment.html')
