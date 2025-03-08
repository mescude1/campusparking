from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from BackendUP.config import Config
from BackendUP.database import db
from BackendUP.routes.profile import profile_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos con la app
    db.init_app(app)

    # Registrar rutas
    app.register_blueprint(profile_bp)

    return app
