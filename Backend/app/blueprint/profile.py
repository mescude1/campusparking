from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp_profile = Blueprint('profile', __name__, url_prefix='/profile')

@bp_profile.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user = get_jwt_identity()
    return jsonify({'status': 'success', 'message': 'Profile data', 'user': user}), 200

@bp_profile.route('/edit-profile', methods=['POST'])
@jwt_required()
def edit_profile():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Profile updated', 'details': data}), 200
