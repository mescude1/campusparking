from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash
from Backend.app.database import db
from Backend.app.model import User

bp_profile = Blueprint('profile', __name__, url_prefix='/profile')

@bp_profile.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    if not request.is_json:
        abort(400)

    data = request.get_json()

    # Verificar que los datos requeridos están presentes
    required_fields = ["username", "password", "name", "last_name", "email", 
                       "cellphone", "type", "profile_img", "id_img", 
                       "driver_license_img", "contract", "vehicle_type"]

    for field in required_fields:
        if field not in data:
            return jsonify({'status': 'error', 'message': f'Missing field: {field}'}), 400

    # Crear nuevo usuario
    new_user = User(
        username=data["username"],
        _password_hash=generate_password_hash(data["password"]),  # Hasheo de contraseña
        name=data["name"],
        last_name=data["last_name"],
        email=data["email"],
        cellphone=data["cellphone"],
        type=data["type"],
        profile_img=data["profile_img"],
        id_img=data["id_img"],
        driver_license_img=data["driver_license_img"],
        contract=data["contract"],
        vehicle_type=data["vehicle_type"],
        is_deleted=False
    )

    # Guardar en la base de datos
    db.session.add(new_user)
    db.session.commit()

    # Crear un token JWT para el usuario registrado
    access_token = create_access_token(identity=new_user.id)

    return jsonify({'status': 'success', 'message': 'User registered', 'access_token': access_token}), 201

@bp_profile.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Obtener datos del perfil del usuario autenticado."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

    user_data = {
        "id": user.id,
        "username": user.username,
        "name": user.name,
        "last_name": user.last_name,
        "email": user.email,
        "cellphone": user.cellphone,
        "type": user.type,
        "profile_img": user.profile_img,
        "id_img": user.id_img,
        "driver_license_img": user.driver_license_img,
        "contract": user.contract,
        "vehicle_type": user.vehicle_type
    }

    return jsonify({'status': 'success', 'message': 'Profile data', 'user': user_data}), 200

@bp_profile.route('/edit-profile', methods=['POST'])
@jwt_required()
def edit_profile():
    """Actualizar datos del perfil del usuario autenticado."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

    data = request.json
    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)

    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Profile updated'}), 200

@bp_profile.route('/generate-enrollment-contracts', methods=['POST'])
@jwt_required()
def generate_enrollment_contracts():
    """Generar contratos de inscripción para el usuario autenticado."""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

    data = request.json
    user.contract = data.get("contract", user.contract)

    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Enrollment contracts generated'}), 200
