"""Blueprint to organize and group, views related
to the '/auth' endpoint of HTTP REST API.
"""

from flask import (
    abort, Blueprint, request, Response, make_response, jsonify, session
)
from Backend.app.model import User
from Backend.app.database import db
from flask_jwt_extended import create_access_token, get_jwt
from Backend.app import blacklisted_tokens


bp = Blueprint('autho', __name__, url_prefix='/autho')


@bp.route('/login', methods=('POST',))
def login() -> Response:
    """Login of the user by creating a valid token.

    Returns:
        response: flask.Response object with the application/json mimetype.
    """

    data = request.json

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter(User.username == username).first()
    if user and user.authenticate(password):
        session['user_id'] = user.id
        access_token = create_access_token(identity=user.id)
        return make_response(jsonify({
            'data': {
                'user': user.to_dict(),
                'access_token': access_token
            }
        }), 200)

    else:
        return make_response(jsonify({
            'status': 'error',
            'data': '401 Unauthorized'
        }), 401)

@bp.route('/logout', methods=('POST',))
def delete() -> Response:
    jti = get_jwt()["jti"]  # Get unique token identifier
    blacklisted_tokens.add(jti)

    return make_response({}, 401)