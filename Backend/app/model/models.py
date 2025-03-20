"""This module define all models (persistent objects - PO) of application. Each model
is a subclasse of the Base class (base declarative) from app.model.database module.
The declarative extension in SQLAlchemy allows to define tables and models in one go,
that is in the same class.
"""
import hashlib


from sqlalchemy import inspect

from Backend.app.database import db
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property



class Model:
    """The Model class declare the serialize() method that is
    supposed to serializes the model data. The Model's subclasses
    can provide a implementation of this method."""

    def serialize(self) -> dict:
        """Serialize the object attributes values into a dictionary."""

        return {}

    def remove_session(self):
        """Removes an object from the session its current session."""

        session = inspect(self).session
        if session:
            session.expunge(self)


class User(UserMixin, db.Model):
    """ User's model class.

    Column:
        id (integer, primary key)
        username (string, unique)
        password (string)

    Attributes:
        username (str): User's username
        password (str): User's password
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        # Generate SHA-256 hash
        self._password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def authenticate(self, password):
        # Check if the given password matches the stored hash
        return self._password_hash == hashlib.sha256(password.encode('utf-8')).hexdigest()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
        }
