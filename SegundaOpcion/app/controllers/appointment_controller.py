from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from ..models.appointment import Appointment

appointment = Blueprint('appointment', __name__)

@appointment.route('/create', methods=['GET', 'POST'])
@login_required
def create_appointment():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        description = request.form['description']
        Appointment.create(current_user.id, date, time, description)
        flash('Cita creada exitosamente')
        return redirect(url_for('main.dashboard'))
    return render_template('create_appointment.html')

@appointment.route('/list')
@login_required
def list_appointments():
    appointments = Appointment.get_by_user_id(current_user.id)
    return render_template('appointments.html', appointments=appointments)

@appointment.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_appointment(id):
    Appointment.delete(id)
    flash('Cita eliminada exitosamente')
    return redirect(url_for('appointment.list_appointments'))
