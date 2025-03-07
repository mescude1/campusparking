"""Blueprint to organize and group, views related
to the '/auth' endpoint of HTTP REST API.
"""

from flask import (
    abort, Blueprint, request, Response, make_response, jsonify, redirect, url_for, flash, session
)

from Backend.app.model import User
from werkzeug.security import check_password_hash

from wsgi import app

bp = Blueprint('autho', __name__, url_prefix='/autho')


@bp.route('/register', methods=('POST',))
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

        app.db.session.add(new_user)
        app.db.session.commit()

        session['user_id'] = new_user.id

    response = make_response(jsonify({
        'status': 'success',
        'data': {
            'message': "Registration successful! Please log in."
        }
    }), 200)

    return response


@bp.route('/login', methods=('POST',))
def login() -> Response:
    """Login of the user by creating a valid token.

    Returns:
        response: flask.Response object with the application/json mimetype.
    """

    data = request.json

    username = request.get_json()['username']
    password = request.get_json()['password']

    user = User.query.filter(User.username == username).first()
    if user and user.authenticate(password):
        session['user_id'] = user.id
        return make_response(jsonify({
            'user': user.to_dict(),
            'data': {}
        }), 200)

    else:
        return make_response(jsonify({
            'status': 'error',
            'data': '401 Unauthorized'
        }), 401)


@bp.route('/check-session', methods=('get',))
def check_session() -> Response:
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return make_response(jsonify({
                'user': user.to_dict(),
                'data': {}
            }), 200)
        return make_response(jsonify({
            'status': 'error',
            'data': '401 Unauthorized'
        }), 401)

@bp.route('/logout', methods=('POST',))
def delete() -> Response:
    if session.get('user_id'):
        session['user_id'] = None
        return make_response({}, 401)
    else:
        return make_response(jsonify({
            'status': 'error',
            'data': '401 Unauthorized'
        }), 401)
