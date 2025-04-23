import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # O cambia a PostgreSQL/MySQL si usas otro motor
    SQLALCHEMY_TRACK_MODIFICATIONS = False
