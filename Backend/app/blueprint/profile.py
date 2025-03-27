from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

@bp.route('/register', methods=('POST',))
def register() -> Response:
    """Register a new user.

    Returns:
        response: flask.Response object with the application/json mimetype.
    """

    if not request.is_json:
        abort(400)

    user_repository = UserRepository()

    # creating a User object
    user = User()
    user.username = request.json.get('username')
    user.password = request.json.get('password')

    # validating the user
    is_invalid = user_repository.is_invalid(user)
    if not is_invalid:
        user_repository.save(user)
        return make_response(jsonify({
            'status': 'success',
            'data': user.serialize()
        }), 200)
    else:
        response = make_response(jsonify({
            'status': 'fail',
            'data': is_invalid
        }), 400)

    return response

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

@bp_profile.route('/generate-enrollment-contracts', methods=['POST'])
@jwt_required()
def generate_enrollment_contracts():
    data = request.json
    return jsonify({'status': 'success', 'message': 'Enrollment contracts generated', 'details': data}), 200
