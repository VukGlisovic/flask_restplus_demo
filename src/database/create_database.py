from src.app import app
from src.database import reset_database


# the app is already initialized
with app.app_context():
    reset_database()
