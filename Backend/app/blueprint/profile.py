from flask import Blueprint, Response, request, jsonify, abort, make_response, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from Backend.app.model import User


bp_profile = Blueprint('profile', __name__, url_prefix='/profile')

@bp_profile.route('/register', methods=('POST',))
def register() -> Response:
    """Register a new user.

    Returns:
        response: flask.Response object with the application/json mimetype.
    """

    if not request.is_json:
        abort(400)

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username and password:
        new_user = User()
        new_user.username = username
        new_user.password_hash = password

        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id

    response = make_response(jsonify({
        'status': 'success',
        'data': {
            'message': "Registration successful! Please log in."
        }
    }), 200)

    return response

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

@bp_profile.route('/generate-enrollment-contracts', methods=['POST'])
@jwt_required()
def generate_enrollment_contracts():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Enrollment contracts generated', 'details': data}), 200
