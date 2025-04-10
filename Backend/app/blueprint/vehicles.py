from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore

bp_vehicles = Blueprint('vehicles', __name__, url_prefix='/vehicles')

@bp_vehicles.route('/new-vehicle', methods=['POST'])
@jwt_required()
def new_vehicle():
    user = get_jwt_identity()
    data = request.json
    return jsonify({'status': 'success', 'message': 'Vehicle registered', 'user': user, 'details': data}), 200

@bp_vehicles.route('/edit-vehicle', methods=['POST'])
@jwt_required()
def edit_vehicle():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Vehicle updated', 'details': data}), 200

@bp_vehicles.route('/vehicle/<int:vehicle_id>', methods=['GET'])
@jwt_required()
def get_vehicle(vehicle_id):
    return jsonify({'status': 'success', 'message': 'Vehicle details', 'vehicle_id': vehicle_id}), 200
