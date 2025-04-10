from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

bp_display = Blueprint('display', __name__, url_prefix='/display')

@bp_display.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    return jsonify({'status': 'success', 'message': 'Dashboard data'}), 200

@bp_display.route('/services', methods=['GET'])
@jwt_required()
def get_services():
    return jsonify({'status': 'success', 'message': 'List of services'}), 200

@bp_display.route('/vehicles', methods=['GET'])
@jwt_required()
def get_vehicles():
    return jsonify({'status': 'success', 'message': 'List of vehicles'}), 200
