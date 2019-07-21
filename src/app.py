import logging
from flask import Flask, Blueprint
from src.backend.restplus import api
from src import settings
from src.backend.endpoints.groceries_list import ns as ns_groceries_list
from src.database import db
from src.constants import URL_PREFIX


logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)


def configure_app(flask_app):
    logging.info("Configuring app...")
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME

    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS


def initialize_app(flask_app):
    logging.info("Configuring app...")
    configure_app(flask_app)
    logging.info("Setting up API...")
    blueprint = Blueprint('api', __name__, url_prefix=URL_PREFIX)
    api.init_app(blueprint)
    api.add_namespace(ns_groceries_list)
    flask_app.register_blueprint(blueprint)
    logging.info("Initializing database...")
    db.init_app(flask_app)


configure_app(app)
initialize_app(app)
logging.info('>>>>> Starting development server at http://{}{}/ <<<<<'.format(app.config['SERVER_NAME'], URL_PREFIX))


if __name__ == "__main__":
    app.run(debug=settings.FLASK_DEBUG)
