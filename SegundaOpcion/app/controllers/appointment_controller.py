from flask import Blueprint, request, jsonify
from flask_login import login_required
from ..models.appointment import Appointment
from ..models.detalle_cita import DetalleCita

bp = Blueprint('appointments', __name__)

@bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    alumno_id = data.get('alumno_id')
    descripcion = data.get('descripcion')
    cita_id = Appointment.create(alumno_id)
    DetalleCita.create(cita_id, descripcion)
    return jsonify({'cita_id': cita_id}), 201

@bp.route('/appointments/<int:id>', methods=['PATCH'])
@login_required
def update_appointment_status(id):
    data = request.get_json()
    status = data.get('status')
    Appointment.update_status(id, status)
    return jsonify({'status': status}), 200

@bp.route('/appointments/<int:id>', methods=['DELETE'])
@login_required
def delete_appointment(id):
    Appointment.delete(id)
    return jsonify({'result': 'success'}), 200

@bp.route('/appointments', methods=['GET'])
@login_required
def get_appointments():
    status = request.args.get('status')
    appointments = Appointment.get_all(status)
    return jsonify(appointments), 200

@bp.route('/appointments/<int:id>/details', methods=['GET'])
@login_required
def get_appointment_details(id):
    details = DetalleCita.get_by_cita_id(id)
    return jsonify(details), 200
