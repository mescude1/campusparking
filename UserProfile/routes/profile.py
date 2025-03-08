from flask import Blueprint, jsonify
from UserProfile.models.user_model import User

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email})


