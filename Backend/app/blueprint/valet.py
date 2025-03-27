from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp_valet = Blueprint('valet', __name__, url_prefix='/valet')

@bp_valet.route('/request-service', methods=['POST'])
@jwt_required()
def request_service():
    user = get_jwt_identity()
    data = request.json
    return jsonify({'status': 'success', 'message': 'Service requested', 'user': user, 'details': data}), 200

@bp_valet.route('/start-service', methods=['POST'])
@jwt_required()
def start_service():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Service started', 'details': data}), 200

@bp_valet.route('/end-service', methods=['POST'])
@jwt_required()
def end_service():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Service ended', 'details': data}), 200

@bp_valet.route('/cancel-service', methods=['POST'])
@jwt_required()
def cancel_service():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Service canceled', 'details': data}), 200

@bp_valet.route('/pre-service-photo', methods=['POST'])
@jwt_required()
def pre_service_photo():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Pre-service photo uploaded', 'details': data}), 200

@bp_valet.route('/post-service-photo', methods=['POST'])
@jwt_required()
def post_service_photo():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Post-service photo uploaded', 'details': data}), 200

@bp_valet.route('/key-photo', methods=['POST'])
@jwt_required()
def key_photo():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Key photo uploaded', 'details': data}), 200
