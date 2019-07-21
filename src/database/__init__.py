"""To startup your database, execute the following
in your python console:

from src.app import app
from src.database import reset_database

with app.app_context():
    reset_database()
"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def reset_database():
    from src.database.models import Product
    db.drop_all()
    db.create_all()
