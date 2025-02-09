from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userprofile.db'  # Cambia según tu BD
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from UserProfile.routes.profile import profile_bp
    app.register_blueprint(profile_bp, url_prefix='/profile')

    return app
